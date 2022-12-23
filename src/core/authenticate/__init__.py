from dataclasses import dataclass
import logging
import time

from eth_account.messages import encode_defunct
import jwt
from pydantic import BaseModel
from web3.auto import w3

from core.planet_email import PlanetEmail, PlanetSendEmailRequest
from core.shared.models import AppBaseException, User
from core.shared.ports import ChainServicePort, ResponsePort, UserRepositoryPort, PlanetRepositoryPort
from datetime import datetime
import json

from core.shared.static.game_data.DailyLoginRewardsData import DailyLoginRewardsData


class AuthenticationDetailsRequest(BaseModel):
    address: str
    signature: str


class JwtResponse(BaseModel):
    jwt: str


class NotWhiteListedException(AppBaseException):
    msg = "Not whitelisted"
    code = 401


@dataclass
class Authenticate:
    secret_key: str
    env: str
    user_repository_port: UserRepositoryPort
    chain_service: ChainServicePort
    planet_repository_port: PlanetRepositoryPort
    email_use_case: PlanetEmail
    response_port: ResponsePort

    async def __ticket_testnet_access(self, address: str):

        if self.env in ["mainnet"]:
            whitelisted_addr = [
                "0x8eA8ba4386FB9f1569eAe8b863f6f8f99687F163",
                "0x4A67f4cACb27f57467F428EE469bfc69B58b9bCf",
                "0x1C6ffD4d136F3da9B03304dE4E457789C013f210",
                "0x0DF2D117fFe0A7C3A8Ec9970a9236eA7B8503E85",
                "0x74D93D4A5F7F3b784D856876075B5343Ba9d2cc2",
                "0xc6411B7F27Bf98Bdee0100E48427ee2e91aE50Fc",
                "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
                "0x03545A3A834A0837aac22eDAE92c0Ed1435F144b",
                "0x92A8269f914930F1E1C228c64CB8371F08982c5d",
            ]

            if address not in whitelisted_addr:
                return False

            return True

        has_access = False
        ticket_amount = await self.chain_service.spaceriders_ticket_nft_call(
            "balanceOf", address
        )
        if ticket_amount <= 0:
            return False
        elif ticket_amount > 0:
            nft_info = []
            for i in range(ticket_amount):
                token_id = await self.chain_service.spaceriders_ticket_nft_call(
                    "walletTokenIds", address, i
                )
                nft_info.append(
                    await self.chain_service.spaceriders_ticket_nft_call(
                        "byTokenIdIdData", token_id
                    )
                )

            for ticket in nft_info:
                owner = ticket[1]
                exists = ticket[2]
                life_time = ticket[3]
                expiry_date = ticket[5]
                burned = ticket[7]

                if owner != address or not exists or burned:
                    continue

                if life_time or time.time() < expiry_date:
                    has_access = True
                    break

        return has_access

    async def __check_daily_login_reward(self, user: User):


        async def give_reward_planet(planets, day):
            email_data = {
                "day": day,
            }
            for planet in planets:
                metal = DailyLoginRewardsData.get_rewards_by_day(day)["metal"]
                petrol = DailyLoginRewardsData.get_rewards_by_day(day)["petrol"]
                crystal = DailyLoginRewardsData.get_rewards_by_day(day)["crystal"]
                energy = DailyLoginRewardsData.get_rewards_by_day(day)["energy"]

                planet.resources.metal += metal
                planet.resources.petrol += petrol
                planet.resources.crystal += crystal
                planet.resources.energy += energy
                await self.planet_repository_port.update(planet)

                email_data["metal"] = metal
                email_data["crystal"] = crystal
                email_data["petrol"] = petrol
                email_data["energy"] = energy

                email: PlanetSendEmailRequest = PlanetSendEmailRequest(
                    planet_id_receiver=str(planet.id),
                    title="Daily login reward",
                    sub_title="Free resources just for logging in!",
                    template="daily_login_reward",
                    topic="",
                    body=json.dumps(email_data),
                )
                await self.email_use_case.create(email)

        now = int(datetime.timestamp(datetime.now()))

        if not user.daily_login_next_reward_timer:
            user.daily_login_streak = 1
            user.daily_login_next_reward_timer = now + 86400  # +24h
            await give_reward_planet(user.planets, 1)

        elif user.daily_login_next_reward_timer <= user.last_login <= (user.daily_login_next_reward_timer + 86400):  # +24h
            user.daily_login_next_reward_timer = now + 86400  # +24h
            user.daily_login_streak += 1
            await give_reward_planet(user.planets, user.daily_login_streak)

        elif now >= user.last_login + 86400:  # +24h
            user.daily_login_streak = 1
            user.daily_login_next_reward_timer = now + 86400  # +24h
            await give_reward_planet(user.planets, 1)

        return user

    async def __call__(self, auth_details_request: AuthenticationDetailsRequest) -> str:
        message = encode_defunct(text="its me:" + auth_details_request.address)
        recovered_address = w3.eth.account.recover_message(
            message, signature=auth_details_request.signature
        )

        # if not await self.__ticket_testnet_access(recovered_address):
        #     raise NotWhiteListedException()

        if auth_details_request.address == recovered_address:
            user = await self.user_repository_port.find_user(recovered_address)

            new_user = False
            if user is None:
                new_user = True
                user = await self.user_repository_port.create_user(recovered_address)

            payload = {
                "user_id": user.wallet,
                "exp": datetime.timestamp(datetime.now()) + 21600,
                "token_type": "access",
            }

            # Check daily rewards, important to do it before updating `user.last_login` timestamp
            if not new_user and len(user.planets) > 0:
                user = await self.__check_daily_login_reward(user)

            user.last_login = int(datetime.timestamp(datetime.now()))
            await self.user_repository_port.update(user)

            logging.info(f"Wallet {user.wallet} authenticated")
            jwt_str = jwt.encode(payload, self.secret_key, algorithm="HS256")
            return await self.response_port.publish_response(JwtResponse(jwt=jwt_str))
