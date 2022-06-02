from src.core.shared.static.game_data.Common import BuildableItemLevelInfo
from src.core.shared.static.game_data.StakingData import StakingData as SD, StakingBenefits
import copy


def tier_benefit_service(tier_code: str, level: BuildableItemLevelInfo = None) -> BuildableItemLevelInfo:
    tier_data: StakingBenefits = SD.DATA[tier_code]

    current_metal_cost = level.cost_metal
    current_crystal_cost = level.cost_crystal
    current_petrol_cost = level.cost_petrol
    experience = level.experience

    cost_discount = tier_data.discount_items / 100
    time_discount = tier_data.time_discount / 100
    xp_boost = tier_data.experience_boost / 100

    metal_end_cost = current_metal_cost - (current_metal_cost * cost_discount)
    petrol_end_cost = current_petrol_cost - (current_petrol_cost * cost_discount)
    crystal_end_cost = current_crystal_cost - (current_crystal_cost * cost_discount)

    time = level.time
    time_discount = time - (time * time_discount)

    # Dont modify original
    item_copy = copy.copy(level)

    item_copy.has_discount = False
    if tier_code != SD.TIER_0:
        # @TODO: Constant
        item_copy.has_discount = True

    item_copy.cost_metal = metal_end_cost
    item_copy.cost_crystal = crystal_end_cost
    item_copy.cost_petrol = petrol_end_cost
    item_copy.time = time_discount
    item_copy.experience = round(experience + (experience * xp_boost))

    return item_copy
