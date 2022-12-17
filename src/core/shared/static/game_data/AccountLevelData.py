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
            CK.REWARDS: {},
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
        16: {
            CK.EXPERIENCE: 36233,
            CK.REWARDS: {},
        },
        17: {
            CK.EXPERIENCE: 42151,
            CK.REWARDS: {},
        },
        18: {
            CK.EXPERIENCE: 48069,
            CK.REWARDS: {},
        },
        19: {
            CK.EXPERIENCE: 53987,
            CK.REWARDS: {},
        },
        20: {
            CK.EXPERIENCE: 59905,
            CK.REWARDS: {},
        },
        21: {
            CK.EXPERIENCE: 65822,
            CK.REWARDS: {},
        },
        22: {
            CK.EXPERIENCE: 71740,
            CK.REWARDS: {},
        },
        23: {
            CK.EXPERIENCE: 77658,
            CK.REWARDS: {},
        },
        24: {
            CK.EXPERIENCE: 83576,
            CK.REWARDS: {},
        },
        25: {
            CK.EXPERIENCE: 89494,
            CK.REWARDS: {},
        },
        26: {
            CK.EXPERIENCE: 661367,
            CK.REWARDS: {},
        },
        27: {
            CK.EXPERIENCE: 1233240,
            CK.REWARDS: {},
        },
        28: {
            CK.EXPERIENCE: 1805113,
            CK.REWARDS: {},
        },
        29: {
            CK.EXPERIENCE: 2376986,
            CK.REWARDS: {},
        },
        30: {
            CK.EXPERIENCE: 2948859,
            CK.REWARDS: {},
        },
        31: {
            CK.EXPERIENCE: 3520731,
            CK.REWARDS: {},
        },
        32: {
            CK.EXPERIENCE: 4092604,
            CK.REWARDS: {},
        },
        33: {
            CK.EXPERIENCE: 4664477,
            CK.REWARDS: {},
        },
        34: {
            CK.EXPERIENCE: 5236350,
            CK.REWARDS: {},
        },
        35: {
            CK.EXPERIENCE: 5808223,
            CK.REWARDS: {},
        },
        36: {
            CK.EXPERIENCE: 6185073,
            CK.REWARDS: {},
        },
        37: {
            CK.EXPERIENCE: 6561923,
            CK.REWARDS: {},
        },
        38: {
            CK.EXPERIENCE: 6938773,
            CK.REWARDS: {},
        },
        39: {
            CK.EXPERIENCE: 7315623,
            CK.REWARDS: {},
        },
        40: {
            CK.EXPERIENCE: 7692473,
            CK.REWARDS: {},
        },
        41: {
            CK.EXPERIENCE: 8069323,
            CK.REWARDS: {},
        },
        42: {
            CK.EXPERIENCE: 8446173,
            CK.REWARDS: {},
        },
        43: {
            CK.EXPERIENCE: 8823023,
            CK.REWARDS: {},
        },
        44: {
            CK.EXPERIENCE: 9199873,
            CK.REWARDS: {},
        },
        45: {
            CK.EXPERIENCE: 9576723,
            CK.REWARDS: {},
        },
        46: {
            CK.EXPERIENCE: 9953573,
            CK.REWARDS: {},
        },
        47: {
            CK.EXPERIENCE: 10330423,
            CK.REWARDS: {},
        },
        48: {
            CK.EXPERIENCE: 10707273,
            CK.REWARDS: {},
        },
        49: {
            CK.EXPERIENCE: 11084123,
            CK.REWARDS: {},
        },
        50: {
            CK.EXPERIENCE: 11460973,
            CK.REWARDS: {},
        }
    }

    @staticmethod
    def get_max_level():
        return 50

    @staticmethod
    def get_level_experience(level: int):
        return list(AccountLevelData.LEVEL.values())[level][CK.EXPERIENCE]

