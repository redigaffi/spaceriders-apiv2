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
                    level=1, experience=225, health=1000, time=600, cost_metal=1000, cost_crystal=2000,
                    cost_petrol=0,
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
