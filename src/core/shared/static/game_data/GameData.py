from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.shared.static.game_data.Common import BuildableItemBaseType


class GameData(ABC):
    @staticmethod
    @abstractmethod
    def valid_type(label: str) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def get_type() -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_item(key: str) -> BuildableItemBaseType:
        pass
