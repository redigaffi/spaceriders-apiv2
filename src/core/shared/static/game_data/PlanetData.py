from dataclasses import dataclass
from .Common import CommonKeys as CK


@dataclass
class PlanetData:
    BUY_PLANET_COST_USD = 10

    IMAGES = 12

    COMMON = "common"
    EPIC = "epic"
    LEGENDARY = "legendary"

    RARITY_WEIGHTS = (90, 9, 1)
    RARITIES = [COMMON, EPIC, LEGENDARY]

    DATA = {
        COMMON: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 50,
            "diameter": {
                "range": (120000, 140000),
            },
            "reserves": {
                "range": (400000, 600000),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 200,
                CK.PETROL: 300,
                CK.CRYSTAL: 150,
                CK.ENERGY: 1.5,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1,
                CK.PETROL: 1,
                CK.CRYSTAL: 1
            }
        },
        EPIC: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 500,
            "diameter": {
                "range": (150000, 170000),
            },
            "reserves": {
                "range": (600000, 800000),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 400,
                CK.PETROL: 400,
                CK.CRYSTAL: 250,
                CK.ENERGY: 2.5,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1.1,
                CK.PETROL: 1.1,
                CK.CRYSTAL: 1.1
            }
        },

        LEGENDARY: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 1500,
            "diameter": {
                "range": (180000, 200000),
            },
            "reserves": {
                "range": (900000, 1100000),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 800,
                CK.PETROL: 800,
                CK.CRYSTAL: 500,
                CK.ENERGY: 5,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1.2,
                CK.PETROL: 1.2,
                CK.CRYSTAL: 1.2
            }
        },
    }
