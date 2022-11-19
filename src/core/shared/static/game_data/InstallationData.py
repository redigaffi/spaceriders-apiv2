from dataclasses import dataclass

from .Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
    BuildableItemRequirement,
)
from .ResourceData import ResourceData as RSOUD
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
                0: BuildableItemLevelInfo(
                    level=0, experience=0, health=0, time=0, cost_metal=0, cost_crystal=0, cost_petrol=0, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(RSOUD.TYPE, RSOUD.METAL_MINE, 5),
                        BuildableItemRequirement(RSOUD.TYPE, RSOUD.CRYSTAL_MINE, 5),
                        BuildableItemRequirement(RSOUD.TYPE, RSOUD.PETROL_MINE, 5)
                    ], has_discount=0
                ),
                1: BuildableItemLevelInfo(
                    level=1, experience=293, health=2000, time=900, cost_metal=400, cost_crystal=800, cost_petrol=400, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=414, health=2083, time=1477, cost_metal=565, cost_crystal=1130, cost_petrol=565, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=571, health=2197, time=2331, cost_metal=779, cost_crystal=1557, cost_petrol=779, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=767, health=2350, time=3531, cost_metal=1046, cost_crystal=2092, cost_petrol=1046, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=1004, health=2551, time=5126, cost_metal=1370, cost_crystal=2740, cost_petrol=1370, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=1280, health=2807, time=7115, cost_metal=1746, cost_crystal=3493, cost_petrol=1746, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=1588, health=3125, time=9426, cost_metal=2166, cost_crystal=4333, cost_petrol=2166, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=1915, health=3508, time=11890, cost_metal=2613, cost_crystal=5225, cost_petrol=2613, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=3453, health=4198, time=14946, cost_metal=3140, cost_crystal=6281, cost_petrol=3140, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=4137, health=5026, time=18719, cost_metal=3762, cost_crystal=7524, cost_petrol=3762, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=4939, health=6013, time=23363, cost_metal=4492, cost_crystal=8984, cost_petrol=4492, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=5877, health=7189, time=29053, cost_metal=5345, cost_crystal=10690, cost_petrol=5345, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=6969, health=8583, time=35999, cost_metal=6338, cost_crystal=12676, cost_petrol=6338, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=8236, health=10230, time=44445, cost_metal=7491, cost_crystal=14981, cost_petrol=7491, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=9700, health=12170, time=54673, cost_metal=8822, cost_crystal=17645, cost_petrol=8822, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=11385, health=14447, time=67011, cost_metal=10355, cost_crystal=20710, cost_petrol=10355, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=18069, health=18061, time=86535, cost_metal=12325, cost_crystal=24650, cost_petrol=12325, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=21805, health=22422, time=117433, cost_metal=14874, cost_crystal=29748, cost_petrol=14874, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=26675, health=27757, time=167078, cost_metal=18196, cost_crystal=36391, cost_petrol=18196, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=79972, health=43751, time=311346, cost_metal=27276, cost_crystal=54551, cost_petrol=27276, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                )
            }
        ),
        HANGAR: BuildableItemBaseType(
            "Hangar",
            HANGAR,
            TYPE,
            None,
            "Hangar is needed in order to build and store spaceships and defense",
            {
                0: BuildableItemLevelInfo(
                    level=0, experience=0, health=0, time=0, cost_metal=0, cost_crystal=0, cost_petrol=0, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                    BuildableItemRequirement(TYPE, INVESTIGATION_LABORATORY, 5)
                    ], has_discount=0
                ),
                1: BuildableItemLevelInfo(
                    level=1, experience=235, health=3000, time=600, cost_metal=800, cost_crystal=400, cost_petrol=300, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=320, health=3064, time=938, cost_metal=1090, cost_crystal=545, cost_petrol=409, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=428, health=3150, time=1423, cost_metal=1458, cost_crystal=729, cost_petrol=547, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=562, health=3262, time=2094, cost_metal=1915, cost_crystal=957, cost_petrol=718, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=725, health=3407, time=2985, cost_metal=2469, cost_crystal=1234, cost_petrol=926, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=917, health=3590, time=4117, cost_metal=3123, cost_crystal=1562, cost_petrol=1171, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=1138, health=3818, time=5488, cost_metal=3875, cost_crystal=1938, cost_petrol=1453, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=1384, health=4095, time=7064, cost_metal=4714, cost_crystal=2357, cost_petrol=1768, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=1650, health=4425, time=8767, cost_metal=5621, cost_crystal=2810, cost_petrol=2108, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=1928, health=4810, time=10477, cost_metal=6565, cost_crystal=3283, cost_petrol=2462, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=2205, health=5251, time=12038, cost_metal=7509, cost_crystal=3755, cost_petrol=2816, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=2468, health=5745, time=13277, cost_metal=8407, cost_crystal=4203, cost_petrol=3153, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=4134, health=6572, time=14596, cost_metal=9387, cost_crystal=4694, cost_petrol=3520, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=4605, health=7493, time=15993, cost_metal=10454, cost_crystal=5227, cost_petrol=3920, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=5115, health=8516, time=17465, cost_metal=11612, cost_crystal=5806, cost_petrol=4355, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=5666, health=9649, time=19010, cost_metal=12865, cost_crystal=6432, cost_petrol=4824, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=6260, health=10901, time=20622, cost_metal=14214, cost_crystal=7107, cost_petrol=5330, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=6899, health=12281, time=22296, cost_metal=15664, cost_crystal=7832, cost_petrol=5874, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=7582, health=13797, time=24025, cost_metal=17215, cost_crystal=8607, cost_petrol=6456, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=8311, health=15459, time=25801, cost_metal=18870, cost_crystal=9435, cost_petrol=7076, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=9085, health=17277, time=27614, cost_metal=20628, cost_crystal=10314, cost_petrol=7736, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=9905, health=19258, time=29455, cost_metal=22490, cost_crystal=11245, cost_petrol=8434, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=10771, health=21412, time=31311, cost_metal=24454, cost_crystal=12227, cost_petrol=9170, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=11680, health=23748, time=33171, cost_metal=26518, cost_crystal=13259, cost_petrol=9944, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=17056, health=27159, time=36760, cost_metal=29044, cost_crystal=14522, cost_petrol=10892, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=18866, health=30932, time=42530, cost_metal=32126, cost_crystal=16063, cost_petrol=12047, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=21072, health=35147, time=51281, cost_metal=35883, cost_crystal=17942, cost_petrol=13456, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=23766, health=39900, time=64336, cost_metal=40469, cost_crystal=20235, cost_petrol=15176, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=27061, health=45312, time=83852, cost_metal=46081, cost_crystal=23040, cost_petrol=17280, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=77660, health=60844, time=151509, cost_metal=66122, cost_crystal=33061, cost_petrol=24796, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                )
            }
        )
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
