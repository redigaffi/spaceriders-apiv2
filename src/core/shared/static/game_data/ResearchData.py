from dataclasses import dataclass

from .Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
    BuildableItemRequirement,
)
from .GameData import GameData
from .InstallationData import InstallationData as ID


@dataclass
class ResearchData(GameData):
    """
    Data class representing in game items
    """

    TYPE = "research"

    ASTEROID_PRECISION = "asteroidPrecision"
    TERRAFORMING = "terraforming"
    LASER_RESEARCH = "laserResearch"

    TYPES = [ASTEROID_PRECISION, TERRAFORMING, LASER_RESEARCH]

    __ITEMS = {
        ASTEROID_PRECISION: BuildableItemBaseType(
            "Asteroid Precision",
            ASTEROID_PRECISION,
            TYPE,
            None,
            "For every upgrade increase chance by 1% of hitting an asteroid",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=925, health=2250, time=900, cost_metal=700, cost_crystal=860, cost_petrol=1400, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 1),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 2)
                    ], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=1260, health=2502, time=1407, cost_metal=953, cost_crystal=1171, cost_petrol=1907, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=1686, health=2839, time=2135, cost_metal=1275, cost_crystal=1567, cost_petrol=2551, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=2214, health=3282, time=3141, cost_metal=1675, cost_crystal=2058, cost_petrol=3351, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=2855, health=3853, time=4477, cost_metal=2160, cost_crystal=2654, cost_petrol=4320, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 5)
                    ], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=3611, health=4575, time=6175, cost_metal=2733, cost_crystal=3357, cost_petrol=5465, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=4481, health=5471, time=8232, cost_metal=3391, cost_crystal=4166, cost_petrol=6781, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=5451, health=6561, time=10596, cost_metal=4125, cost_crystal=5068, cost_petrol=8250, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=6499, health=7861, time=13150, cost_metal=4918, cost_crystal=6042, cost_petrol=9836, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=7591, health=9380, time=15715, cost_metal=5744, cost_crystal=7058, cost_petrol=11489, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 7)
                    ], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=8683, health=11116, time=18057, cost_metal=6571, cost_crystal=8072, cost_petrol=13141, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=9721, health=13060, time=19916, cost_metal=7356, cost_crystal=9037, cost_petrol=14712, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=16282, health=16317, time=21894, cost_metal=8214, cost_crystal=10091, cost_petrol=16428, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=18133, health=19943, time=23989, cost_metal=9148, cost_crystal=11239, cost_petrol=18295, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=20141, health=23971, time=26198, cost_metal=10161, cost_crystal=12483, cost_petrol=20322, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 7),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 10)
                    ], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=22313, health=28434, time=28515, cost_metal=11256, cost_crystal=13829, cost_petrol=22513, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=24654, health=33365, time=30933, cost_metal=12437, cost_crystal=15280, cost_petrol=24875, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=27168, health=38798, time=33444, cost_metal=13706, cost_crystal=16838, cost_petrol=27411, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=29859, health=44770, time=36037, cost_metal=15063, cost_crystal=18506, cost_petrol=30126, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=32729, health=51316, time=38701, cost_metal=16511, cost_crystal=20285, cost_petrol=33022, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 9),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 13)
                    ], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=35779, health=58472, time=41421, cost_metal=18050, cost_crystal=22175, cost_petrol=36099, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=39008, health=66273, time=44182, cost_metal=19679, cost_crystal=24177, cost_petrol=39358, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=42415, health=74756, time=46967, cost_metal=21397, cost_crystal=26288, cost_petrol=42795, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=45995, health=83955, time=49756, cost_metal=23203, cost_crystal=28507, cost_petrol=46407, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=67168, health=97389, time=55139, cost_metal=25414, cost_crystal=31223, cost_petrol=50827, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 12),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 16)
                    ], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=74295, health=112248, time=63795, cost_metal=28110, cost_crystal=34535, cost_petrol=56220, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=82984, health=128845, time=76922, cost_metal=31398, cost_crystal=38574, cost_petrol=62796, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=93590, health=147563, time=96503, cost_metal=35411, cost_crystal=43505, cost_petrol=70821, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=106567, health=168876, time=125777, cost_metal=40321, cost_crystal=49537, cost_petrol=80641, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=305831, health=230043, time=227264, cost_metal=57857, cost_crystal=71081, cost_petrol=115714, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 15),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 20)
                    ], has_discount=0
                )
            },
        ),
        TERRAFORMING: BuildableItemBaseType(
            "Terraforming",
            TERRAFORMING,
            TYPE,
            None,
            "For Every upgrade get 1 additional slot on your planet.",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=293, health=2000, time=900, cost_metal=400, cost_crystal=800, cost_petrol=400, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 5)
                    ], has_discount=0
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
                    level=5, experience=1004, health=2551, time=5126, cost_metal=1370, cost_crystal=2740, cost_petrol=1370, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 7),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 10)
                    ], has_discount=0
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
                    level=10, experience=4137, health=5026, time=18719, cost_metal=3762, cost_crystal=7524, cost_petrol=3762, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 11),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 15)
                    ], has_discount=0
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
                    level=15, experience=9700, health=12170, time=54673, cost_metal=8822, cost_crystal=17645, cost_petrol=8822, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 15),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 20)
                    ], has_discount=0
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
                    level=20, experience=79972, health=43751, time=311346, cost_metal=27276, cost_crystal=54551, cost_petrol=27276, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 20),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 25)
                    ], has_discount=0
                )
            },
        ),
        LASER_RESEARCH: BuildableItemBaseType(
            "Laser Research",
            LASER_RESEARCH,
            TYPE,
            None,
            "Research in how to implement/improve laser technology in using laser for military approach.",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=1412, health=2750, time=2000, cost_metal=2000, cost_crystal=1000, cost_petrol=2000, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 7)
                    ], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=2232, health=3196, time=3437, cost_metal=3163, cost_crystal=1582, cost_petrol=3163, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=3402, health=3877, time=5512, cost_metal=4821, cost_crystal=2410, cost_petrol=4821, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=4990, health=4875, time=8212, cost_metal=7071, cost_crystal=3535, cost_petrol=7071, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=10931, health=7061, time=12175, cost_metal=10326, cost_crystal=5163, cost_petrol=10326, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 8),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 10)
                    ], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=15896, health=10240, time=17965, cost_metal=15015, cost_crystal=7508, cost_petrol=15015, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=23014, health=14843, time=26382, cost_metal=21740, cost_crystal=10870, cost_petrol=21740, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=33177, health=21479, time=38556, cost_metal=31340, cost_crystal=15670, cost_petrol=31340, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=65440, health=34567, time=62051, cost_metal=46362, cost_crystal=23181, cost_petrol=46362, production=0, energy_usage=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=222496, health=79066, time=122919, cost_metal=78815, cost_crystal=39408, cost_petrol=78815, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 10),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 15)
                    ], has_discount=0
                )
            },
        ),
    }

    @staticmethod
    def valid_type(label: str) -> bool:
        return label in ResearchData.TYPES

    @staticmethod
    def get_type() -> str:
        return ResearchData.TYPE

    @staticmethod
    def get_item(key: str) -> BuildableItemBaseType:
        if key not in ResearchData.TYPES:
            raise ValueError(
                f"{key} not in {ResearchData.TYPES} for {ResearchData.TYPE}"
            )

        return ResearchData.__ITEMS[key]
