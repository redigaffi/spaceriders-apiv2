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
                    level=0, experience=75, health=500, time=300, cost_metal=1500, cost_crystal=0, cost_petrol=0, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 3)
                    ], has_discount=0
                ),
            },
        ),
        LASER_LAUNCHER: BuildableItemBaseType(
            "Laser Turret",
            LASER_LAUNCHER,
            TYPE,
            None,
            "The Laser Turret is a more powerful defense when compared to the simple missile launcher",
            {
                0: BuildableItemLevelInfo(
                    level=0, experience=113, health=1000, time=500, cost_metal=500, cost_crystal=1000, cost_petrol=0, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(RD.TYPE, RD.LASER_RESEARCH, 5)
                    ], has_discount=0
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
