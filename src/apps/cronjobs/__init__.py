# https://schedule.readthedocs.io/en/stable/parallel-execution.html
# stuff like cronjobs like planet imports, building queues etc t oremove some burden from api
import asyncio

import aioschedule as schedule
from beanie import init_beanie
from decouple import config
import motor.motor_asyncio

from adapters.shared.beani_repository_adapter import (
    PlanetDocument,
    UserDocument,
)
from adapters.shared.beanie_models_adapter import BKMTransactionDocument, EmailDocument
import apps.cronjobs.dependencies as dependencies
import apps.cronjobs.settings as settings
from controllers.cronjobs import CronjobController
from core.planet_bkm import RecoverBKMTransactionRequest
from core.shared.models import Planet


async def asteroid(controller: CronjobController):
    await dependencies.logging_adapter.info("Running task: asteroid")

    all_claimed: list[
        Planet
    ] = await dependencies.planet_repository.all_claimed_planets()
    for planet in all_claimed:
        await controller.asteroid_pve(str(planet.id))


async def space_pirate(controller: CronjobController):
    await dependencies.logging_adapter.info("Running task: space_pirate")

    all_claimed: list[
        Planet
    ] = await dependencies.planet_repository.all_claimed_planets()
    for planet in all_claimed:
        await controller.space_pirate_pve(str(planet.id))


async def smart_contract_recover_by_user_cronjob(controller: CronjobController):
    await dependencies.logging_adapter.info(
        "Running task: smart_contract_recover_by_user_cronjob"
    )

    all_users = await dependencies.user_repository.all()
    for user in all_users:
        await controller.recover_planets(user.wallet)


async def smart_contract_recover_by_planet_cronjob(controller: CronjobController):
    await dependencies.logging_adapter.info(
        "Running task: smart_contract_recover_by_planet_cronjob"
    )
    all_claimed: list[
        Planet
    ] = await dependencies.planet_repository.all_claimed_planets()
    for planet in all_claimed:
        bkm_request = RecoverBKMTransactionRequest(planet_id=str(planet.id))

        await controller.recover_bkm_deposits(bkm_request)
        await controller.recover_staking(str(planet.id))


# @TODO: add emails when something got imported
async def main():
    await dependencies.logging_adapter.info("Cronjobs started")
    client = motor.motor_asyncio.AsyncIOMotorClient(
        config("DB_URL"),
    )
    db = client[config("DB_NAME")]

    await init_beanie(
        database=db,
        document_models=[
            UserDocument,
            PlanetDocument,
            EmailDocument,
            BKMTransactionDocument,
        ],
    )

    controller = await dependencies.cronjob_controller()

    # If this is not here in main function it won't work (also below model initialization)
    schedule.every(1200).seconds.do(
        smart_contract_recover_by_planet_cronjob, controller
    )
    #schedule.every(1200).seconds.do(smart_contract_recover_by_user_cronjob, controller)
    schedule.every(50).hours.do(asteroid, controller)
    schedule.every(20).hours.do(space_pirate, controller)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())
