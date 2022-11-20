from dataclasses import dataclass

from .Common import CommonKeys as CK


@dataclass
class PlanetData:
    BUY_PLANET_COST_USD = 15

    POISON = "poison"
    WATER = "water"
    FIRE = "fire"
    GAS = "gas"
    SAND = "sand"

    PlANET_TYPES = [POISON, WATER, FIRE, GAS, SAND]
    PLANET_TYPE_WEIGHTS = (50, 25, 15, 8, 2)
    PLANET_TYPE_IMAGE_MAPPING = {
        POISON: 1,
        WATER: 2,
        FIRE: 3,
        GAS: 4,
        SAND: 5,
    }

    UNCOMMON = "uncommon"
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

    RARITIES = [COMMON, UNCOMMON, RARE, EPIC, LEGENDARY]
    RARITY_WEIGHTS = (50, 25, 15, 8, 2)

    DATA = {
        COMMON: {
            POISON: {
                CK.DIAMETER: {
                    CK.RANGE: (180000, 200000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 499.50,
                    CK.PETROL: 176.50,
                    CK.CRYSTAL: 285.43,
                    CK.ENERGY: 500,
                },
            },

            WATER: {
                CK.DIAMETER: {
                    CK.RANGE: (180000, 200000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 499.50,
                    CK.PETROL: 176.50,
                    CK.CRYSTAL: 285.43,
                    CK.ENERGY: 500,
                },
            },

            FIRE: {
                CK.DIAMETER: {
                    CK.RANGE: (180000, 200000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 499.50,
                    CK.PETROL: 176.50,
                    CK.CRYSTAL: 285.43,
                    CK.ENERGY: 500,
                },
            },

            GAS: {
                CK.DIAMETER: {
                    CK.RANGE: (180000, 200000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 499.50,
                    CK.PETROL: 176.50,
                    CK.CRYSTAL: 285.43,
                    CK.ENERGY: 500,
                },
            },

            SAND: {
                CK.DIAMETER: {
                    CK.RANGE: (180000, 200000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 499.50,
                    CK.PETROL: 176.50,
                    CK.CRYSTAL: 285.43,
                    CK.ENERGY: 500,
                },
            },
        },
        UNCOMMON: {
            POISON: {
                CK.DIAMETER: {
                    CK.RANGE: (200000, 230000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 624.38,
                    CK.PETROL: 220.63,
                    CK.CRYSTAL: 356.79,
                    CK.ENERGY: 750,
                },
            },
            WATER: {
                CK.DIAMETER: {
                    CK.RANGE: (200000, 230000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 624.38,
                    CK.PETROL: 220.63,
                    CK.CRYSTAL: 356.79,
                    CK.ENERGY: 750,
                },
            },
            FIRE: {
                CK.DIAMETER: {
                    CK.RANGE: (200000, 230000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 624.38,
                    CK.PETROL: 220.63,
                    CK.CRYSTAL: 356.79,
                    CK.ENERGY: 750,
                },
            },
            GAS: {
                CK.DIAMETER: {
                    CK.RANGE: (200000, 230000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 624.38,
                    CK.PETROL: 220.63,
                    CK.CRYSTAL: 356.79,
                    CK.ENERGY: 750,
                },
            },
            SAND: {
                CK.DIAMETER: {
                    CK.RANGE: (200000, 230000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 624.38,
                    CK.PETROL: 220.63,
                    CK.CRYSTAL: 356.79,
                    CK.ENERGY: 750,
                },
            },

        },
        RARE: {
            POISON: {
                CK.DIAMETER: {
                    CK.RANGE: (230000, 260000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 749.25,
                    CK.PETROL: 264.75,
                    CK.CRYSTAL: 428.14,
                    CK.ENERGY: 1000,
                },
            },
            WATER: {
                CK.DIAMETER: {
                    CK.RANGE: (230000, 260000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 749.25,
                    CK.PETROL: 264.75,
                    CK.CRYSTAL: 428.14,
                    CK.ENERGY: 1000,
                },
            },
            FIRE: {
                CK.DIAMETER: {
                    CK.RANGE: (230000, 260000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 749.25,
                    CK.PETROL: 264.75,
                    CK.CRYSTAL: 428.14,
                    CK.ENERGY: 1000,
                },
            },
            GAS: {
                CK.DIAMETER: {
                    CK.RANGE: (230000, 260000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 749.25,
                    CK.PETROL: 264.75,
                    CK.CRYSTAL: 428.14,
                    CK.ENERGY: 1000,
                },
            },
            SAND: {
                CK.DIAMETER: {
                    CK.RANGE: (230000, 260000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 749.25,
                    CK.PETROL: 264.75,
                    CK.CRYSTAL: 428.14,
                    CK.ENERGY: 1000,
                },
            },


        },
        EPIC: {
            POISON: {
                CK.DIAMETER: {
                    CK.RANGE: (2600000, 3000000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 874.13,
                    CK.PETROL: 308.88,
                    CK.CRYSTAL: 499.50,
                    CK.ENERGY: 1250,
                },
            },
            WATER: {
                CK.DIAMETER: {
                    CK.RANGE: (2600000, 3000000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 874.13,
                    CK.PETROL: 308.88,
                    CK.CRYSTAL: 499.50,
                    CK.ENERGY: 1250,
                },
            },
            FIRE: {
                CK.DIAMETER: {
                    CK.RANGE: (2600000, 3000000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 874.13,
                    CK.PETROL: 308.88,
                    CK.CRYSTAL: 499.50,
                    CK.ENERGY: 1250,
                },
            },
            GAS: {
                CK.DIAMETER: {
                    CK.RANGE: (2600000, 3000000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 874.13,
                    CK.PETROL: 308.88,
                    CK.CRYSTAL: 499.50,
                    CK.ENERGY: 1250,
                },
            },
            SAND: {
                CK.DIAMETER: {
                    CK.RANGE: (2600000, 3000000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 874.13,
                    CK.PETROL: 308.88,
                    CK.CRYSTAL: 499.50,
                    CK.ENERGY: 1250,
                },
            },
        },
        LEGENDARY: {
            POISON: {
                CK.DIAMETER: {
                    CK.RANGE: (300000, 330000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 999.00,
                    CK.PETROL: 353.00,
                    CK.CRYSTAL: 570.86,
                    CK.ENERGY: 1500,
                },
            },
            WATER: {
                CK.DIAMETER: {
                    CK.RANGE: (300000, 330000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 999.00,
                    CK.PETROL: 353.00,
                    CK.CRYSTAL: 570.86,
                    CK.ENERGY: 1500,
                },
            },
            FIRE: {
                CK.DIAMETER: {
                    CK.RANGE: (300000, 330000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 999.00,
                    CK.PETROL: 353.00,
                    CK.CRYSTAL: 570.86,
                    CK.ENERGY: 1500,
                },
            },
            GAS: {
                CK.DIAMETER: {
                    CK.RANGE: (300000, 330000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 999.00,
                    CK.PETROL: 353.00,
                    CK.CRYSTAL: 570.86,
                    CK.ENERGY: 1500,
                },
            },
            SAND: {
                CK.DIAMETER: {
                    CK.RANGE: (300000, 330000),
                },
                CK.RESERVES: {
                    CK.METAL: (862393, 1062393),
                    CK.CRYSTAL: (862393, 1062393),
                    CK.PETROL: (862393, 1062393),
                },
                CK.INITIAL_RESERVE: {
                    CK.METAL: 999.00,
                    CK.PETROL: 353.00,
                    CK.CRYSTAL: 570.86,
                    CK.ENERGY: 1500,
                },
            },
        }
    }
