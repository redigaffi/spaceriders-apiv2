import random

from core.shared.models import ResourceExchange
from core.shared.ports import ResponsePort, ResourceExchangeRepositoryPort
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ResourcesExchange:
    resource_repository: ResourceExchangeRepositoryPort
    response_port: ResponsePort

    async def get_current_price(self) -> ResourceExchange:
        return await self.resource_repository.get_latest()

    async def new_resource_exchange_price(self):
        metal = random.uniform(0.001, 0.01)
        crystal = random.uniform(0.001, 0.01)
        petrol = random.uniform(0.001, 0.01)

        now = datetime.timestamp(datetime.now())
        resource_exchange = ResourceExchange(created_time=now, metal_usd_price=metal, crystal_usd_price=crystal, petrol_usd_price=petrol)
        await self.resource_repository.create(resource_exchange)
        return await self.response_port.publish_response(resource_exchange)

