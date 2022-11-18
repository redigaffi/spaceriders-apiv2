from dataclasses import dataclass

from .Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
    BuildableItemRequirement,
)
from .Common import CommonKeys as CK
from .InstallationData import InstallationData as ID
from .ResearchData import ResearchData as RD
from .GameData import GameData


@dataclass
class ResourceData(GameData):
    """
    Data class representing in game items
    Production is expressed per minute
    """

    TYPE = "resources"

    MINE_CATEGORY = "mine_category"
    WAREHOUSE_CATEGORY = "warehouse_category"

    METAL_MINE = "metalMine"
    CRYSTAL_MINE = "crystalMine"
    PETROL_MINE = "petrolMine"
    METAL_WAREHOUSE = "metalWarehouse"
    CRYSTAL_WAREHOUSE = "crystalWarehouse"
    PETROL_WAREHOUSE = "petrolWarehouse"

    TYPES = [
        METAL_MINE,
        CRYSTAL_MINE,
        PETROL_MINE,
        METAL_WAREHOUSE,
        CRYSTAL_WAREHOUSE,
        PETROL_WAREHOUSE,
    ]

    COMMON_WAREHOUSE_KEYS = [
        CK.LEVEL,
        CK.COST_METAL,
        CK.COST_PETROL,
        CK.COST_CRYSTAL,
        CK.CAPACITY,
        CK.TIME,
        CK.HEALTH,
        CK.EXPERIENCE,
        CK.REQUIREMENTS,
    ]

    __ITEMS = {
        METAL_MINE: BuildableItemBaseType(
            "Metal Mine",
            METAL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Metal mine to extract metal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=9, health=1000, time=70, cost_metal=60, cost_crystal=15, cost_petrol=0,
                    production=1.0, energy_usage=0.10, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=12, health=1002, time=111, cost_metal=82, cost_crystal=21, cost_petrol=0,
                    production=1.03, energy_usage=0.103318, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=16, health=1006, time=176, cost_metal=112, cost_crystal=28, cost_petrol=0,
                    production=1.07, energy_usage=0.107115, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=22, health=1010, time=263, cost_metal=150, cost_crystal=38, cost_petrol=0,
                    production=1.11, energy_usage=0.111434, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=29, health=1016, time=394, cost_metal=199, cost_crystal=50, cost_petrol=0,
                    production=1.16, energy_usage=0.116323, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=38, health=1023, time=581, cost_metal=262, cost_crystal=65, cost_petrol=0,
                    production=1.22, energy_usage=0.121842, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=49, health=1033, time=839, cost_metal=340, cost_crystal=85, cost_petrol=0,
                    production=1.28, energy_usage=0.128057, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=63, health=1046, time=1190, cost_metal=437, cost_crystal=109, cost_petrol=0,
                    production=1.35, energy_usage=0.135046, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=80, health=1061, time=1655, cost_metal=555, cost_crystal=139, cost_petrol=0,
                    production=1.43, energy_usage=0.142898, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=100, health=1082, time=2256, cost_metal=698, cost_crystal=174, cost_petrol=0,
                    production=1.52, energy_usage=0.151715, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=125, health=1106, time=3013, cost_metal=866, cost_crystal=217, cost_petrol=0,
                    production=1.62, energy_usage=0.161618, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=153, health=1137, time=3942, cost_metal=1063, cost_crystal=266, cost_petrol=0,
                    production=1.73, energy_usage=0.172743, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=185, health=1174, time=5050, cost_metal=1289, cost_crystal=322, cost_petrol=0,
                    production=1.85, energy_usage=0.185249, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=222, health=1218, time=6331, cost_metal=1544, cost_crystal=386, cost_petrol=0,
                    production=1.99, energy_usage=0.199322, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=263, health=1271, time=7763, cost_metal=1827, cost_crystal=457, cost_petrol=0,
                    production=2.15, energy_usage=0.215174, capacity=0, attack=0, requirements=[], has_discount=0
                ),
            },
        ),
        CRYSTAL_MINE: BuildableItemBaseType(
            "Crystal Mine",
            CRYSTAL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Crystal mine to extract Crystal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 48, 0, 24, 0.10, 0.57, 0, 91, 1000, 0, 9, [], 1
                ),
                2: BuildableItemLevelInfo(
                    2, 66, 0, 33, 0.103318, 0.59, 0, 144, 1002, 0, 12, [], 1
                ),
                3: BuildableItemLevelInfo(
                    3, 89, 0, 45, 0.107115, 0.61, 0, 224, 1006, 0, 17, [], 1
                ),
                4: BuildableItemLevelInfo(
                    4, 89, 0, 45, 0.111434, 0.64, 0, 342, 1010, 0, 23, [], 1
                ),
                5: BuildableItemLevelInfo(
                    5,
                    120,
                    0,
                    45,
                    0.116323,
                    0.66,
                    0,
                    513,
                    1016,
                    0,
                    30,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 1)],
                    1,
                ),
                6: BuildableItemLevelInfo(
                    6,
                    209,
                    0,
                    105,
                    0.121842,
                    0.70,
                    0,
                    755,
                    1024,
                    0,
                    39,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 1)],
                    1,
                ),
                7: BuildableItemLevelInfo(
                    7,
                    272,
                    0,
                    136,
                    0.128057,
                    0.73,
                    0,
                    1091,
                    1034,
                    0,
                    51,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 1)],
                    1,
                ),
                8: BuildableItemLevelInfo(
                    8,
                    350,
                    0,
                    175,
                    0.135046,
                    0.77,
                    0,
                    1547,
                    1047,
                    0,
                    66,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
                    1,
                ),
                9: BuildableItemLevelInfo(
                    9,
                    444,
                    0,
                    222,
                    0.142898,
                    0.82,
                    0,
                    2151,
                    1064,
                    0,
                    83,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
                    1,
                ),
                10: BuildableItemLevelInfo(
                    10,
                    558,
                    0,
                    279,
                    0.1517175,
                    0.87,
                    0,
                    2800,
                    1500,
                    0,
                    120,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
                    1,
                ),
                11: BuildableItemLevelInfo(
                    11,
                    693,
                    0,
                    346,
                    0.161618,
                    0.92,
                    0,
                    3917,
                    1111,
                    0,
                    130,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
                    1,
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=159, health=1143, time=5125, cost_metal=850, cost_crystal=425, cost_petrol=0,
                    energy_usage=0.172743, production=0.99, capacity=0, attack=0, requirements=[BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=193, health=1182, time=6565, cost_metal=1031, cost_crystal=515, cost_petrol=0,
                    energy_usage=0.185249, production=1.06, capacity=0, attack=0, requirements=[BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=232, health=1228, time=8230, cost_metal=1235, cost_crystal=618, cost_petrol=0,
                    energy_usage=0.199322, production=1.14, capacity=0, attack=0, requirements=[BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=274, health=1283, time=10092, cost_metal=1462, cost_crystal=731, cost_petrol=0,
                    energy_usage=0.215174, production=1.23, capacity=0, attack=0, requirements=[BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)], has_discount=0
                ),
            },
        ),
        PETROL_MINE: BuildableItemBaseType(
            "Petrol Mine",
            PETROL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Petrol mine to extract Petrol",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 50, 40, 50, 0.02, 5, 0, 600, 250, 0, 30, [], 1
                ),
                2: BuildableItemLevelInfo(
                    2, 100, 60, 100, 0.03, 10, 0, 1200, 500, 0, 40, [], 1
                ),
                3: BuildableItemLevelInfo(
                    3, 150, 100, 120, 0.06, 15, 0, 1600, 800, 0, 50, [], 1
                ),
                4: BuildableItemLevelInfo(
                    4, 200, 120, 150, 0.07, 20, 0, 1800, 900, 0, 60, [], 1
                ),
                5: BuildableItemLevelInfo(
                    5,
                    250,
                    140,
                    200,
                    0.08,
                    25,
                    0,
                    1900,
                    1000,
                    0,
                    70,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)],
                    1,
                ),
                6: BuildableItemLevelInfo(
                    6,
                    300,
                    160,
                    240,
                    0.09,
                    30,
                    0,
                    2000,
                    1100,
                    0,
                    80,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)],
                    1,
                ),
                7: BuildableItemLevelInfo(
                    7,
                    350,
                    200,
                    350,
                    0.10,
                    35,
                    0,
                    2200,
                    1200,
                    0,
                    90,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 4)],
                    1,
                ),
                8: BuildableItemLevelInfo(
                    8,
                    500,
                    250,
                    420,
                    0.12,
                    40,
                    0,
                    2400,
                    1300,
                    0,
                    100,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 4)],
                    1,
                ),
                9: BuildableItemLevelInfo(
                    9,
                    670,
                    270,
                    550,
                    0.13,
                    50,
                    0,
                    2600,
                    1400,
                    0,
                    110,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 4)],
                    1,
                ),
                10: BuildableItemLevelInfo(
                    10,
                    1005,
                    390,
                    610,
                    0.14,
                    60,
                    0,
                    2800,
                    1500,
                    0,
                    120,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5)],
                    1,
                ),
                11: BuildableItemLevelInfo(
                    11,
                    1310,
                    560,
                    700,
                    0.16,
                    75,
                    0,
                    3000,
                    1650,
                    0,
                    140,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5)],
                    1,
                ),
                12: BuildableItemLevelInfo(
                    12,
                    1420,
                    620,
                    730,
                    0.19,
                    85,
                    0,
                    3200,
                    1850,
                    0,
                    165,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 6)],
                    1,
                ),
                13: BuildableItemLevelInfo(
                    13,
                    1640,
                    780,
                    810,
                    0.22,
                    105,
                    0,
                    3600,
                    2050,
                    0,
                    190,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 7
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 1),
                    ],
                    1,
                ),
                14: BuildableItemLevelInfo(
                    14,
                    1760,
                    900,
                    900,
                    0.26,
                    140,
                    0,
                    4200,
                    2300,
                    0,
                    220,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 7
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 2),
                    ],
                    1,
                ),
                15: BuildableItemLevelInfo(
                    15,
                    1880,
                    980,
                    980,
                    0.30,
                    170,
                    0,
                    4800,
                    2650,
                    0,
                    250,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 8
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 2),
                    ],
                    1,
                ),
                16: BuildableItemLevelInfo(
                    16,
                    2000,
                    1020,
                    1100,
                    0.35,
                    250,
                    0,
                    5500,
                    2950,
                    0,
                    340,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 8
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 3),
                    ],
                    1,
                ),
                17: BuildableItemLevelInfo(
                    17,
                    2250,
                    1230,
                    1300,
                    0.40,
                    350,
                    0,
                    6500,
                    3750,
                    0,
                    450,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 9
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 4),
                    ],
                    1,
                ),
                18: BuildableItemLevelInfo(
                    18,
                    2800,
                    1350,
                    1400,
                    0.45,
                    470,
                    0,
                    7500,
                    4500,
                    0,
                    520,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 9
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 4),
                    ],
                    1,
                ),
                19: BuildableItemLevelInfo(
                    19,
                    3000,
                    1420,
                    1500,
                    0.50,
                    590,
                    0,
                    8500,
                    5500,
                    0,
                    630,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 10
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 5),
                    ],
                    1,
                ),
                20: BuildableItemLevelInfo(
                    20,
                    3300,
                    1500,
                    1600,
                    0.55,
                    700,
                    0,
                    9500,
                    7000,
                    0,
                    750,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 10
                        ),
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 5),
                    ],
                    1,
                ),
            },
        ),
        METAL_WAREHOUSE: BuildableItemBaseType(
            "Metal Warehouse",
            METAL_WAREHOUSE,
            TYPE,
            WAREHOUSE_CATEGORY,
            "Metal warehouse to store metal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 60, 20, 40, 0, 0, 1000, 30, 60, 0, 0, [], 0
                ),
                2: BuildableItemLevelInfo(
                    2, 120, 40, 80, 0, 0, 1500, 60, 120, 0, 0, [], 0
                ),
                3: BuildableItemLevelInfo(
                    3, 240, 80, 160, 0, 0, 2000, 120, 240, 0, 0, [], 0
                ),
                4: BuildableItemLevelInfo(
                    4, 480, 160, 320, 0, 0, 3000, 240, 600, 0, 0, [], 0
                ),
                5: BuildableItemLevelInfo(
                    5, 1000, 400, 600, 0, 0, 5000, 500, 1200, 0, 0, [], 0
                ),
                6: BuildableItemLevelInfo(
                    6, 2500, 600, 800, 0, 0, 6000, 1000, 1800, 0, 0, [], 0
                ),
                7: BuildableItemLevelInfo(
                    7, 3500, 1000, 1300, 0, 0, 7000, 2300, 2500, 0, 0, [], 0
                ),
                8: BuildableItemLevelInfo(
                    8, 5500, 1500, 2000, 0, 0, 8000, 3300, 3500, 0, 0, [], 0
                ),
                9: BuildableItemLevelInfo(
                    9, 6500, 2500, 3000, 0, 0, 9000, 4500, 5000, 0, 0, [], 0
                ),
                10: BuildableItemLevelInfo(
                    10, 7500, 3500, 4000, 0, 0, 10000, 5500, 7000, 0, 0, [], 0
                ),
            },
        ),
        CRYSTAL_WAREHOUSE: BuildableItemBaseType(
            "Crystal Warehouse",
            CRYSTAL_WAREHOUSE,
            TYPE,
            WAREHOUSE_CATEGORY,
            "Crystal warehouse to store crystal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=235, health=2000, time=780, cost_metal=500, cost_crystal=250, cost_petrol=500,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=320, health=2064, time=1219, cost_metal=681, cost_crystal=341, cost_petrol=681,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=429, health=2150, time=1850, cost_metal=911, cost_crystal=456, cost_petrol=911,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=563, health=2408, time=2722, cost_metal=1197, cost_crystal=598, cost_petrol=1197,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                     level=5, experience=726, health=2262, time=3880, cost_metal=1543, cost_crystal=771, cost_petrol=1543,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                     level=6, experience=918, health=2591, time=5352, cost_metal=1952, cost_crystal=976, cost_petrol=1952,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                     level=7, experience=1139, health=2819, time=7135, cost_metal=2422, cost_crystal=1211, cost_petrol=2422,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                     level=8, experience=1386, health=3096, time=9183, cost_metal=2946, cost_crystal=1473, cost_petrol=2946,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                     level=9, experience=1653, health=3427, time=11397, cost_metal=3513, cost_crystal=1756, cost_petrol=3513,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                     level=10, experience=1931, health=3813, time=13620, cost_metal=4103, cost_crystal=2052, cost_petrol=4103,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
            },
        ),
        PETROL_WAREHOUSE: BuildableItemBaseType(
            "Petrol Warehouse",
            PETROL_WAREHOUSE,
            TYPE,
            WAREHOUSE_CATEGORY,
            "Petrol warehouse to store petrol",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 60, 20, 40, 0, 0, 1000, 30, 60, 0, 0, [], 0
                ),
                2: BuildableItemLevelInfo(
                    2, 120, 40, 80, 0, 0, 1500, 60, 120, 0, 0, [], 0
                ),
                3: BuildableItemLevelInfo(
                    3, 240, 80, 160, 0, 0, 2000, 120, 240, 0, 0, [], 0
                ),
                4: BuildableItemLevelInfo(
                    4, 480, 160, 320, 0, 0, 3000, 240, 600, 0, 0, [], 0
                ),
                5: BuildableItemLevelInfo(
                    5, 1000, 400, 600, 0, 0, 5000, 500, 1200, 0, 0, [], 0
                ),
                6: BuildableItemLevelInfo(
                    6, 2500, 600, 800, 0, 0, 6000, 1000, 1800, 0, 0, [], 0
                ),
                7: BuildableItemLevelInfo(
                    7, 3500, 1000, 1300, 0, 0, 7000, 2300, 2500, 0, 0, [], 0
                ),
                8: BuildableItemLevelInfo(
                    8, 5500, 1500, 2000, 0, 0, 8000, 3300, 3500, 0, 0, [], 0
                ),
                9: BuildableItemLevelInfo(
                    9, 6500, 2500, 3000, 0, 0, 9000, 4500, 5000, 0, 0, [], 0
                ),
                10: BuildableItemLevelInfo(
                    10, 7500, 3500, 4000, 0, 0, 10000, 5500, 7000, 0, 0, [], 0
                ),
            },
        ),
    }
    @staticmethod
    def valid_type(label: str) -> bool:
        return label in ResourceData.TYPES

    @staticmethod
    def get_type() -> str:
        return ResourceData.TYPE

    @staticmethod
    def get_item(key: str) -> BuildableItemBaseType:
        if key not in ResourceData.TYPES:
            raise ValueError(
                f"{key} not in {ResourceData.TYPES} for {ResourceData.TYPE}"
            )

        return ResourceData.__ITEMS[key]
