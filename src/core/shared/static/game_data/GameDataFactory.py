from src.core.shared.static.game_data.GameData import GameData
from src.core.shared.static.game_data.ResourceData import ResourceData
from src.core.shared.static.game_data.DefenseData import DefenseData
from src.core.shared.static.game_data.InstallationData import InstallationData
from src.core.shared.static.game_data.ResearchData import ResearchData

game_data_factory: dict[str, GameData] = {
    ResourceData.TYPE: ResourceData,
    InstallationData.TYPE: InstallationData,
    ResearchData.TYPE: ResearchData,
    DefenseData.TYPE: DefenseData,
}