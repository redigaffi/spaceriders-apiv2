from dataclasses import dataclass


class CommonKeys:
    # Generic
    SUBTYPE = "subtype"
    NAME = "name"
    LABEL = "label"
    TYPE = "type"
    DESCRIPTION = "description"
    ATTACK = "attack"

    REWARDS = "rewards"
    PURCHASING_POWER = "purchasing_power"

    METAL = "metal"
    PETROL = "petrol"
    CRYSTAL = "crystal"
    ENERGY = "energy"

    # For upgrades data
    PRODUCTION = "production"
    CAPACITY = "capacity"

    COST_METAL = "cost_metal"
    COST_PETROL = "cost_petrol"
    COST_CRYSTAL = "cost_crystal"
    TIME = "time"
    LEVEL = "level"
    REQUIREMENTS = "requirements"
    ENERGY_USAGE = "energy_usage"
    HEALTH = "health"
    EXPERIENCE = "experience"
    NEW_RESERVE_FOUND_PERCENTAGE = "new_reserve_found_percentage"

    ENERGY_DEPOSIT_MAX_ONCE = "energy_deposit_max_once"
    RESOURCE_EXTRACTION_MULTIPLIER = "resource_extraction_multiplier"
    INITIAL_RESERVE = "initial_resources"


@dataclass
class BuildableItemRequirement:
    type: str
    asset: str
    level: int


@dataclass
class BuildableItemLevelInfo:
    level: int = 0
    cost_metal: float = 0
    cost_petrol: float = 0
    cost_crystal: float = 0
    energy_usage: float = 0  # Minute
    production: float = 0
    capacity: float = 0
    time: float = 0
    health: float = 0
    attack: float = 0
    experience: float = 0
    requirements: list[BuildableItemRequirement] = None
    new_reserve_found_percentage: float = 0
    has_discount: bool = False


@dataclass
class BuildableItemBaseType:
    """
    Represents example metal mine with its upgrade/build info
    """

    name: str = None  # Nice readable name
    label: str = None  # Code name
    type: str = None  # subtype
    category: str = None
    description: str = None

    builds: dict[int, BuildableItemLevelInfo] = None

    def get_level_info(self, level: int = 0) -> BuildableItemLevelInfo:

        try:
            level_info = self.builds[level]
        except:
            level_info = self.builds[0]

        return level_info
