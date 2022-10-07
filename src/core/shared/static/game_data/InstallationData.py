from dataclasses import dataclass

from .Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
    BuildableItemRequirement,
)
from .GameData import GameData


@dataclass
class InstallationData(GameData):
    """
    Data class representing in game items
    Production is expressed per minute
    """

    TYPE = "installations"

    INVESTIGATION_LABORATORY = "investigationLaboratory"
    HANGAR = "hangar"

    TYPES = [
        INVESTIGATION_LABORATORY,
        HANGAR,
    ]

    __ITEMS = {
        INVESTIGATION_LABORATORY: BuildableItemBaseType(
            "Investigation Laboratory",
            INVESTIGATION_LABORATORY,
            TYPE,
            None,
            "Investigation laboratory is needed in order to conduct new research",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 150, 50, 600, 0, 0, 0, 1200, 0, 0, 15, [], 0
                ),
                2: BuildableItemLevelInfo(
                    2, 200, 100, 800, 0, 0, 0, 1500, 0, 0, 25, [], 0
                ),
                3: BuildableItemLevelInfo(
                    3, 250, 200, 1000, 0, 0, 0, 1800, 0, 0, 35, [], 0
                ),
                4: BuildableItemLevelInfo(
                    4, 350, 300, 1200, 0, 0, 0, 2000, 0, 0, 45, [], 0
                ),
                5: BuildableItemLevelInfo(
                    5, 350, 400, 1400, 0, 0, 0, 2300, 0, 0, 55, [], 0
                ),
                6: BuildableItemLevelInfo(
                    6, 450, 500, 1600, 0, 0, 0, 2600, 0, 0, 65, [], 0
                ),
                7: BuildableItemLevelInfo(
                    7, 500, 800, 1800, 0, 0, 0, 2800, 0, 0, 85, [], 0
                ),
                8: BuildableItemLevelInfo(
                    8, 650, 900, 2000, 0, 0, 0, 3000, 0, 0, 150, [], 0
                ),
                9: BuildableItemLevelInfo(
                    9, 750, 1000, 3000, 0, 0, 0, 3400, 0, 0, 200, [], 0
                ),
                10: BuildableItemLevelInfo(
                    10, 900, 1100, 4000, 0, 0, 0, 4000, 0, 0, 300, [], 0
                ),
            },
        ),
        HANGAR: BuildableItemBaseType(
            "Hangar",
            HANGAR,
            TYPE,
            None,
            "Hangar is needed in order to build and store spaceships and defense",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 100, 100, 50, 0, 0, 0, 1400, 0, 0, 10, [], 0
                ),
                2: BuildableItemLevelInfo(
                    2, 150, 200, 60, 0, 0, 0, 1700, 0, 0, 20, [], 0
                ),
                3: BuildableItemLevelInfo(
                    3, 200, 300, 70, 0, 0, 0, 2000, 0, 0, 30, [], 0
                ),
                4: BuildableItemLevelInfo(
                    4,
                    250,
                    400,
                    100,
                    0,
                    0,
                    0,
                    2300,
                    0,
                    0,
                    40,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 4)],
                    0,
                ),
                5: BuildableItemLevelInfo(
                    5,
                    300,
                    500,
                    120,
                    0,
                    0,
                    0,
                    2600,
                    0,
                    0,
                    50,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 5)],
                    0,
                ),
                6: BuildableItemLevelInfo(
                    6,
                    350,
                    600,
                    140,
                    0,
                    0,
                    0,
                    2800,
                    0,
                    0,
                    60,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 6)],
                    0,
                ),
                7: BuildableItemLevelInfo(
                    7,
                    400,
                    700,
                    150,
                    0,
                    0,
                    0,
                    3200,
                    0,
                    0,
                    80,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 7)],
                    0,
                ),
                8: BuildableItemLevelInfo(
                    8,
                    450,
                    800,
                    200,
                    0,
                    0,
                    0,
                    3600,
                    0,
                    0,
                    100,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 8)],
                    0,
                ),
                9: BuildableItemLevelInfo(
                    9,
                    550,
                    900,
                    250,
                    0,
                    0,
                    0,
                    4000,
                    0,
                    0,
                    150,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 9)],
                    0,
                ),
                10: BuildableItemLevelInfo(
                    10,
                    700,
                    1000,
                    350,
                    0,
                    0,
                    0,
                    4800,
                    0,
                    0,
                    250,
                    [BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 10)],
                    0,
                ),
            },
        ),
    }

    @staticmethod
    def valid_type(label: str) -> bool:
        return label in InstallationData.TYPES

    @staticmethod
    def get_type() -> str:
        return InstallationData.TYPE

    @staticmethod
    def get_item(key: str) -> BuildableItemBaseType:
        if key not in InstallationData.TYPES:
            raise ValueError(
                f"{key} not in {InstallationData.TYPES} for {InstallationData.TYPE}"
            )

        return InstallationData.__ITEMS[key]
