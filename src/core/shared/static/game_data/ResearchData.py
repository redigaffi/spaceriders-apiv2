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
                    100,
                    0,
                    60,
                    0,
                    0,
                    0,
                    1200,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 2)],
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
                    100,
                    0,
                    60,
                    0,
                    0,
                    0,
                    1200,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)],
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
                    1,
                    100,
                    0,
                    60,
                    0,
                    0,
                    0,
                    1200,
                    0,
                    0,
                    10,
                    [BuildableItemRequirement(ID.TYPE, ID.INVESTIGATION_LABORATORY, 3)],
                    0,
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
