from time import timezone

from web3.auto import w3
from eth_account.messages import encode_defunct
from dataclasses import dataclass

from core.shared.models import AppBaseException
from core.shared.ports import UserRepositoryPort, ResponsePort, ChainServicePort
from pydantic import BaseModel
import jwt
from datetime import datetime, timezone
import time
import logging


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
    response_port: ResponsePort

    async def __ticket_testnet_access(self, address: str):

        if self.env in ['mainnet']:
            whitelisted_addr = [
                "0x8eA8ba4386FB9f1569eAe8b863f6f8f99687F163",
                "0x4A67f4cACb27f57467F428EE469bfc69B58b9bCf",
                "0x1C6ffD4d136F3da9B03304dE4E457789C013f210",
                "0x0DF2D117fFe0A7C3A8Ec9970a9236eA7B8503E85",
                "0x74D93D4A5F7F3b784D856876075B5343Ba9d2cc2",
                "0xc6411B7F27Bf98Bdee0100E48427ee2e91aE50Fc",
                "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
                "0x03545A3A834A0837aac22eDAE92c0Ed1435F144b",
                "0x92A8269f914930F1E1C228c64CB8371F08982c5d"
            ]

            if address not in whitelisted_addr:
                return False

            return True

        has_access = False
        ticket_amount = await self.chain_service.spaceriders_ticket_nft_call("balanceOf", address)
        if ticket_amount <= 0:
            return False
        elif ticket_amount > 0:
            nft_info = []
            for i in range(ticket_amount):
                token_id = await self.chain_service.spaceriders_ticket_nft_call("walletTokenIds", address, i)
                nft_info.append(
                    await self.chain_service.spaceriders_ticket_nft_call("byTokenIdIdData", token_id)
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

    async def __call__(self, auth_details_request: AuthenticationDetailsRequest) -> str:
        message = encode_defunct(text="its me:" + auth_details_request.address)
        recovered_address = w3.eth.account.recover_message(message, signature=auth_details_request.signature)

        if not await self.__ticket_testnet_access(recovered_address):
            raise NotWhiteListedException()

        if auth_details_request.address == recovered_address:
            user = await self.user_repository_port.find_user(recovered_address)

            if user is None:
                user = await self.user_repository_port.create_user(recovered_address)

            payload = {
                "user_id": user.wallet,
                "exp": datetime.timestamp(datetime.now())+43200,
                "token_type": "access",
            }

            logging.info(f"Wallet {user.wallet} authenticated")
            jwt_str = jwt.encode(payload, self.secret_key, algorithm="HS256")
            return await self.response_port.publish_response(JwtResponse(jwt=jwt_str))
