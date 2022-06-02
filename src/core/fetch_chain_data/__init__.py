from dataclasses import dataclass
from pydantic import BaseModel
from core.shared.ports import TokenPricePort, ChainServicePort, ResponsePort


class FetchChainDataResponse(BaseModel):
    rpc: str
    chain_id: str
    chain_name: str
    token_contract: str
    game_contract: str
    nft_contract: str
    router_contract: str
    pair_contract: str
    busd_contract: str


class FetchChainTokenPriceResponse(BaseModel):
    spr_price_usd: str


@dataclass
class FetchChainData:
    token_price: TokenPricePort
    contract_service: ChainServicePort
    chain_id: str
    chain_name: str
    response_port: ResponsePort

    async def get_chain_data(self):
        router_address = await self.contract_service.spaceriders_token_call("dexAddresses", 0)
        pair_address = await self.contract_service.spaceriders_token_call("dexPairAddress", router_address)
        busd_address = await self.contract_service.spaceriders_token_call("busdAddress")

        rpc_url = await self.contract_service.get_rpc_url()

        token_contract = await self.contract_service.get_contract_address(ChainServicePort.SPACERIDERS_TOKEN_CONTRACT)
        game_contract = await self.contract_service.get_contract_address(ChainServicePort.SPACERIDERS_GAME_CONTRACT)
        nft_contract = await self.contract_service.get_contract_address(ChainServicePort.SPACERIDERS_NFT_CONTRACT)

        response = FetchChainDataResponse(
            rpc=rpc_url,
            chain_id=self.chain_id,
            chain_name=self.chain_name,
            token_contract=token_contract,
            game_contract=game_contract,
            nft_contract=nft_contract,
            router_contract=router_address,
            pair_contract=pair_address,
            busd_contract=busd_address,
        )

        return await self.response_port.publish_response(response)

    async def get_chain_token_price(self):
        token_price: float = await self.token_price.fetch_token_price_usd()
        token_price = f"{token_price:.4f}"
        return await self.response_port.publish_response(FetchChainTokenPriceResponse(spr_price_usd=token_price))
