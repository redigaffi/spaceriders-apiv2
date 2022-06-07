from dataclasses import dataclass
from .Common import BuildableItemBaseType, CommonKeys as CK, BuildableItemLevelInfo
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
        PETROL_WAREHOUSE
    ]

    COMMON_WAREHOUSE_KEYS = [CK.LEVEL, CK.COST_METAL, CK.COST_PETROL, CK.COST_CRYSTAL, CK.CAPACITY, CK.TIME, CK.HEALTH,
                             CK.EXPERIENCE, CK.REQUIREMENTS]
    __ITEMS = {
        METAL_MINE: BuildableItemBaseType("Metal Mine", METAL_MINE, TYPE, MINE_CATEGORY, "Metal mine to extract metal",
                                          {
                                              0: BuildableItemLevelInfo(0, 100, 0, 60, 0, 0, 0, 60, 10, 0, 0, [], 0),
                                              1: BuildableItemLevelInfo(1, 50, 0, 40, 0.01, 5, 0, 10, 500, 0, 500, [], 1),
                                              2: BuildableItemLevelInfo(2, 100, 0, 60, 0.03, 5, 0, 1200, 500, 0, 0, [], 1),

                                              3: BuildableItemLevelInfo(3, 150, 0, 100, 0.06, 10, 0, 1600, 800, 0, 50, [], 1),
                                              4: BuildableItemLevelInfo(4, 200, 0, 120, 0.07, 15, 0, 1800, 900, 0, 60,
                                                                        [], 1),
                                              5: BuildableItemLevelInfo(5, 250, 0, 140, 0.08, 20, 0, 1900, 1000, 0, 70,
                                                                        [], 1),
                                              6: BuildableItemLevelInfo(6, 300, 0, 160, 0.09, 25, 0, 2000, 1100, 0, 80,
                                                                        [], 1),

                                              7: BuildableItemLevelInfo(7, 350, 0, 200, 0.10, 35, 0, 2200, 1200, 0, 90,
                                                                        [], 1),
                                              8: BuildableItemLevelInfo(8, 500, 0, 250, 0.12, 40, 0, 2400, 1300, 0, 100,
                                                                        [], 1),
                                              9: BuildableItemLevelInfo(9, 670, 0, 270, 0.13, 50, 0, 2600, 1400, 0, 110,
                                                                        [], 1),
                                              10: BuildableItemLevelInfo(10, 1000, 0, 390, 0.14, 60, 0, 2800, 1500, 0, 120,
                                                                        [], 1),
                                          }
                                          ),

        CRYSTAL_MINE: BuildableItemBaseType("Crystal Mine", CRYSTAL_MINE, TYPE, MINE_CATEGORY,  "Crystal mine to extract metal",
                                            {
                                                0: BuildableItemLevelInfo(0, 100, 50, 0, 0, 0, 0, 1200, 10, 0, 0, [], 0),
                                                1: BuildableItemLevelInfo(1, 50, 10, 0, 1, 2, 0, 10, 500, 0, 0, [], 0),

                                                2: BuildableItemLevelInfo(2, 100, 150, 0, 0.03, 4, 0, 1200, 500, 0, 0,
                                                                          [], 1),

                                                3: BuildableItemLevelInfo(3, 150, 170, 0, 0.06, 6, 0, 1600, 800, 0, 50,
                                                                          [], 1),
                                                4: BuildableItemLevelInfo(4, 200, 250, 0, 0.07, 8, 0, 1800, 900, 0, 60,
                                                                          [], 1),
                                                5: BuildableItemLevelInfo(5, 250, 300, 0, 0.08, 10, 0, 1900, 1000, 0,
                                                                          70,
                                                                          [], 1),
                                                6: BuildableItemLevelInfo(6, 300, 400, 0, 0.09, 12, 0, 2000, 1100, 0,
                                                                          80,
                                                                          [], 1),

                                                7: BuildableItemLevelInfo(7, 350, 500, 0, 0.10, 14, 0, 2200, 1200, 0,
                                                                          90,
                                                                          [], 1),
                                                8: BuildableItemLevelInfo(8, 500, 600, 0, 0.12, 16, 0, 2400, 1300, 0,
                                                                          100,
                                                                          [], 1),
                                                9: BuildableItemLevelInfo(9, 670, 800, 0, 0.13, 18, 0, 2600, 1400, 0,
                                                                          110,
                                                                          [], 1),
                                                10: BuildableItemLevelInfo(10, 1000, 1500, 0, 0.14, 20, 0, 2800, 1500, 0,
                                                                           120,
                                                                           [], 1),
                                            }
                                            ),

        PETROL_MINE: BuildableItemBaseType("Petrol Mine", PETROL_MINE, TYPE, MINE_CATEGORY, "Petrol mine to extract metal",
                                           {
                                               0: BuildableItemLevelInfo(0, 100, 10, 60, 0, 0, 0, 1200, 10, 0, 0, [], 0),
                                               1: BuildableItemLevelInfo(1, 40, 10, 30, 1, 5, 0, 10, 500, 0, 0, [], 0),
                                               2: BuildableItemLevelInfo(2, 100, 150, 80, 0.03, 40, 0, 1200, 500, 0, 0,
                                                                         [], 1),

                                               3: BuildableItemLevelInfo(3, 150, 170, 10, 0.06, 60, 0, 1600, 800, 0, 50,
                                                                         [], 1),
                                               4: BuildableItemLevelInfo(4, 200, 250, 50, 0.07, 80, 0, 1800, 900, 0, 60,
                                                                         [], 1),
                                               5: BuildableItemLevelInfo(5, 250, 300, 60, 0.08, 90, 0, 1900, 1000, 0,
                                                                         70,
                                                                         [], 1),
                                               6: BuildableItemLevelInfo(6, 300, 400, 70, 0.09, 100, 0, 2000, 1100, 0,
                                                                         80,
                                                                         [], 1),

                                               7: BuildableItemLevelInfo(7, 350, 500, 80, 0.10, 120, 0, 2200, 1200, 0,
                                                                         90,
                                                                         [], 1),
                                               8: BuildableItemLevelInfo(8, 500, 600, 90, 0.12, 140, 0, 2400, 1300, 0,
                                                                         100,
                                                                         [], 1),
                                               9: BuildableItemLevelInfo(9, 670, 800, 100, 0.13, 180, 0, 2600, 1400, 0,
                                                                         110,
                                                                         [], 1),
                                               10: BuildableItemLevelInfo(10, 1000, 100, 120, 0.14, 200, 0, 2800, 1500, 0,
                                                                          120,
                                                                          [], 1),
                                           }
                                           ),

        METAL_WAREHOUSE: BuildableItemBaseType("Metal Warehouse", METAL_WAREHOUSE, TYPE, WAREHOUSE_CATEGORY,
                                               "Metal warehouse to store metal",
                                               {
                                                   0: BuildableItemLevelInfo(0, 100, 50, 60, 0, 0, 200, 1200, 10, 0, 0, [],
                                                                             0),
                                                   1: BuildableItemLevelInfo(1, 30, 10, 20, 0, 0, 500, 10, 30, 0, 0, [],
                                                                             0),

                                                   2: BuildableItemLevelInfo(2, 140, 300, 90, 0, 0, 700, 30, 100, 0, 0, [],
                                                                             0),
                                                   3: BuildableItemLevelInfo(3, 180, 350, 100, 0, 0, 900, 60, 150, 0, 0, [],
                                                                             0),
                                                   4: BuildableItemLevelInfo(4, 250, 450, 150, 0, 0, 2000, 120, 200, 0, 0, [],
                                                                             0),
                                                   5: BuildableItemLevelInfo(5, 3000, 600, 600, 0, 0, 4000, 1000, 500, 0, 0, [],
                                                                             0),
                                                   6: BuildableItemLevelInfo(6, 3500, 700, 650, 0, 0, 4100, 1300, 600, 0, 0, [],
                                                                             0),
                                                   7: BuildableItemLevelInfo(7, 4000, 800, 900, 0, 0, 4500, 1800, 600, 0, 0, [],
                                                                             0),
                                                   8: BuildableItemLevelInfo(8, 5000, 1000, 1000, 0, 0, 5000, 2000, 800, 0, 0, [],
                                                                             0),

                                                   9: BuildableItemLevelInfo(9, 100, 0, 60, 0, 0, 500, 2500, 900, 0, 0, [],
                                                                             0),

                                                   10: BuildableItemLevelInfo(10, 100, 0, 60, 0, 0, 500, 3500, 900, 0, 0, [],
                                                                             0),

                                               }
                                               ),

        CRYSTAL_WAREHOUSE: BuildableItemBaseType("Crystal Warehouse", CRYSTAL_WAREHOUSE, TYPE, WAREHOUSE_CATEGORY,
                                                 "Crystal warehouse to store crystal",
                                                 {
                                                     0: BuildableItemLevelInfo(0, 100, 50, 60, 0, 0, 150, 1200, 10, 0, 0,
                                                                               [],
                                                                               0),
                                                     1: BuildableItemLevelInfo(1, 30, 10, 20, 0, 0, 500, 10, 30, 0, 0,
                                                                               [],
                                                                               0),

                                                     2: BuildableItemLevelInfo(2, 140, 300, 90, 0, 0, 700, 30, 100, 0,
                                                                               0, [],
                                                                               0),
                                                     3: BuildableItemLevelInfo(3, 180, 350, 100, 0, 0, 900, 60, 150, 0,
                                                                               0, [],
                                                                               0),
                                                     4: BuildableItemLevelInfo(4, 250, 450, 150, 0, 0, 2000, 120, 200,
                                                                               0, 0, [],
                                                                               0),
                                                     5: BuildableItemLevelInfo(5, 3000, 600, 600, 0, 0, 4000, 1000, 500,
                                                                               0, 0, [],
                                                                               0),
                                                     6: BuildableItemLevelInfo(6, 3500, 700, 650, 0, 0, 4100, 1300, 600,
                                                                               0, 0, [],
                                                                               0),
                                                     7: BuildableItemLevelInfo(7, 4000, 800, 900, 0, 0, 4500, 1800, 600,
                                                                               0, 0, [],
                                                                               0),
                                                     8: BuildableItemLevelInfo(8, 5000, 1000, 1000, 0, 0, 5000, 2000,
                                                                               800, 0, 0, [],
                                                                               0),

                                                     9: BuildableItemLevelInfo(9, 100, 0, 60, 0, 0, 500, 2500, 900, 0,
                                                                               0, [],
                                                                               0),

                                                     10: BuildableItemLevelInfo(10, 100, 0, 60, 0, 0, 500, 3500, 900, 0,
                                                                                0, [],
                                                                                0),
                                                 }
                                                 ),
        PETROL_WAREHOUSE: BuildableItemBaseType("Petrol Warehouse", PETROL_WAREHOUSE, TYPE, WAREHOUSE_CATEGORY,
                                                "Petrol warehouse to store petrol",
                                                {
                                                    0: BuildableItemLevelInfo(0, 100, 50, 60, 0, 0, 300, 1200, 10, 0, 0,
                                                                              [],
                                                                              0),
                                                    1: BuildableItemLevelInfo(1, 30, 10, 20, 0, 0, 500, 10, 30, 0, 0,
                                                                              [],
                                                                              0),

                                                    2: BuildableItemLevelInfo(2, 140, 300, 90, 0, 0, 700, 30, 100, 0, 0,
                                                                              [],
                                                                              0),
                                                    3: BuildableItemLevelInfo(3, 180, 350, 100, 0, 0, 900, 60, 150, 0,
                                                                              0, [],
                                                                              0),
                                                    4: BuildableItemLevelInfo(4, 250, 450, 150, 0, 0, 2000, 120, 200, 0,
                                                                              0, [],
                                                                              0),
                                                    5: BuildableItemLevelInfo(5, 3000, 600, 600, 0, 0, 4000, 1000, 500,
                                                                              0, 0, [],
                                                                              0),
                                                    6: BuildableItemLevelInfo(6, 3500, 700, 650, 0, 0, 4100, 1300, 600,
                                                                              0, 0, [],
                                                                              0),
                                                    7: BuildableItemLevelInfo(7, 4000, 800, 900, 0, 0, 4500, 1800, 600,
                                                                              0, 0, [],
                                                                              0),
                                                    8: BuildableItemLevelInfo(8, 5000, 1000, 1000, 0, 0, 5000, 2000,
                                                                              800, 0, 0, [],
                                                                              0),

                                                    9: BuildableItemLevelInfo(9, 100, 0, 60, 0, 0, 500, 2500, 900, 0, 0,
                                                                              [],
                                                                              0),

                                                    10: BuildableItemLevelInfo(10, 100, 0, 60, 0, 0, 500, 3500, 900, 0,
                                                                               0, [],
                                                                               0),
                                                }
                                                )
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
            raise ValueError(f"{key} not in {ResourceData.TYPES} for {ResourceData.TYPE}")

        return ResourceData.__ITEMS[key]
