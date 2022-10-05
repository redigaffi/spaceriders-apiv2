from dataclasses import dataclass
import datetime

from pydantic import BaseModel

from core.shared.models import AppBaseException, BKMTransaction, ShadyActivityException
from core.shared.ports import (
    BKMDepositRepositoryPort,
    ChainServicePort,
    LoggingPort,
    PlanetRepositoryPort,
    ResponsePort,
)


class RecoverBKMTransactionRequest(BaseModel):
    planet_id: str


class BKMTransactionRequest(BaseModel):
    planet_id: str
    deposit_id: str
    amount: float = None
    type: str = None


class BKMWithdrawResponse(BaseModel):
    amount: str
    planet_id: str
    v: str
    r: str
    s: str


class BKMTransactionNotFoundSmartContractException(AppBaseException):
    msg = "$BKM transaction not found in the smart contract, did you execute the transaction?"


class BKMTransactionAlreadyExistsException(AppBaseException):
    msg = "$BKM transaction with given id already exists"


class BKMTransactionFailedWrongTypeException(AppBaseException):
    msg = "Transaction type is wrong..."


class BKMWithdrawFailedNotEnoughFunds(AppBaseException):
    msg = "Not enough $BKM to withdraw"


@dataclass
class PlanetBKM:
    bkm_repository_port: BKMDepositRepositoryPort
    planet_repository_port: PlanetRepositoryPort
    logging_port: LoggingPort
    contract_service: ChainServicePort
    response_port: ResponsePort

    async def recover_transactions(
        self, request: RecoverBKMTransactionRequest
    ) -> list[BKMTransaction]:

        planet = await self.planet_repository_port.get(request.planet_id)

        energy_deposit_count = await self.contract_service.spaceriders_game_call(
            "getBkmTransactionMapCount", str(request.planet_id)
        )

        result = []
        for i in range(energy_deposit_count):
            energy_deposit_id_sm = await self.contract_service.spaceriders_game_call(
                "bkmTransactionMap", str(request.planet_id), i
            )
            energy_deposit = await self.bkm_repository_port.get(energy_deposit_id_sm)

            if energy_deposit is None:
                await self.logging_port.info(
                    "Found a $BKM transaction on blockchain which was not in our database"
                )
                energy_deposit_info = await self.contract_service.spaceriders_game_call(
                    "bkmTransactions", energy_deposit_id_sm
                )
                planet_id_sm = energy_deposit_info[1]
                owner = energy_deposit_info[2]
                created_timestamp = energy_deposit_info[3]
                amount = energy_deposit_info[4]
                tx_type = energy_deposit_info[6]

                token_amount = amount / 10**18

                energy_deposit = BKMTransaction(
                    request_id=energy_deposit_id_sm,
                    created_time=created_timestamp,
                    token_amount=token_amount,
                    planet_id=request.planet_id,
                    was_recovered=True,
                    type=tx_type,
                )

                energy_deposit = await self.bkm_repository_port.create_bkm_transaction(
                    energy_deposit
                )
                planet.bkm_deposits.append(energy_deposit)

                if tx_type == "deposit":
                    planet.resources.bkm += token_amount
                elif tx_type == "withdraw":
                    planet.resources.bkm -= token_amount

                planet = await self.planet_repository_port.update(planet)
                result.append(energy_deposit)

        return await self.response_port.publish_response(result)

    async def withdraw(self, user: str, request: BKMTransactionRequest):
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        if planet.resources.bkm < request.amount:
            raise BKMWithdrawFailedNotEnoughFunds()

        amount = int(request.amount * 10**18)
        signed_msg = await self.contract_service.sign_message(
            ["uint256", "string", "address"], [amount, str(planet.id), user]
        )

        response = BKMWithdrawResponse(
            planet_id=request.planet_id,
            amount=amount,
            v=signed_msg["v"],
            r=signed_msg["r"],
            s=signed_msg["s"],
        )

        return await self.response_port.publish_response(response)

    async def create_transaction(
        self, user: str, request: BKMTransactionRequest
    ) -> BKMTransaction:
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        bkm_deposit = await self.bkm_repository_port.get(request.deposit_id)
        if bkm_deposit is not None:
            raise BKMTransactionAlreadyExistsException()

        bkm_deposit_info = await self.contract_service.spaceriders_game_call(
            "bkmTransactions", request.deposit_id
        )
        planet_id_sm = bkm_deposit_info[1]
        owner = bkm_deposit_info[2]
        created_timestamp = bkm_deposit_info[3]
        amount = bkm_deposit_info[4]
        exists = bkm_deposit_info[5]
        tx_type = bkm_deposit_info[6]
        fee_wei = bkm_deposit_info[7]

        if not exists:
            raise BKMTransactionNotFoundSmartContractException()

        if tx_type != request.type:
            raise BKMTransactionFailedWrongTypeException()

        if (owner.lower() != user.lower()) or (request.planet_id != planet_id_sm):
            raise ShadyActivityException()

        token_amount = amount / 10**18
        fee = fee_wei / 10**18

        now = datetime.datetime.timestamp(datetime.datetime.now())

        bkm_deposit = BKMTransaction(
            request_id=request.deposit_id,
            created_time=now,
            token_amount=token_amount,
            planet_id=request.planet_id,
            was_recovered=False,
            type=tx_type,
        )

        bkm_deposit = await self.bkm_repository_port.create_bkm_transaction(bkm_deposit)
        planet.bkm_deposits.append(bkm_deposit)
        if tx_type == "deposit":
            planet.resources.bkm += token_amount - fee
        elif tx_type == "withdraw":
            planet.resources.bkm -= token_amount

        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(bkm_deposit)
