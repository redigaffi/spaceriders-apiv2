from core.shared.models import Planet, BuildableItem
from core.shared.static.game_data.StakingData import StakingData


def is_queue_full(planet: Planet) -> bool:
    # tier_code = planet.tier.tier_code
    # max_queue = StakingData.DATA[tier_code].max_queue
    return len(planet.building_queue()) >= 2


