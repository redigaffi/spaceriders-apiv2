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
            CK.EXPERIENCE: 2021.0,
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
            CK.EXPERIENCE: 4042.0,
            CK.REWARDS: {},
        },
        11: {
            CK.EXPERIENCE: 4446.2,
            CK.REWARDS: {},
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
            CK.EXPERIENCE: 6063.0,
            CK.REWARDS: {},
        },
        16: {
            CK.EXPERIENCE: 7246.6,
            CK.REWARDS: {},
        },
        17: {
            CK.EXPERIENCE: 8430.2,
            CK.REWARDS: {},
        },
        18: {
            CK.EXPERIENCE: 9613.8,
            CK.REWARDS: {},
        },
        19: {
            CK.EXPERIENCE: 10797.4,
            CK.REWARDS: {},
        },
        20: {
            CK.EXPERIENCE: 11981.0,
            CK.REWARDS: {},
        },
        21: {
            CK.EXPERIENCE: 13164.4,
            CK.REWARDS: {},
        },
        22: {
            CK.EXPERIENCE: 14348.0,
            CK.REWARDS: {},
        },
        23: {
            CK.EXPERIENCE: 15531.6,
            CK.REWARDS: {},
        },
        24: {
            CK.EXPERIENCE: 16715.2,
            CK.REWARDS: {},
        },
        25: {
            CK.EXPERIENCE: 17898.8,
            CK.REWARDS: {},
        },
        26: {
            CK.EXPERIENCE: 132273.4,
            CK.REWARDS: {},
        },
        27: {
            CK.EXPERIENCE: 246648.0,
            CK.REWARDS: {},
        },
        28: {
            CK.EXPERIENCE: 361022.6,
            CK.REWARDS: {},
        },
        29: {
            CK.EXPERIENCE: 475397.2,
            CK.REWARDS: {},
        },
        30: {
            CK.EXPERIENCE: 589771.8,
            CK.REWARDS: {},
        },
        31: {
            CK.EXPERIENCE: 704146.2,
            CK.REWARDS: {},
        },
        32: {
            CK.EXPERIENCE: 818520.8,
            CK.REWARDS: {},
        },
        33: {
            CK.EXPERIENCE: 932895.4,
            CK.REWARDS: {},
        },
        34: {
            CK.EXPERIENCE: 1047270.0,
            CK.REWARDS: {},
        },
        35: {
            CK.EXPERIENCE: 1161644.6,
            CK.REWARDS: {},
        },
        36: {
            CK.EXPERIENCE: 1237014.6,
            CK.REWARDS: {},
        },
        37: {
            CK.EXPERIENCE: 1312384.6,
            CK.REWARDS: {},
        },
        38: {
            CK.EXPERIENCE: 1387754.6,
            CK.REWARDS: {},
        },
        39: {
            CK.EXPERIENCE: 1463124.6,
            CK.REWARDS: {},
        },
        40: {
            CK.EXPERIENCE: 1538494.6,
            CK.REWARDS: {},
        },
        41: {
            CK.EXPERIENCE: 1613864.6,
            CK.REWARDS: {},
        },
        42: {
            CK.EXPERIENCE: 1689234.6,
            CK.REWARDS: {},
        },
        43: {
            CK.EXPERIENCE: 1764604.6,
            CK.REWARDS: {},
        },
        44: {
            CK.EXPERIENCE: 1839974.6,
            CK.REWARDS: {},
        },
        45: {
            CK.EXPERIENCE: 1915344.6,
            CK.REWARDS: {},
        },
        46: {
            CK.EXPERIENCE: 1990714.6,
            CK.REWARDS: {},
        },
        47: {
            CK.EXPERIENCE: 2066084.6,
            CK.REWARDS: {},
        },
        48: {
            CK.EXPERIENCE: 2141454.6,
            CK.REWARDS: {},
        },
        49: {
            CK.EXPERIENCE: 2216824.6,
            CK.REWARDS: {},
        },
        50: {
            CK.EXPERIENCE: 2292194.6,
            CK.REWARDS: {},
        }
    }

    @staticmethod
    def get_max_level():
        return 50

    @staticmethod
    def get_level_experience(level: int):
        return PlanetLevelData.LEVEL[level][CK.EXPERIENCE]

    @staticmethod
    def get_level_rewards(level):
        return PlanetLevelData.LEVEL[level][CK.REWARDS]
