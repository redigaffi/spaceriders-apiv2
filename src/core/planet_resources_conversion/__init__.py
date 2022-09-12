import datetime
import math
from typing import List

from pydantic import BaseModel
from dataclasses import dataclass

from core.resource_exchange import ResourcesExchange
from core.shared.models import TokenConversions, AppBaseException, Planet
from core.shared.ports import PlanetRepositoryPort, ResponsePort, TokenConversionsRepositoryPort, ChainServicePort, \
    TokenPricePort
from core.shared.static.game_data.Common import CommonKeys
from core.shared.static.game_data.PlanetData import PlanetData


class PreviewConversionResponse(BaseModel):
    planet_id: str
    metal_cost: float
    crystal_cost: float
    petrol_cost: float
    rarity_multiplier: dict
    level_bonus_multiplier: float
    fee: float


class PendingConversionsResponse(BaseModel):
    id: str
    completed: bool
    metal: float
    petrol: float
    crystal: float
    token: float
    date: float
    action: str


class ResourceConvertRequest(BaseModel):
    planet_id: str
    metal: float
    petrol: float
    crystal: float


class ResourceConvertResponse(BaseModel):
    id: str
    tokens: str
    forAddress: str
    v: int
    r: str
    s: str


class ConfirmConversionRequest(BaseModel):
    planet_id: str
    token_conversion_id: str


class RetryConversionRequest(ConfirmConversionRequest):
    pass


class NotEnoughResourcesException(AppBaseException):
    msg = "Not holding enough resources"


class TokenConversionNotFoundException(AppBaseException):
    msg = "Token conversion not found"


class TokenConversionConfirmWentWrong(AppBaseException):
    msg = "Something went wrong while confirming the token conversion..."


class ConversionAlreadyCompletedException(AppBaseException):
    msg = "Conversion is already completed"


@dataclass
class PlanetResourcesConversion:
    planet_repository_port: PlanetRepositoryPort
    token_conversion_repository_port: TokenConversionsRepositoryPort
    resource_exchange: ResourcesExchange
    chain_service: ChainServicePort
    token_price_port: TokenPricePort
    response_port: ResponsePort

    def __level_bonus_multiplier(self, planet: Planet):
        return planet.level / 100

    def __calculate_fee(self, latest_conversion: TokenConversions):

        day_fee = {
            0: 90,
            1: 80,
            2: 70,
            3: 60,
            4: 50,
            5: 55,
            6: 47,
            7: 45,
            8: 40,
            9: 35,
            10: 30,
            11: 25,
            12: 12,
            13: 10,
            14: 0,
        }

        # set claim fee to 0
        days_passed = 14

        if latest_conversion:
            total_days_passed = (datetime.datetime.timestamp(
                datetime.datetime.now()) - latest_conversion.created_time) / 86400  # 1 day in seconds
            total_days_passed = round(total_days_passed)
            days_passed = total_days_passed

            if total_days_passed >= 15:
                halfs_passed = math.trunc(total_days_passed / 15)
                days_passed = total_days_passed - (15 * halfs_passed)

        return day_fee[days_passed]

    async def pending_conversions(self, planet_id: str, user: str) -> List[PendingConversionsResponse]:
        planet = await self.planet_repository_port.get_my_planet(user, planet_id, True)

        re = []

        for conversion in planet.resource_conversions:
            if conversion.completed:
                continue

            conversion_data = await self.chain_service.spaceriders_game_call("conversions", str(conversion.id))
            exists = bool(conversion_data[3])

            action = "CONFIRM_API"
            if not exists:
                action = "CALL_SMART_CONTRACT"

            tmp = PendingConversionsResponse(
                id=str(conversion.id),
                completed=conversion.completed,
                metal=conversion.metal,
                petrol=conversion.petrol,
                crystal=conversion.crystal,
                token=conversion.token,
                date=conversion.created_time,
                action=action
            )
            re.append(tmp)

        return await self.response_port.publish_response(re)

    async def preview_conversion(self, planet_id: str, user: str):
        planet = await self.planet_repository_port.get_my_planet(user, planet_id)

        resource_multiplier_info = PlanetData.DATA[planet.rarity][CommonKeys.RESOURCE_EXTRACTION_MULTIPLIER]
        resource_price = await self.resource_exchange.get_current_price()

        last_conversion = await self.token_conversion_repository_port.get_latest()
        reduce_fee = self.__calculate_fee(last_conversion)

        re = PreviewConversionResponse(
            planet_id=str(planet.id),
            metal_cost=resource_price.metal_usd_price,
            crystal_cost=resource_price.crystal_usd_price,
            petrol_cost=resource_price.petrol_usd_price,
            rarity_multiplier=resource_multiplier_info,
            level_bonus_multiplier=self.__level_bonus_multiplier(planet),
            fee=reduce_fee
        )

        return await self.response_port.publish_response(re)

    async def convert_conversion(self, request: ResourceConvertRequest, user: str):
        planet = await self.planet_repository_port.get_my_planet(user, request.planet_id)
        last_conversion = await self.token_conversion_repository_port.get_latest()

        if planet.resources.metal < request.metal or planet.resources.petrol < request.petrol or planet.resources.crystal < request.crystal:
            raise NotEnoughResourcesException()

        resource_price = await self.resource_exchange.get_current_price()

        total_metal_value = resource_price.metal_usd_price * request.metal
        total_crystal_value = resource_price.crystal_usd_price * request.crystal
        total_petrol_value = resource_price.petrol_usd_price * request.petrol

        resource_multiplier_info = PlanetData.DATA[planet.rarity][CommonKeys.RESOURCE_EXTRACTION_MULTIPLIER]
        level_bonus_multiplier = self.__level_bonus_multiplier(planet)
        token_cost_usd = await self.token_price_port.fetch_token_price_usd()

        metal_token_amount = (1 / token_cost_usd) * total_metal_value
        metal_token_amount *= resource_multiplier_info[CommonKeys.METAL] + level_bonus_multiplier

        crystal_token_amount = (1 / token_cost_usd) * total_crystal_value
        crystal_token_amount *= resource_multiplier_info[CommonKeys.CRYSTAL] + level_bonus_multiplier

        petrol_token_amount = (1 / token_cost_usd) * total_petrol_value
        petrol_token_amount *= resource_multiplier_info[CommonKeys.PETROL] + level_bonus_multiplier

        token_amount = metal_token_amount + crystal_token_amount + petrol_token_amount
        reduce_fee = 100 - self.__calculate_fee(last_conversion)
        token_amount = token_amount * (reduce_fee / 100)

        now = datetime.datetime.timestamp(datetime.datetime.now())
        token_conversion = TokenConversions(
            completed=False,
            created_time=now,
            metal=request.metal,
            petrol=request.petrol,
            crystal=request.crystal,
            token=token_amount,
        )

        planet.resources.metal -= request.metal
        planet.resources.crystal -= request.crystal
        planet.resources.petrol -= request.petrol

        token_conversion = await self.token_conversion_repository_port.create(token_conversion)

        planet.resource_conversions.append(token_conversion)
        planet = await self.planet_repository_port.update(planet)

        token_wei_amount = await self.chain_service.to_wei(token_conversion.token)

        signed_msg = await self.chain_service.sign_message(
            ['string', 'uint256', 'address'],
            [str(token_conversion.id), token_wei_amount, user]
        )

        re = ResourceConvertResponse(
            id=str(token_conversion.id),
            tokens=str(token_wei_amount),
            forAddress=user,
            v=signed_msg['v'],
            r=signed_msg['r'],
            s=signed_msg['s'],
        )

        return await self.response_port.publish_response(re)

    async def retry_conversion(self, request: RetryConversionRequest, user: str) -> ResourceConvertResponse:
        planet = await self.planet_repository_port.get_my_planet(user, request.planet_id)
        conversion = await self.token_conversion_repository_port.get(request.token_conversion_id)

        if conversion.completed:
            raise ConversionAlreadyCompletedException()

        conversion_data = await self.chain_service.spaceriders_game_call("conversions", conversion.id)
        exists = bool(conversion_data[3])

        if exists:
            raise ConversionAlreadyCompletedException()

        token_wei_amount = await self.chain_service.to_wei(conversion.token)

        signed_msg = await self.chain_service.sign_message(
            ['string', 'uint256', 'address'],
            [str(conversion.id), token_wei_amount, user]
        )

        re = ResourceConvertResponse(
            id=str(conversion.id),
            tokens=str(token_wei_amount),
            forAddress=user,
            v=signed_msg['v'],
            r=signed_msg['r'],
            s=signed_msg['s'],
        )
        return await self.response_port.publish_response(re)

    async def confirm_conversion(self, request: ConfirmConversionRequest, user: str):
        planet = await self.planet_repository_port.get_my_planet(user, request.planet_id)
        conversion = await self.token_conversion_repository_port.get(request.token_conversion_id)

        if conversion is None:
            raise TokenConversionNotFoundException()

        conversion_data = await self.chain_service.spaceriders_game_call("conversions", request.token_conversion_id)

        address = str(conversion_data[1])
        exists = bool(conversion_data[3])

        if address.lower() != user.lower() or not exists:
            raise TokenConversionConfirmWentWrong()

        conversion.completed = True
        await self.token_conversion_repository_port.update(conversion)

        return await self.response_port.publish_response({})
