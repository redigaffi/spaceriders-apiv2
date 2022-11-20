from dataclasses import dataclass

from .Common import CommonKeys as CK


@dataclass
class PlanetData:
    BUY_PLANET_COST_USD = 15

    IMAGES = 5

    UNCOMMON = "uncommon"
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

    RARITY_WEIGHTS = (50, 25, 15, 8, 2)
    RARITIES = [COMMON, UNCOMMON, RARE, EPIC, LEGENDARY]

    DATA = {
        COMMON: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 50,
            "diameter": {
                "range": (180000, 200000),
            },
            "reserves": {
                "range": (862393, 1062393),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 499.50,
                CK.PETROL: 176.50,
                CK.CRYSTAL: 285.43,
                CK.ENERGY: 500,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1,
                CK.PETROL: 1,
                CK.CRYSTAL: 1,
            }
        },
        UNCOMMON: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 50,
            "diameter": {
                "range": (200000, 230000),
            },
            "reserves": {
                "range": (1102991, 1302991),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 624.38,
                CK.PETROL: 220.63,
                CK.CRYSTAL: 356.79,
                CK.ENERGY: 750,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1,
                CK.PETROL: 1,
                CK.CRYSTAL: 1,
            }
        },
        RARE: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 50,
            "diameter": {
                "range": (230000, 260000),
            },
            "reserves": {
                "range": (1343589, 1543589),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 749.25,
                CK.PETROL: 264.75,
                CK.CRYSTAL: 428.14,
                CK.ENERGY: 1000,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1,
                CK.PETROL: 1,
                CK.CRYSTAL: 1,
            }
        },
        EPIC: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 500,
            "diameter": {
                "range": (2600000, 3000000),
            },
            "reserves": {
                "range": (1584187, 1784187),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 874.13,
                CK.PETROL: 308.88,
                CK.CRYSTAL: 499.50,
                CK.ENERGY: 1250,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1,
                CK.PETROL: 1,
                CK.CRYSTAL: 1,
            }
        },
        LEGENDARY: {
            CK.ENERGY_DEPOSIT_MAX_ONCE: 1500,
            "diameter": {
                "range": (300000, 330000),
            },
            "reserves": {
                "range": (1824785, 2024785),
            },
            CK.INITIAL_RESERVE: {
                CK.METAL: 999.00,
                CK.PETROL: 353.00,
                CK.CRYSTAL: 570.86,
                CK.ENERGY: 1500,
            },
            CK.RESOURCE_EXTRACTION_MULTIPLIER: {
                CK.METAL: 1,
                CK.PETROL: 1,
                CK.CRYSTAL: 1,
            }
        }
    }
