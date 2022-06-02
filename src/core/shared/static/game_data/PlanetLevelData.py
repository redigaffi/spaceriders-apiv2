from .Common import CommonKeys as CK


class PlanetLevelData:
    LEVEL = {
        1: {
            CK.EXPERIENCE: 200,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        2: {
            CK.EXPERIENCE: 400,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        3: {
            CK.EXPERIENCE: 800,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        4: {
            CK.EXPERIENCE: 1200,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        5: {
            CK.EXPERIENCE: 2400,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        6: {
            CK.EXPERIENCE: 400,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        7: {
            CK.EXPERIENCE: 7500,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        8: {
            CK.EXPERIENCE: 8000,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        9: {
            CK.EXPERIENCE: 10000,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        10: {
            CK.EXPERIENCE: 15000,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },
        11: {
            CK.EXPERIENCE: 30000,
            CK.REWARDS: {
                CK.PURCHASING_POWER: 10  # Additional (in usd)
            }
        },

    }

    @staticmethod
    def get_level_rewards(level):
        return PlanetLevelData.LEVEL[level][CK.REWARDS]
