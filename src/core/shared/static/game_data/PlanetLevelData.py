from .Common import CommonKeys as CK


class PlanetLevelData:
    LEVEL = {
        1: {
            CK.EXPERIENCE: 200,
            CK.REWARDS: {},
        },
        2: {
            CK.EXPERIENCE: 400,
            CK.REWARDS: {},
        },
        3: {
            CK.EXPERIENCE: 800,
            CK.REWARDS: {},
        },
        4: {
            CK.EXPERIENCE: 1200,
            CK.REWARDS: {},
        },
        5: {
            CK.EXPERIENCE: 2400,
            CK.REWARDS: {},
        },
        6: {
            CK.EXPERIENCE: 3000,
            CK.REWARDS: {},
        },
        7: {
            CK.EXPERIENCE: 7500,
            CK.REWARDS: {},
        },
        8: {
            CK.EXPERIENCE: 8000,
            CK.REWARDS: {},
        },
        9: {
            CK.EXPERIENCE: 10000,
            CK.REWARDS: {},
        },
        10: {
            CK.EXPERIENCE: 15000,
            CK.REWARDS: {},
        },
        11: {
            CK.EXPERIENCE: 30000,
            CK.REWARDS: {}
        },
        12: {
            CK.EXPERIENCE: 60000,
            CK.REWARDS: {},
        },
        13: {
            CK.EXPERIENCE: 90000,
            CK.REWARDS: {},
        },
        14: {
            CK.EXPERIENCE: 120000,
            CK.REWARDS: {},
        },
        15: {
            CK.EXPERIENCE: 150000,
            CK.REWARDS: {},
        },
    }

    @staticmethod
    def get_level_experience(level: int):
        return PlanetLevelData.LEVEL[level][CK.EXPERIENCE]

    @staticmethod
    def get_level_rewards(level):
        return PlanetLevelData.LEVEL[level][CK.REWARDS]
