from dataclasses import dataclass

from pydantic import BaseModel

from core.shared.models import AppBaseException
from core.shared.ports import ResponsePort, VoucherRepositoryPort, PlanetRepositoryPort


class RedeemVoucherRequest(BaseModel):
    voucher_id: str


class VoucherNotFoundException(AppBaseException):
    msg = "Provided voucher id not found..."


class VoucherAlreadyRedeemedException(AppBaseException):
    msg = "Voucher already redeemed..."


class RedeemVoucherResponse(BaseModel):
    redeemed: bool = None


@dataclass
class RedeemVoucher:
    voucher_repository: VoucherRepositoryPort
    planet_repository_port: PlanetRepositoryPort
    response_port: ResponsePort

    async def redeem_voucher(self, user_id: str, request: RedeemVoucherRequest):

        voucher = await self.voucher_repository.find_voucher(request.voucher_id)

        if not voucher:
            raise VoucherNotFoundException()

        if voucher.redeemed:
            raise VoucherAlreadyRedeemedException()

        all_planets = await self.planet_repository_port.all_user_planets(user_id)
        for planet in all_planets:
            planet.resources.metal += voucher.amount_metal
            planet.resources.crystal += voucher.amount_crystal
            planet.resources.petrol += voucher.amount_petrol
            planet.resources.energy += voucher.amount_energy
            voucher.redeemed = True
            await self.voucher_repository.update(voucher)
            await self.planet_repository_port.update(planet)

        return RedeemVoucherResponse(redeemed=True)
