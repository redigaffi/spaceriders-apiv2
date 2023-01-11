from dataclasses import dataclass
from .Common import CommonKeys as CK


@dataclass
class DailyLoginRewardsData:
    REWARDS_BY_DAY = {
        1: {
            CK.METAL: 100,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 2000,
        },
         2: {
            CK.METAL: 150,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 2250,
        },
         3: {
            CK.METAL: 200,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 2500,
        },
         4: {
            CK.METAL: 250,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 2750,
        },
         5: {
            CK.METAL: 300,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 3000,
        },
         6: {
            CK.METAL: 350,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 3250,
        },
         7: {
            CK.METAL: 400,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 3500,
        },
         8: {
            CK.METAL: 450,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 3750,
        },
         9: {
            CK.METAL: 500,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 4000,
        },
         10: {
            CK.METAL: 550,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 4250,
        },
          11: {
            CK.METAL: 600,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 4500,
        },
          12: {
            CK.METAL: 650,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 4750,
        },
          13: {
            CK.METAL: 700,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 5000,
        },
          14: {
            CK.METAL: 750,
            CK.CRYSTAL: 0,
            CK.PETROL: 0,
            CK.ENERGY: 5250,
        },
          15: {
            CK.METAL: 800,
            CK.CRYSTAL: 220,
            CK.PETROL: 0,
            CK.ENERGY: 5500,
        },
          16: {
            CK.METAL: 850,
            CK.CRYSTAL: 360,
            CK.PETROL: 0,
            CK.ENERGY: 5750,
        },
          17: {
            CK.METAL: 900,
            CK.CRYSTAL: 500,
            CK.PETROL: 0,
            CK.ENERGY: 6000,
        },
          18: {
            CK.METAL: 950,
            CK.CRYSTAL: 640,
            CK.PETROL: 0,
            CK.ENERGY: 6250,
        },
          19: {
            CK.METAL: 1000,
            CK.CRYSTAL: 780,
            CK.PETROL: 0,
            CK.ENERGY: 6500,
        },
        20: {
            CK.METAL: 1050,
            CK.CRYSTAL: 920,
            CK.PETROL: 0,
            CK.ENERGY: 6750,
        },
        21: {
            CK.METAL: 1100,
            CK.CRYSTAL: 1060,
            CK.PETROL: 0,
            CK.ENERGY: 7000,
        },
         22: {
            CK.METAL: 1150,
            CK.CRYSTAL: 1200,
            CK.PETROL: 320,
            CK.ENERGY: 7250,
        },
         23: {
            CK.METAL: 1200,
            CK.CRYSTAL: 1340,
            CK.PETROL: 650,
            CK.ENERGY: 7500,
        },
         24: {
            CK.METAL: 1250,
            CK.CRYSTAL: 1480,
            CK.PETROL: 980,
            CK.ENERGY: 7750,
        },
         25: {
            CK.METAL: 1300,
            CK.CRYSTAL: 1620,
            CK.PETROL: 1310,
            CK.ENERGY: 8000,
        },
         26: {
            CK.METAL: 1350,
            CK.CRYSTAL: 1760,
            CK.PETROL: 1640,
            CK.ENERGY: 8250,
        },
         27: {
            CK.METAL: 1400,
            CK.CRYSTAL: 1900,
            CK.PETROL: 1970,
            CK.ENERGY: 8500,
        },
        28: {
            CK.METAL: 1450,
            CK.CRYSTAL: 2040,
            CK.PETROL: 2300,
            CK.ENERGY: 8750,
        },
        29: {
            CK.METAL: 1500,
            CK.CRYSTAL: 2180,
            CK.PETROL: 2630,
            CK.ENERGY: 9000,
        },
         30: {
            CK.METAL: 1550,
            CK.CRYSTAL: 2320,
            CK.PETROL: 2960,
            CK.ENERGY: 9250,
        },
    }

    @staticmethod
    def daily_reward_amount():
        return 30

    @staticmethod
    def get_rewards_by_day(day: int):
        return DailyLoginRewardsData.REWARDS_BY_DAY[day % DailyLoginRewardsData.daily_reward_amount()]

