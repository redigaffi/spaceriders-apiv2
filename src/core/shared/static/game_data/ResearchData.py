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
                    1,
                    700,
                    1400,
                    860,
                    0,
                    0,
                    0,
                    900,
                    0,
                    0,
                    925,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 1)],
                    0,
                ),
                2: BuildableItemLevelInfo(
                    2,
                    953,
                    1907,
                    1171,
                    0,
                    0,
                    0,
                    1407,
                    0,
                    0,
                    1260,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
                    0,
                ),
                3: BuildableItemLevelInfo(
                    3,
                    1275,
                    2551,
                    1567,
                    0,
                    0,
                    0,
                    2135,
                    0,
                    0,
                    1686,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)],
                    0,
                ),
                4: BuildableItemLevelInfo(
                    4,
                    1675,
                    3351,
                    2058,
                    0,
                    0,
                    0,
                    3141,
                    0,
                    0,
                    2214,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 4)],
                    0,
                ),
                5: BuildableItemLevelInfo(
                    5,
                    2160,
                    4320,
                    2654,
                    0,
                    0,
                    0,
                    4477,
                    0,
                    0,
                    2855,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 5)],
                    0,
                ),
                6: BuildableItemLevelInfo(
                    6,
                    600,
                    1050,
                    750,
                    0,
                    0,
                    0,
                    2200,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 6)],
                    0,
                ),
                7: BuildableItemLevelInfo(
                    7,
                    700,
                    1150,
                    850,
                    0,
                    0,
                    0,
                    2400,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 7)],
                    0,
                ),
                8: BuildableItemLevelInfo(
                    8,
                    800,
                    1250,
                    950,
                    0,
                    0,
                    0,
                    2600,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 8)],
                    0,
                ),
                9: BuildableItemLevelInfo(
                    9,
                    900,
                    1350,
                    1050,
                    0,
                    0,
                    0,
                    2800,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 9)],
                    0,
                ),
                10: BuildableItemLevelInfo(
                    10,
                    1000,
                    1450,
                    1150,
                    0,
                    0,
                    0,
                    3000,
                    0,
                    0,
                    10,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 10
                        )
                    ],
                    0,
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
                    1,
                    500,
                    500,
                    500,
                    0,
                    0,
                    0,
                    2000,
                    0,
                    0,
                    20,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
                    0,
                ),
                2: BuildableItemLevelInfo(
                    2,
                    1000,
                    800,
                    600,
                    0,
                    0,
                    0,
                    3000,
                    0,
                    0,
                    30,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 4)],
                    0,
                ),
                3: BuildableItemLevelInfo(
                    3,
                    2000,
                    1100,
                    700,
                    0,
                    0,
                    0,
                    4000,
                    0,
                    0,
                    40,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 6)],
                    0,
                ),
                4: BuildableItemLevelInfo(
                    4,
                    3000,
                    1400,
                    800,
                    0,
                    0,
                    0,
                    5000,
                    0,
                    0,
                    50,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 8)],
                    0,
                ),
                5: BuildableItemLevelInfo(
                    5,
                    4000,
                    1700,
                    900,
                    0,
                    0,
                    0,
                    6000,
                    0,
                    0,
                    60,
                    [
                        BuildableItemRequirement(
                            ID.TYPE, ID.INVESTIGATION_LABORATORY, 10
                        )
                    ],
                    0,
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
                    lvl=1, experience=1412, health=2750, time=2000, cost_metal=2000, cost_crystal=1000,
                    cost_petrol=2000,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    lvl=2, experience=2232, health=3196, time=3437, cost_metal=3163, cost_crystal=1582,
                    cost_petrol=3163,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    lvl=3, experience=3402, health=3877, time=5512, cost_metal=4821, cost_crystal=2410,
                    cost_petrol=4821,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    lvl=4, experience=4990, health=4875, time=8212, cost_metal=7071, cost_crystal=3535,
                    cost_petrol=7071,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    lvl=5, experience=10931, health=7061, time=12175, cost_metal=10326, cost_crystal=5163,
                    cost_petrol=10326,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    lvl=6, experience=15896, health=10240, time=17965, cost_metal=15015, cost_crystal=7508,
                    cost_petrol=15015,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    lvl=7, experience=23014, health=14843, time=26382, cost_metal=21740, cost_crystal=10870,
                    cost_petrol=21740,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    lvl=8, experience=33177, health=21479, time=38556, cost_metal=31340, cost_crystal=15670,
                    cost_petrol=31340,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    lvl=9, experience=65440, health=34567, time=62051, cost_metal=46362, cost_crystal=23181,
                    cost_petrol=46362,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    lvl=10, experience=222496, health=79066, time=122919, cost_metal=78815, cost_crystal=39408,
                    cost_petrol=78815,
                    energy_usage=0, production=0, capacity=0, attack=0, requirements=[], has_discount=0
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
