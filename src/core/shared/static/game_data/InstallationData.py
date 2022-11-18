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
                # level=1, cost_metal=150, cost_petrol=50, cost_crystal=600, energy_usage=0, production=0, capacity=0, time=1200, health=0, attack=0, experience=15, requirements=[], has_discount=0
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=293, health=2000, time=900, cost_metal=400, cost_crystal=800, cost_petrol=400, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=414, health=2000, time=1477, cost_metal=565, cost_crystal=1130, cost_petrol=565, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=571, health=2197, time=2331, cost_metal=779, cost_crystal=1557, cost_petrol=779, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=767, health=2350, time=3531, cost_metal=1046, cost_crystal=2092, cost_petrol=1046, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=1004, health=2551, time=5126, cost_metal=1370, cost_crystal=2740, cost_petrol=1370, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=1280, health=2807, time=7115, cost_metal=1746, cost_crystal=3493, cost_petrol=1746, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=1588, health=3125, time=9426, cost_metal=2166, cost_crystal=4333, cost_petrol=2166, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=1915, health=3508, time=11890, cost_metal=2613, cost_crystal=5225, cost_petrol=2613, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=3453, health=4198, time=14946, cost_metal=3140, cost_crystal=6281, cost_petrol=3140, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=4137, health=5026, time=18719, cost_metal=3762, cost_crystal=7524, cost_petrol=3762, energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
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
