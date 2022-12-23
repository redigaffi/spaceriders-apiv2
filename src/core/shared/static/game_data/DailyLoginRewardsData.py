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
         2: {
            CK.METAL: 150,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
         3: {
            CK.METAL: 200,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
         4: {
            CK.METAL: 250,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
         5: {
            CK.METAL: 300,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
         6: {
            CK.METAL: 350,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
         7: {
            CK.METAL: 400,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 0,
        },
         8: {
            CK.METAL: 450,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 120,
        },
         9: {
            CK.METAL: 500,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 200,
        },
         10: {
            CK.METAL: 550,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 280,
        },
          11: {
            CK.METAL: 600,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 360,
        },
          12: {
            CK.METAL: 650,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 440,
        },
          13: {
            CK.METAL: 700,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 520,
        },
          14: {
            CK.METAL: 750,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 600,
        },
          15: {
            CK.METAL: 800,
            CK.CRYSTAL: 220,
            CK.PETROL: 0,
            CK.ENERGY: 680,
        },
          16: {
            CK.METAL: 850,
            CK.CRYSTAL: 360,
            CK.PETROL: 0,
            CK.ENERGY: 760,
        },
          17: {
            CK.METAL: 900,
            CK.CRYSTAL: 500,
            CK.PETROL: 0,
            CK.ENERGY: 840,
        },
          18: {
            CK.METAL: 950,
            CK.CRYSTAL: 640,
            CK.PETROL: 0,
            CK.ENERGY: 920,
        },
          19: {
            CK.METAL: 1000,
            CK.CRYSTAL: 780,
            CK.PETROL: 0,
            CK.ENERGY: 1000,
        },
        20: {
            CK.METAL: 1050,
            CK.CRYSTAL: 920,
            CK.PETROL: 0,
            CK.ENERGY: 1080,
        },
        21: {
            CK.METAL: 1100,
            CK.CRYSTAL: 1060,
            CK.PETROL: 0,
            CK.ENERGY: 1160,
        },
         22: {
            CK.METAL: 1150,
            CK.CRYSTAL: 1200,
            CK.PETROL: 320,
            CK.ENERGY: 1240,
        },
         23: {
            CK.METAL: 1200,
            CK.CRYSTAL: 1340,
            CK.PETROL: 650,
            CK.ENERGY: 1320,
        },
         24: {
            CK.METAL: 1250,
            CK.CRYSTAL: 1480,
            CK.PETROL: 980,
            CK.ENERGY: 1400,
        },
         25: {
            CK.METAL: 1300,
            CK.CRYSTAL: 1620,
            CK.PETROL: 1310,
            CK.ENERGY: 1480,
        },
         26: {
            CK.METAL: 1350,
            CK.CRYSTAL: 1760,
            CK.PETROL: 1640,
            CK.ENERGY: 1560,
        },
         27: {
            CK.METAL: 1400,
            CK.CRYSTAL: 1900,
            CK.PETROL: 1970,
            CK.ENERGY: 1640,
        },
        28: {
            CK.METAL: 1450,
            CK.CRYSTAL: 2040,
            CK.PETROL: 2300,
            CK.ENERGY: 1720,
        },
        29: {
            CK.METAL: 1500,
            CK.CRYSTAL: 2180,
            CK.PETROL: 2630,
            CK.ENERGY: 1800,
        },
         30: {
            CK.METAL: 1550,
            CK.CRYSTAL: 2320,
            CK.PETROL: 2960,
            CK.ENERGY: 1880,
        },
    }

    @staticmethod
    def daily_reward_amount():
        return 30

    @staticmethod
    def get_rewards_by_day(day: int):
        return DailyLoginRewardsData.REWARDS_BY_DAY[day % DailyLoginRewardsData.daily_reward_amount()]

