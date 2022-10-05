from dataclasses import dataclass

from .Common import BuildableItemBaseType, BuildableItemLevelInfo
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
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    1, 100, 0, 60, 0, 0, 0, 1200, 0, 0, 10, [], 0
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
                    1, 100, 0, 60, 0, 0, 0, 1200, 0, 0, 10, [], 0
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
