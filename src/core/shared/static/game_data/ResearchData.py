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
                    level=1, experience=925, health=2250, time=450, cost_metal=700, cost_crystal=860, cost_petrol=1400, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 1),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 2)
                    ], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=1260, health=2502, time=704, cost_metal=953, cost_crystal=1171, cost_petrol=1907, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=1686, health=2839, time=1067, cost_metal=1275, cost_crystal=1567, cost_petrol=2551, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=2214, health=3282, time=1571, cost_metal=1675, cost_crystal=2058, cost_petrol=3351, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=2855, health=3853, time=2239, cost_metal=2160, cost_crystal=2654, cost_petrol=4320, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 5)
                    ], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=3611, health=4575, time=3087, cost_metal=2733, cost_crystal=3357, cost_petrol=5465, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=4481, health=5471, time=4116, cost_metal=3391, cost_crystal=4166, cost_petrol=6781, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=5451, health=6561, time=5298, cost_metal=4125, cost_crystal=5068, cost_petrol=8250, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=6499, health=7861, time=6575, cost_metal=4918, cost_crystal=6042, cost_petrol=9836, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=7591, health=9380, time=7858, cost_metal=5744, cost_crystal=7058, cost_petrol=11489, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 7)
                    ], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=8683, health=11116, time=9028, cost_metal=6571, cost_crystal=8072, cost_petrol=13141, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=9721, health=13060, time=9958, cost_metal=7356, cost_crystal=9037, cost_petrol=14712, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=16282, health=16317, time=10947, cost_metal=8214, cost_crystal=10091, cost_petrol=16428, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=18133, health=19943, time=11995, cost_metal=9148, cost_crystal=11239, cost_petrol=18295, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=20141, health=23971, time=13099, cost_metal=10161, cost_crystal=12483, cost_petrol=20322, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 7),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 10)
                    ], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=22313, health=28434, time=14257, cost_metal=11256, cost_crystal=13829, cost_petrol=22513, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=24654, health=33365, time=15466, cost_metal=12437, cost_crystal=15280, cost_petrol=24875, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=27168, health=38798, time=16722, cost_metal=13706, cost_crystal=16838, cost_petrol=27411, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=29859, health=44770, time=18019, cost_metal=15063, cost_crystal=18506, cost_petrol=30126, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=32729, health=51316, time=19350, cost_metal=16511, cost_crystal=20285, cost_petrol=33022, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 9),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 13)
                    ], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=35779, health=58472, time=20711, cost_metal=18050, cost_crystal=22175, cost_petrol=36099, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=39008, health=66273, time=22091, cost_metal=19679, cost_crystal=24177, cost_petrol=39358, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=42415, health=74756, time=23483, cost_metal=21397, cost_crystal=26288, cost_petrol=42795, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=45995, health=83955, time=24878, cost_metal=23203, cost_crystal=28507, cost_petrol=46407, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=67168, health=97389, time=27570, cost_metal=25414, cost_crystal=31223, cost_petrol=50827, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 12),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 16)
                    ], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=74295, health=112248, time=31898, cost_metal=28110, cost_crystal=34535, cost_petrol=56220, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=82984, health=128845, time=38461, cost_metal=31398, cost_crystal=38574, cost_petrol=62796, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=93590, health=147563, time=48252, cost_metal=35411, cost_crystal=43505, cost_petrol=70821, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=106567, health=168876, time=62889, cost_metal=40321, cost_crystal=49537, cost_petrol=80641, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=305831, health=230043, time=113632, cost_metal=57857, cost_crystal=71081, cost_petrol=115714, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 15),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 20)
                    ], has_discount=0
                ),
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
                    level=1, experience=4047, health=3000, time=750, cost_metal=3000, cost_crystal=4000, cost_petrol=6000, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 5)
                    ], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=5462, health=4092, time=1201, cost_metal=4049, cost_crystal=5399, cost_petrol=8098, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=7172, health=5527, time=1846, cost_metal=5317, cost_crystal=7089, cost_petrol=10634, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=9156, health=7358, time=2714, cost_metal=6787, cost_crystal=9049, cost_petrol=13574, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=11352, health=9628, time=3811, cost_metal=8415, cost_crystal=11220, cost_petrol=16830, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 7),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 10)
                    ], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=13660, health=12360, time=5102, cost_metal=10126, cost_crystal=13501, cost_petrol=20252, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=15937, health=15548, time=6495, cost_metal=11814, cost_crystal=15752, cost_petrol=23628, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=18010, health=19150, time=7840, cost_metal=13351, cost_crystal=17801, cost_petrol=26702, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=30411, health=25232, time=9426, cost_metal=15029, cost_crystal=20039, cost_petrol=30058, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=34101, health=32052, time=11287, cost_metal=16852, cost_crystal=22470, cost_petrol=33705, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 11),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 15)
                    ], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=38087, health=39670, time=13462, cost_metal=18823, cost_crystal=25097, cost_petrol=37645, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=42373, health=48144, time=15991, cost_metal=20940, cost_crystal=27921, cost_petrol=41881, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=46954, health=57535, time=18918, cost_metal=23205, cost_crystal=30939, cost_petrol=46409, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=51825, health=67900, time=22289, cost_metal=25611, cost_crystal=34149, cost_petrol=51223, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=56973, health=79295, time=26154, cost_metal=28155, cost_crystal=37541, cost_petrol=56311, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 15),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 20)
                    ], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=62381, health=91771, time=30563, cost_metal=30828, cost_crystal=41105, cost_petrol=61657, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=92570, health=110285, time=37878, cost_metal=34311, cost_crystal=45747, cost_petrol=68621, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=104694, health=131224, time=49624, cost_metal=38804, cost_crystal=51739, cost_petrol=77609, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=120293, health=155282, time=68524, cost_metal=44586, cost_crystal=59448, cost_petrol=89172, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=347707, health=224824, time=126408, cost_metal=64438, cost_crystal=85917, cost_petrol=128876, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 20),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 25)
                    ], has_discount=0
                ),
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
                    level=1, experience=1412, health=2750, time=1000, cost_metal=2000, cost_crystal=1000, cost_petrol=2000, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 7)
                    ], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=2232, health=3196, time=1718, cost_metal=3163, cost_crystal=1582, cost_petrol=3163, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=3402, health=3877, time=2756, cost_metal=4821, cost_crystal=2410, cost_petrol=4821, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=4990, health=4875, time=4106, cost_metal=7071, cost_crystal=3535, cost_petrol=7071, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=10931, health=7061, time=6088, cost_metal=10326, cost_crystal=5163, cost_petrol=10326, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 8),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 10)
                    ], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=15896, health=10240, time=8983, cost_metal=15015, cost_crystal=7508, cost_petrol=15015, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=23014, health=14843, time=13191, cost_metal=21740, cost_crystal=10870, cost_petrol=21740, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=33177, health=21479, time=19278, cost_metal=31340, cost_crystal=15670, cost_petrol=31340, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=65440, health=34567, time=31026, cost_metal=46362, cost_crystal=23181, cost_petrol=46362, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=222496, health=79066, time=61460, cost_metal=78815, cost_crystal=39408, cost_petrol=78815, production=0, energy_usage=0, capacity=0, attack=0,
                    requirements=[
                        BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 10),
                        BuildableItemRequirement(ID.TYPE, ID.HANGAR, 15)
                    ], has_discount=0
                ),
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
