from dataclasses import dataclass
from .Common import CommonKeys as CK


@dataclass
class DailyLoginRewardsData:
    REWARDS_BY_DAY = {
        1: {
            CK.METAL: 100,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
    }

    @staticmethod
    def daily_reward_amount():
        return 30

    @staticmethod
    def get_rewards_by_day(day: int):
        return DailyLoginRewardsData.REWARDS_BY_DAY[day % DailyLoginRewardsData.daily_reward_amount()]

