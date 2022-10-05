from core.shared.static.game_data.DefenseData import DefenseData
from core.shared.static.game_data.GameData import GameData
from core.shared.static.game_data.InstallationData import InstallationData
from core.shared.static.game_data.ResearchData import ResearchData
from core.shared.static.game_data.ResourceData import ResourceData

game_data_factory: dict[str, GameData] = {
    ResourceData.TYPE: ResourceData,
    InstallationData.TYPE: InstallationData,
    ResearchData.TYPE: ResearchData,
    DefenseData.TYPE: DefenseData,
}
