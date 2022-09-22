from core.shared.static.game_data.Common import BuildableItemLevelInfo
from core.shared.static.game_data.StakingData import StakingData as SD, StakingBenefits
import copy


def tier_benefit_service(tier_code: str, level: BuildableItemLevelInfo = None) -> BuildableItemLevelInfo:
    tier_data: StakingBenefits = SD.DATA[tier_code]
    return level
