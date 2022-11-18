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
                    level=1, experience=235, health=3000, time=600, cost_metal=800, cost_crystal=400, cost_petrol=300, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=320, health=3064, time=938, cost_metal=1090, cost_crystal=545, cost_petrol=409, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=293, health=2000, time=900, cost_metal=400, cost_crystal=800, cost_petrol=400, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 2)], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=562, health=3262, time=2094, cost_metal=1915, cost_crystal=957, cost_petrol=718, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 2)], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=725, health=3407, time=2985, cost_metal=2469, cost_crystal=1234, cost_petrol=926, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 3)], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=917, health=3590, time=4117, cost_metal=3123, cost_crystal=1562, cost_petrol=1171, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 3)], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=1138, health=3818, time=5488, cost_metal=3875, cost_crystal=1938, cost_petrol=1453, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 3)], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=1384, health=4095, time=7064, cost_metal=4714, cost_crystal=2357, cost_petrol=1768, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 4)], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=1650, health=4425, time=8767, cost_metal=5621, cost_crystal=2810, cost_petrol=2108, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 4)], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=1928, health=4810, time=10477, cost_metal=6565, cost_crystal=3283, cost_petrol=2462, energy_usage=0, production=0, capacity=0, 
                    attack=0, requirements=[BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 4)], has_discount=0
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
