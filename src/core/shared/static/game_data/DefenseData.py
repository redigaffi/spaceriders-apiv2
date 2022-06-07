from dataclasses import dataclass

from .InstallationData import InstallationData as ID
from .ResearchData import ResearchData as RD
from .Common import BuildableItemBaseType, BuildableItemRequirement, BuildableItemLevelInfo
from .GameData import GameData


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
        MISSILE_LAUNCHER: BuildableItemBaseType("Missile Launcher", MISSILE_LAUNCHER, TYPE, None,
                                                "Missile launcher is a cheap yet effective defense mechanism",
                                                {
                                                    0: BuildableItemLevelInfo(0, 100, 50, 40, 0, 0, 0, 50, 50,
                                                                              40, 10,
                                                                              [BuildableItemRequirement(ID.TYPE,
                                                                                                        ID.HANGAR, 2)],
                                                                              0),
                                                }
                                                ),
        LASER_LAUNCHER: BuildableItemBaseType("Laser Launcher", LASER_LAUNCHER, TYPE, None,
                                              "The Laser Launcher is a more powerful defense when compared to the simple missile launcher",
                                              {
                                                  0: BuildableItemLevelInfo(0, 200, 150, 80, 0, 0, 0, 50, 50,
                                                                            150, 10,
                                                                            [BuildableItemRequirement(ID.TYPE,
                                                                                                      ID.HANGAR, 2),
                                                                             BuildableItemRequirement(RD.TYPE,
                                                                                                      RD.LASER_RESEARCH,
                                                                                                      2)
                                                                             ],
                                                                            0),
                                              }
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
