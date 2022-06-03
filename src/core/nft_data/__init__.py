from dataclasses import dataclass
from pydantic import BaseModel

from core.shared.ports import PlanetRepositoryPort, ChainServicePort


class FreePlanetRequest(BaseModel):
    name: str


@dataclass
class NftData:
    api_endpoint: str
    planet_images_base_url: str
    testnet_ticket_images_base_url: str
    planet_repository_port: PlanetRepositoryPort
    chain_service_port: ChainServicePort
    chain_service_mainnet_port: ChainServicePort

    async def planet_nft_view(self, planet_id: str):
        print("ASD")
        pass

    async def testnet_ticket_nft(self):
        pass
