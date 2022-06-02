# https://schedule.readthedocs.io/en/stable/parallel-execution.html
# stuff like cronjobs like planet imports, building queues etc t oremove some burden from api
from beanie import init_beanie
from decouple import config
import motor.motor_asyncio
import asyncio
import aioschedule as schedule
import dependencies
from src.adapters.shared.beani_repository_adapter import UserDocument, PlanetDocument, EnergyDepositDocument
from src.controllers.cronjobs import CronjobController
from src.core.planet_energy import PlanetEnergyRecoverEnergyDepositsRequest
from src.core.shared.models import Planet


async def energy_deposit_recover_cronjob(controller: CronjobController):
    all_claimed: list[Planet] = await dependencies.planet_repository.all_claimed_planets()
    for planet in all_claimed:
        request = PlanetEnergyRecoverEnergyDepositsRequest(planet_id=str(planet.id))
        await controller.recover_deposits(request)



async def main():
    await dependencies.logging_adapter.info("App started")
    client = motor.motor_asyncio.AsyncIOMotorClient(config("DB_URL"), )
    db = client[config('DB_NAME')]

    await init_beanie(database=db, document_models=[UserDocument, EnergyDepositDocument, PlanetDocument])

    controller = await dependencies.cronjob_controller()
    # If this is not here in main function it wont work
    schedule.every(3).seconds.do(energy_deposit_recover_cronjob, controller)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())

