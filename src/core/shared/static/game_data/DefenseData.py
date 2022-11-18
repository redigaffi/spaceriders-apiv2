from dataclasses import dataclass

from .Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
    BuildableItemRequirement,
)
from .GameData import GameData
from .InstallationData import InstallationData as ID
from .ResearchData import ResearchData as RD


@dataclass
class DefenseData(GameData):
    """
    Data class representing in game items
    Production is expressed per minute
    """

    TYPE = "defense"

    MISSILE_LAUNCHER = "missileLauncher"
    LASER_LAUNCHER = "laserLauncher"

    TYPES = [
        MISSILE_LAUNCHER,
        LASER_LAUNCHER,
    ]

    __ITEMS = {
        MISSILE_LAUNCHER: BuildableItemBaseType(
            "Missile Launcher",
            MISSILE_LAUNCHER,
            TYPE,
            None,
            "Missile launcher is a cheap yet effective defense mechanism",
            {
                0: BuildableItemLevelInfo(
                    0,
                    100,
                    50,
                    40,
                    0,
                    0,
                    0,
                    50,
                    50,
                    40,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.HANGAR, 2)],
                    0,
                ),
            },
        ),
        LASER_LAUNCHER: BuildableItemBaseType(
            "Laser Launcher",
            LASER_LAUNCHER,
            TYPE,
            None,
            "The Laser Launcher is a more powerful defense when compared to the simple missile launcher",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    lvl=1, experience=1412, health=2750, time=2000, cost_metal=2000, cost_crystal=1000, cost_petrol=2000,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    lvl=2, experience=2232, health=3196, time=3437, cost_metal=3163, cost_crystal=1582, cost_petrol=3163,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    lvl=3, experience=3402, health=3877, time=5512, cost_metal=4821, cost_crystal=2410, cost_petrol=4821,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    lvl=4, experience=4990, health=4875, time=8212, cost_metal=7071, cost_crystal=3535, cost_petrol=7071,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    lvl=5, experience=10931, health=7061, time=12175, cost_metal=10326, cost_crystal=5163, cost_petrol=10326,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    lvl=6, experience=15896, health=10240, time=17965, cost_metal=15015, cost_crystal=7508, cost_petrol=15015,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    lvl=7, experience=23014, health=14843, time=26382, cost_metal=21740, cost_crystal=10870, cost_petrol=21740,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    lvl=8, experience=33177, health=21479, time=38556, cost_metal=31340, cost_crystal=15670, cost_petrol=31340,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    lvl=9, experience=65440, health=34567, time=62051, cost_metal=46362, cost_crystal=23181, cost_petrol=46362,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    lvl=10, experience=222496, health=79066, time=122919, cost_metal=78815, cost_crystal=39408, cost_petrol=78815,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
            },
        ),
    }

    @staticmethod
    def valid_type(label: str) -> bool:
        return label in DefenseData.TYPES

    @staticmethod
    def get_type() -> str:
        return DefenseData.TYPE

    @staticmethod
    def get_item(key: str) -> BuildableItemBaseType:
        if key not in DefenseData.TYPES:
            raise ValueError(f"{key} not in {DefenseData.TYPES} for {DefenseData.TYPE}")

        return DefenseData.__ITEMS[key]
