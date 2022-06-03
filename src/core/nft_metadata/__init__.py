from dataclasses import dataclass

from ethpm.tools.builder import description
from pydantic import BaseModel
from core.shared.ports import PlanetRepositoryPort, ChainServicePort, ResponsePort


class FreePlanetRequest(BaseModel):
    name: str


class OpenseaAttributeStandardResponse(BaseModel):
    display_type: str = None
    trait_type: str = None
    value: str = None


class OpenseaMetadataNftResponse(BaseModel):
    description: str
    external_url: str
    image: str
    name: str
    attributes: list[OpenseaAttributeStandardResponse]
    animation_url: str = None
    seller_fee_basis_points: str = None
    fee_recipient: str = None


@dataclass
class NftData:
    api_endpoint: str
    planet_images_base_url: str
    testnet_ticket_images_base_url: str
    planet_repository_port: PlanetRepositoryPort
    chain_service_port: ChainServicePort
    response_port: ResponsePort

    async def planet_nft_view(self, planet_id: str):

        planet = await self.planet_repository_port.get(planet_id)
        attributes = [
            OpenseaAttributeStandardResponse(display_type="string", trait_type="Position", value=f"{planet.position}:{planet.solar_system}:{planet.galaxy}"),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Level", value=str(planet.level)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Experience", value=str(planet.experience)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Diameter", value=str("planet.diameter")),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Slots", value=str(planet.slots)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Slots Used", value=str(planet.slots_used)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Minimum Temperature", value=str(planet.min_temperature)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Maximum Temperature", value=str(planet.max_temperature)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Metal Reserve",
                                             value=str(planet.reserves.total_metal)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Petrol Reserve",
                                             value=str(planet.reserves.total_petrol)),
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Crystal Reserve",
                                             value=str(planet.reserves.total_crystal)),

        ]

        image_name = f"{planet.image}-{planet.rarity}.png"
        response = OpenseaMetadataNftResponse(description="Deep space is dangerous, this is your home, fight for it.",
                                              external_url=f"{self.api_endpoint}/nft/{planet_id}",
                                              image=f"{self.planet_images_base_url}/{image_name}",
                                              name=planet.name,
                                              attributes=attributes)

        return await self.response_port.publish_response(response)

    async def testnet_ticket_nft(self, token_id: int):
        ticket_info = await self.chain_service_port.spaceriders_ticket_nft_call("byTokenIdIdData", token_id)

        royalty_fee_bips = await self.chain_service_port.spaceriders_ticket_nft_call("royaltyFeeBips")
        royalty_receiver = await self.chain_service_port.spaceriders_ticket_nft_call("royaltyReceiver")

        owner = ticket_info[1]
        exists = ticket_info[2]
        life_time = ticket_info[3]
        generation = ticket_info[4]
        expiry_date = ticket_info[5]
        burned = ticket_info[7]

        life_time_str = "Yes" if life_time else "No"

        attributes = [
            OpenseaAttributeStandardResponse(display_type="number", trait_type="Generation", value=str(generation)),
            OpenseaAttributeStandardResponse(display_type="", trait_type="Lifetime Access", value=life_time_str),
        ]

        if not life_time:
            attributes.append(
                OpenseaAttributeStandardResponse(display_type="date", trait_type="Expiry date", value=str(expiry_date)),
            )

        tmp_lifet = "lifetime" if life_time else "temporary"

        anim_url = f"{self.testnet_ticket_images_base_url}/{tmp_lifet}_gen_{generation}.mp4"
        img_url = f"{self.testnet_ticket_images_base_url}/{tmp_lifet}_gen_{generation}.jpg"
        re = OpenseaMetadataNftResponse(
            image=img_url,
            description="Ticket that gives you access to https://www.spaceriders.io testnet.",
            external_url=f"{self.api_endpoint}/nft/ticket/{token_id}",
            animation_url=anim_url,
            name="SpaceRiders Alpha Access Ticket",
            attributes=attributes,
            seller_fee_basis_points=royalty_fee_bips,
            fee_recipient=royalty_receiver
        )

        return await self.response_port.publish_response(re)

