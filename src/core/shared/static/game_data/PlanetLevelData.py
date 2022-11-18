from .Common import CommonKeys as CK


class PlanetLevelData:
    LEVEL = {
        1: {
            CK.EXPERIENCE: 404.2,
            CK.REWARDS: {},
        },
        2: {
            CK.EXPERIENCE: 808.4,
            CK.REWARDS: {},
        },
        3: {
            CK.EXPERIENCE: 1212.6,
            CK.REWARDS: {},
        },
        4: {
            CK.EXPERIENCE: 1616.8,
            CK.REWARDS: {},
        },
        5: {
            CK.EXPERIENCE: 2021,
            CK.REWARDS: {},
        },
        6: {
            CK.EXPERIENCE: 2425.2,
            CK.REWARDS: {},
        },
        7: {
            CK.EXPERIENCE: 2829.4,
            CK.REWARDS: {},
        },
        8: {
            CK.EXPERIENCE: 3233.6,
            CK.REWARDS: {},
        },
        9: {
            CK.EXPERIENCE: 3637.8,
            CK.REWARDS: {},
        },
        10: {
            CK.EXPERIENCE: 4042,
            CK.REWARDS: {},
        },
        11: {
            CK.EXPERIENCE: 4446.2,
            CK.REWARDS: {}
        },
        12: {
            CK.EXPERIENCE: 4850.4,
            CK.REWARDS: {},
        },
        13: {
            CK.EXPERIENCE: 5254.6,
            CK.REWARDS: {},
        },
        14: {
            CK.EXPERIENCE: 5658.8,
            CK.REWARDS: {},
        },
        15: {
            CK.EXPERIENCE: 6063,
            CK.REWARDS: {},
        },
    }

    @staticmethod
    def get_level_experience(level: int):
        return PlanetLevelData.LEVEL[level][CK.EXPERIENCE]

    @staticmethod
    def get_level_rewards(level):
        return PlanetLevelData.LEVEL[level][CK.REWARDS]
