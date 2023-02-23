from dataclasses import dataclass
import datetime

from pydantic import BaseModel

from core.shared.models import AppBaseException, EnergyDeposit, ShadyActivityException
from core.shared.ports import (
    ChainServicePort,
    EnergyDepositRepositoryPort,
    LoggingPort,
    PlanetRepositoryPort,
    ResponsePort,
    TokenPricePort,
    CacheServicePort,
)


class PlanetEnergyRecoverEnergyDepositsRequest(BaseModel):
    planet_id: str


class EnergyDepositRequest(BaseModel):
    planet_id: str
    amount: float = None


class NotEnoughBKM(AppBaseException):
    msg = "Not enough $BKM in wallet"


class EnergyDepositAlreadyExistsException(AppBaseException):
    msg = "Energy deposit with given id already exists"


@dataclass
class PlanetEnergy:
    token_price: TokenPricePort
    energy_repository_port: EnergyDepositRepositoryPort
    planet_repository_port: PlanetRepositoryPort
    logging_port: LoggingPort
    contract_port: CacheServicePort
    response_port: ResponsePort

    async def create_deposit(
        self, user: str, request: EnergyDepositRequest
    ) -> EnergyDeposit:
        planet = await self.planet_repository_port.get_my_planet(
            user, request.planet_id
        )

        amount = request.amount - (request.amount * 0.1)  # fee
        energy_amount = amount * 200

        if planet.resources.bkm <= amount:
            raise NotEnoughBKM

        energy_deposit = EnergyDeposit(
            created_time=datetime.datetime.timestamp(datetime.datetime.now()),
            energy_amount=energy_amount,
            planet_id=request.planet_id,
        )

        energy_deposit = await self.energy_repository_port.create_energy_deposit(
            energy_deposit
        )

        planet.resources.bkm -= request.amount
        planet.energy_deposits.append(energy_deposit)
        planet.resources.energy += round(energy_amount, 0)
        await self.planet_repository_port.update(planet)
        return await self.response_port.publish_response(energy_deposit)
