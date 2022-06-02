from src.core.shared.models import Planet, BuildableItem
from src.core.shared.static.game_data.StakingData import StakingData


def is_queue_full(planet: Planet) -> bool:

    queue = planet.building_queue()

    tier_code = planet.tier.tier_code
    max_queue = StakingData.DATA[tier_code].max_queue
    return len(queue) >= max_queue


