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
                                              1: BuildableItemLevelInfo(1, 100, 0, 60, 0.01, 5, 0, 10, 500, 0, 500, [], 1),
                                              2: BuildableItemLevelInfo(2, 100, 0, 60, 1, 5, 0, 1200, 500, 0, 0, [], 1),
                                          }
                                          ),

        CRYSTAL_MINE: BuildableItemBaseType("Crystal Mine", CRYSTAL_MINE, TYPE, MINE_CATEGORY,  "Crystal mine to extract metal",
                                            {
                                                0: BuildableItemLevelInfo(0, 100, 0, 60, 0, 0, 0, 1200, 10, 0, 0, [], 0),
                                                1: BuildableItemLevelInfo(1, 100, 0, 60, 1, 5, 0, 1200, 500, 0, 0, [], 0),
                                            }
                                            ),

        PETROL_MINE: BuildableItemBaseType("Petrol Mine", PETROL_MINE, TYPE, MINE_CATEGORY, "Petrol mine to extract metal",
                                           {
                                               0: BuildableItemLevelInfo(0, 100, 0, 60, 0, 0, 0, 1200, 10, 0, 0, [], 0),
                                               1: BuildableItemLevelInfo(1, 100, 0, 60, 1, 5, 0, 1200, 500, 0, 0, [], 0),
                                           }
                                           ),

        METAL_WAREHOUSE: BuildableItemBaseType("Metal Warehouse", METAL_WAREHOUSE, TYPE, WAREHOUSE_CATEGORY,
                                               "Metal warehouse to store metal",
                                               {
                                                   0: BuildableItemLevelInfo(0, 100, 0, 60, 0, 0, 0, 1200, 10, 0, 0, [],
                                                                             0),
                                                   1: BuildableItemLevelInfo(1, 100, 0, 60, 0, 0, 500, 10, 10, 0, 0, [],
                                                                             0),
                                               }
                                               ),

        CRYSTAL_WAREHOUSE: BuildableItemBaseType("Crystal Warehouse", CRYSTAL_WAREHOUSE, TYPE, WAREHOUSE_CATEGORY,
                                                 "Crystal warehouse to store crystal",
                                                 {
                                                     0: BuildableItemLevelInfo(0, 100, 0, 60, 0, 0, 0, 1200, 10, 0, 0,
                                                                               [],
                                                                               0),
                                                     1: BuildableItemLevelInfo(1, 100, 0, 60, 0, 0, 500, 1200, 10, 0, 0,
                                                                               [],
                                                                               0),
                                                 }
                                                 ),
        PETROL_WAREHOUSE: BuildableItemBaseType("Petrol Warehouse", PETROL_WAREHOUSE, TYPE, WAREHOUSE_CATEGORY,
                                                "Petrol warehouse to store petrol",
                                                {
                                                    0: BuildableItemLevelInfo(0, 100, 0, 60, 0, 0, 0, 1200, 10, 0, 0, [],
                                                                              0),
                                                    1: BuildableItemLevelInfo(1, 100, 0, 60, 0, 0, 500, 1200, 10, 0, 0,
                                                                              [],
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
