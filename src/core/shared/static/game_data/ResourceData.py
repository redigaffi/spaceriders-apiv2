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
                    1, 50, 0, 40, 0.02, 5, 0, 600, 250, 0, 30, [], 1
                ),
                2: BuildableItemLevelInfo(
                    2, 100, 0, 60, 0.03, 10, 0, 1200, 500, 0, 40, [], 1
                ),
                3: BuildableItemLevelInfo(
                    3, 150, 0, 100, 0.06, 15, 0, 1600, 800, 0, 50, [], 1
                ),
                4: BuildableItemLevelInfo(
                    4, 200, 0, 120, 0.07, 20, 0, 1800, 900, 0, 60, [], 1
                ),
                5: BuildableItemLevelInfo(
                    5,
                    250,
                    0,
                    140,
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
                    0,
                    160,
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
                    0,
                    200,
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
                    0,
                    250,
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
                    0,
                    270,
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
                    0,
                    390,
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
                    0,
                    560,
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
                    0,
                    620,
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
                    0,
                    780,
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
                    0,
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
                    0,
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
                    0,
                    1020,
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
                    0,
                    1230,
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
                    0,
                    1350,
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
                    0,
                    1420,
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
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 4),
                    ],
                    1,
                ),
                20: BuildableItemLevelInfo(
                    20,
                    3300,
                    0,
                    1500,
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
        CRYSTAL_MINE: BuildableItemBaseType(
            "Crystal Mine",
            CRYSTAL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Crystal mine to extract metal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 50, 40, 0, 0.02, 5, 0, 600, 250, 0, 30, [], 1
                ),
                2: BuildableItemLevelInfo(
                    2, 100, 60, 0, 0.03, 10, 0, 1200, 500, 0, 40, [], 1
                ),
                3: BuildableItemLevelInfo(
                    3, 150, 100, 0, 0.06, 15, 0, 1600, 800, 0, 50, [], 1
                ),
                4: BuildableItemLevelInfo(
                    4, 200, 120, 0, 0.07, 20, 0, 1800, 900, 0, 60, [], 1
                ),
                5: BuildableItemLevelInfo(
                    5,
                    250,
                    140,
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                    0,
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
                        BuildableItemRequirement(RD.TYPE, RD.TERRAFORMING, 4),
                    ],
                    1,
                ),
                20: BuildableItemLevelInfo(
                    20,
                    3300,
                    1500,
                    0,
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
        PETROL_MINE: BuildableItemBaseType(
            "Petrol Mine",
            PETROL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Petrol mine to extract metal",
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
