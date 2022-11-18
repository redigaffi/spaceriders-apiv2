from .Common import CommonKeys as CK


class AccountLevelData:
    LEVEL = {
        1: {
            CK.EXPERIENCE: 2021,
            CK.REWARDS: {},
        },
        2: {
            CK.EXPERIENCE: 4042,
            CK.REWARDS: {},
        },
        3: {
            CK.EXPERIENCE: 6063,
            CK.REWARDS: {},
        },
        4: {
            CK.EXPERIENCE: 8084,
            CK.REWARDS: {},
        },
        5: {
            CK.EXPERIENCE: 10105,
            CK.REWARDS: {},
        },
        6: {
            CK.EXPERIENCE: 12126,
            CK.REWARDS: {},
        },
        7: {
            CK.EXPERIENCE: 14147,
            CK.REWARDS: {},
        },
        8: {
            CK.EXPERIENCE: 16168,
            CK.REWARDS: {},
        },
        9: {
            CK.EXPERIENCE: 18189,
            CK.REWARDS: {},
        },
        10: {
            CK.EXPERIENCE: 20210,
            CK.REWARDS: {},
        },
        11: {
            CK.EXPERIENCE: 22231,
            CK.REWARDS: {}
        },
        12: {
            CK.EXPERIENCE: 24252,
            CK.REWARDS: {},
        },
        13: {
            CK.EXPERIENCE: 26273,
            CK.REWARDS: {},
        },
        14: {
            CK.EXPERIENCE: 28294,
            CK.REWARDS: {},
        },
        15: {
            CK.EXPERIENCE: 30315,
            CK.REWARDS: {},
        },
    }

    @staticmethod
    def get_level_experience(level: int):
        return list(AccountLevelData.LEVEL.values())[level][CK.EXPERIENCE]

