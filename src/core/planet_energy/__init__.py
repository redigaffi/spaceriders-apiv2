from pydantic import BaseModel

from core.shared.models import AppBaseException, ShadyActivityException
from core.shared.models import EnergyDeposit
from core.shared.ports import ResponsePort, PlanetRepositoryPort, LoggingPort, ChainServicePort, \
    EnergyDepositRepositoryPort, TokenPricePort
from dataclasses import dataclass
import datetime


class PlanetEnergyRecoverEnergyDepositsRequest(BaseModel):
    planet_id: str


class EnergyDepositRequest(BaseModel):
    planet_id: str
    deposit_id: str
    amount: float = None


class EnergyDepositNotFoundSmartContractException(AppBaseException):
    msg = "Energy deposit not found in the smart contract, did you execute the transaction?"


class EnergyDepositAlreadyExistsException(AppBaseException):
    msg = "Energy deposit with given id already exists"


class NotEnoughFreeTokensForEnergyDepositException(AppBaseException):
    msg = "Not holding enough $SPR tokens for energy deposit"


@dataclass
class PlanetEnergy:
    token_price: TokenPricePort
    energy_repository_port: EnergyDepositRepositoryPort
    planet_repository_port: PlanetRepositoryPort
    logging_port: LoggingPort
    contract_service: ChainServicePort
    response_port: ResponsePort

    async def recover_deposits(self, request: PlanetEnergyRecoverEnergyDepositsRequest) -> list[EnergyDeposit]:

        planet = await self.planet_repository_port.get(request.planet_id)

        energy_deposit_count = await self.contract_service.spaceriders_game_call("getEnergyDepositsMapCount", request.planet_id)

        result = []
        for i in range(energy_deposit_count):
            energy_deposit_id_sm = await self.contract_service.spaceriders_game_call("energyDepositsMap", request.planet_id, i)
            energy_deposit = await self.energy_repository_port.get(energy_deposit_id_sm)

            if energy_deposit is None:
                energy_deposit_info = await self.contract_service.spaceriders_game_call("energyDeposits", energy_deposit_id_sm)
                planet_id_sm = energy_deposit_info[1]
                owner = energy_deposit_info[2]
                created_timestamp = energy_deposit_info[3]
                amount = energy_deposit_info[4]

                token_amount = amount / 10 ** 18
                usd_value = token_amount * await self.token_price.fetch_token_price_usd()

                energy_deposit = EnergyDeposit(id=energy_deposit_id_sm,
                                               created_time=created_timestamp,
                                               token_amount=token_amount,
                                               usd_value=usd_value,
                                               planet_id=request.planet_id,
                                               was_recovered=True)

                await self.energy_repository_port.create_energy_deposit(energy_deposit)
                planet.energy_deposits.append(energy_deposit)
                await self.planet_repository_port.update(planet)
                result.append(energy_deposit)

        return await self.response_port.publish_response(result)

    async def create_deposit(self, user: str, request: EnergyDepositRequest) -> EnergyDeposit:
        planet = await self.planet_repository_port.get_my_planet(user, request.planet_id)

        energy_deposit = await self.energy_repository_port.get(request.deposit_id)
        if energy_deposit is not None:
            raise EnergyDepositAlreadyExistsException()

        if planet.is_free():
            if planet.free_tokens < request.amount:
                raise NotEnoughFreeTokensForEnergyDepositException()

            now = datetime.datetime.timestamp(datetime.datetime.now())
            usd_value = request.amount * await self.token_price.fetch_token_price_usd()

            energy_deposit = EnergyDeposit(id=request.deposit_id,
                                           created_time=now,
                                           token_amount=request.amount,
                                           usd_value=usd_value,
                                           planet_id=request.planet_id,
                                           was_recovered=False)

            await self.energy_repository_port.create_energy_deposit(energy_deposit)

            planet.free_tokens -= request.amount
            planet.resources.energy += usd_value
            planet.energy_deposits.append(energy_deposit)
            await self.planet_repository_port.update(planet)

            return await self.response_port.publish_response(energy_deposit)

        energy_deposit_info = await self.contract_service.spaceriders_game_call("energyDeposits", request.deposit_id)
        planet_id_sm = energy_deposit_info[1]
        owner = energy_deposit_info[2]
        created_timestamp = energy_deposit_info[3]
        amount = energy_deposit_info[4]
        exists = energy_deposit_info[5]

        if not exists:
            raise EnergyDepositNotFoundSmartContractException()

        if (owner.lower() != user.lower()) or (request.planet_id != planet_id_sm):
            raise ShadyActivityException()

        token_amount = amount / 10 ** 18
        usd_value = token_amount * await self.token_price.fetch_token_price_usd()

        now = datetime.datetime.timestamp(datetime.datetime.now())

        energy_deposit = EnergyDeposit(id=request.deposit_id,
                                       created_time=now,
                                       token_amount=token_amount,
                                       usd_value=usd_value,
                                       planet_id=request.planet_id,
                                       was_recovered=False)

        await self.energy_repository_port.create_energy_deposit(energy_deposit)
        planet.energy_deposits.append(energy_deposit)
        planet.resources.energy += round(usd_value, 0)
        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(energy_deposit)
