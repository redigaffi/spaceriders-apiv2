from core.shared.static.game_data.Common import BuildableItemLevelInfo
from core.shared.static.game_data.StakingData import StakingBenefits
from core.shared.static.game_data.StakingData import StakingData as SD


def tier_benefit_buildable_items(
    tier_code: str, level: BuildableItemLevelInfo = None
) -> BuildableItemLevelInfo:
    tier_data: StakingBenefits = SD.DATA[tier_code]
    return level


def tier_benefit_trading_fee(planet) -> float:

    tier_data: StakingBenefits = SD.DATA[planet.tier.tier_code]
    return tier_data.trading_fee
