from dataclasses import dataclass


@dataclass
class StakingBenefits:
    usd_cost: float
    trading_fee_discount: float  # trading fee discount
    tokens_time_locked: int  # seconds
    experience_boost: int  # percentage of xp boost 0-100


class StakingData:
    """ Data representing TIER costs """

    TIER_0: str = "TIER_0"
    TIER_1: str = "TIER_1"
    TIER_2: str = "TIER_2"

    TIERS: list[str] = [
        TIER_0,
        TIER_1,
        TIER_2
    ]

    TIER_NAMES: dict[str, str] = {
        TIER_0: "Tier 0",
        TIER_1: "Tier 1",
        TIER_2: "Tier 2",
    }

    DATA: dict[str, StakingBenefits] = {
        TIER_0: StakingBenefits(0, 0, 0, 0),
        TIER_1: StakingBenefits(50, 10, 60, 2),
        TIER_2: StakingBenefits(50, 10, 172800, 2),
    }
