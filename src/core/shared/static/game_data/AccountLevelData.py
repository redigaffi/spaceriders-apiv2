from .Common import CommonKeys as CK


class AccountLevelData:
    LEVEL = {
        1: {
            CK.EXPERIENCE: 400,
            CK.REWARDS: {},
        },
        2: {
            CK.EXPERIENCE: 600,
            CK.REWARDS: {},
        },
        3: {
            CK.EXPERIENCE: 1000,
            CK.REWARDS: {},
        },
        4: {
            CK.EXPERIENCE: 1400,
            CK.REWARDS: {},
        },
        5: {
            CK.EXPERIENCE: 2600,
            CK.REWARDS: {},
        },
        6: {
            CK.EXPERIENCE: 4000,
            CK.REWARDS: {},
        },
        7: {
            CK.EXPERIENCE: 8000,
            CK.REWARDS: {},
        },
        8: {
            CK.EXPERIENCE: 14000,
            CK.REWARDS: {},
        },
        9: {
            CK.EXPERIENCE: 20000,
            CK.REWARDS: {},
        },
        10: {
            CK.EXPERIENCE: 25000,
            CK.REWARDS: {},
        },
        11: {
            CK.EXPERIENCE: 35000,
            CK.REWARDS: {}
        },
        12: {
            CK.EXPERIENCE: 50000,
            CK.REWARDS: {},
        },
        13: {
            CK.EXPERIENCE: 60000,
            CK.REWARDS: {},
        },
        14: {
            CK.EXPERIENCE: 75000,
            CK.REWARDS: {},
        },
        15: {
            CK.EXPERIENCE: 100000,
            CK.REWARDS: {},
        },
    }

    @staticmethod
    def get_level_experience(level: int):
        return list(AccountLevelData.LEVEL.values())[level][CK.EXPERIENCE]

