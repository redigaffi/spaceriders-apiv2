from dataclasses import dataclass

from .Common import (
    BuildableItemBaseType,
    BuildableItemLevelInfo,
    BuildableItemRequirement,
)
from .Common import CommonKeys as CK
from .GameData import GameData


@dataclass
class ResourceData(GameData):
    """
    Data class representing in game items
    Production is expressed per minute
    """

    TYPE = "resources"

    MINE_CATEGORY = "mine_category"
    WAREHOUSE_CATEGORY = "warehouse_category"

    METAL_MINE = "metalMine"
    CRYSTAL_MINE = "crystalMine"
    PETROL_MINE = "petrolMine"
    METAL_WAREHOUSE = "metalWarehouse"
    CRYSTAL_WAREHOUSE = "crystalWarehouse"
    PETROL_WAREHOUSE = "petrolWarehouse"

    TYPES = [
        METAL_MINE,
        CRYSTAL_MINE,
        PETROL_MINE,
        METAL_WAREHOUSE,
        CRYSTAL_WAREHOUSE,
        PETROL_WAREHOUSE,
    ]

    COMMON_WAREHOUSE_KEYS = [
        CK.LEVEL,
        CK.COST_METAL,
        CK.COST_PETROL,
        CK.COST_CRYSTAL,
        CK.CAPACITY,
        CK.TIME,
        CK.HEALTH,
        CK.EXPERIENCE,
        CK.REQUIREMENTS,
    ]

    __ITEMS = {
        METAL_MINE: BuildableItemBaseType(
            "Metal Mine",
            METAL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Metal mine to extract metal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=9, health=1000, time=70, cost_metal=60, cost_crystal=15, cost_petrol=0, production=1.0, energy_usage=0.1, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=12, health=1002, time=111, cost_metal=82, cost_crystal=21, cost_petrol=0, production=1.03, energy_usage=0.103318, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=16, health=1006, time=172, cost_metal=112, cost_crystal=28, cost_petrol=0, production=1.07, energy_usage=0.107115, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=22, health=1010, time=263, cost_metal=150, cost_crystal=38, cost_petrol=0, production=1.11, energy_usage=0.111434, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=29, health=1016, time=394, cost_metal=199, cost_crystal=50, cost_petrol=0, production=1.16, energy_usage=0.116323, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=38, health=1023, time=581, cost_metal=262, cost_crystal=65, cost_petrol=0, production=1.22, energy_usage=0.121842, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=49, health=1033, time=839, cost_metal=340, cost_crystal=85, cost_petrol=0, production=1.28, energy_usage=0.128057, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=63, health=1046, time=1190, cost_metal=437, cost_crystal=109, cost_petrol=0, production=1.35, energy_usage=0.135046, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=80, health=1061, time=1655, cost_metal=555, cost_crystal=139, cost_petrol=0, production=1.43, energy_usage=0.142898, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=100, health=1082, time=2256, cost_metal=698, cost_crystal=174, cost_petrol=0, production=1.52, energy_usage=0.151715, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=125, health=1106, time=3013, cost_metal=866, cost_crystal=217, cost_petrol=0, production=1.62, energy_usage=0.161618, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=153, health=1137, time=3942, cost_metal=1063, cost_crystal=266, cost_petrol=0, production=1.73, energy_usage=0.172743, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=185, health=1174, time=5050, cost_metal=1289, cost_crystal=322, cost_petrol=0, production=1.85, energy_usage=0.185249, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=222, health=1218, time=6331, cost_metal=1544, cost_crystal=386, cost_petrol=0, production=1.99, energy_usage=0.199322, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=263, health=1271, time=7763, cost_metal=1827, cost_crystal=457, cost_petrol=0, production=2.15, energy_usage=0.215174, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=307, health=1332, time=9307, cost_metal=2136, cost_crystal=534, cost_petrol=0, production=2.33, energy_usage=0.233054, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=355, health=1403, time=10903, cost_metal=2467, cost_crystal=617, cost_petrol=0, production=2.53, energy_usage=0.25325, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=404, health=1484, time=12474, cost_metal=2812, cost_crystal=703, cost_petrol=0, production=2.76, energy_usage=0.2761, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=455, health=1575, time=13931, cost_metal=3166, cost_crystal=791, cost_petrol=0, production=3.02, energy_usage=0.301996, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=506, health=1676, time=15176, cost_metal=3518, cost_crystal=879, cost_petrol=0, production=3.31, energy_usage=0.331397, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=841, health=1845, time=16499, cost_metal=3903, cost_crystal=976, cost_petrol=0, production=3.65, energy_usage=0.365038, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=932, health=2031, time=17902, cost_metal=4323, cost_crystal=1081, cost_petrol=0, production=4.04, energy_usage=0.403612, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=1031, health=2237, time=19386, cost_metal=4781, cost_crystal=1195, cost_petrol=0, production=4.48, energy_usage=0.447941, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=1138, health=2465, time=20950, cost_metal=5279, cost_crystal=1320, cost_petrol=0, production=4.99, energy_usage=0.499001, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=1255, health=2716, time=22594, cost_metal=5819, cost_crystal=1455, cost_petrol=0, production=5.58, energy_usage=0.557955, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=1381, health=2992, time=24319, cost_metal=6405, cost_crystal=1601, cost_petrol=0, production=6.26, energy_usage=0.626195, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=1518, health=3295, time=26122, cost_metal=7038, cost_crystal=1760, cost_petrol=0, production=7.05, energy_usage=0.705385, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=1665, health=3628, time=28002, cost_metal=7722, cost_crystal=1930, cost_petrol=0, production=7.98, energy_usage=0.797522, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=1824, health=3993, time=29957, cost_metal=8459, cost_crystal=2115, cost_petrol=0, production=9.05, energy_usage=0.905011, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=1995, health=4392, time=31983, cost_metal=9251, cost_crystal=2313, cost_petrol=0, production=10.31, energy_usage=1.030749, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                31: BuildableItemLevelInfo(
                    level=31, experience=2178, health=4828, time=34076, cost_metal=10100, cost_crystal=2525, cost_petrol=0, production=11.78, energy_usage=1.178243, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                32: BuildableItemLevelInfo(
                    level=32, experience=2374, health=5303, time=36232, cost_metal=11011, cost_crystal=2753, cost_petrol=0, production=13.52, energy_usage=1.351741, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                33: BuildableItemLevelInfo(
                    level=33, experience=2584, health=5819, time=38445, cost_metal=11983, cost_crystal=2996, cost_petrol=0, production=15.56, energy_usage=1.556408, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                34: BuildableItemLevelInfo(
                    level=34, experience=2808, health=6381, time=40711, cost_metal=13021, cost_crystal=3255, cost_petrol=0, production=17.99, energy_usage=1.798535, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                35: BuildableItemLevelInfo(
                    level=35, experience=3046, health=6990, time=43021, cost_metal=14126, cost_crystal=3532, cost_petrol=0, production=20.86, energy_usage=2.085807, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                36: BuildableItemLevelInfo(
                    level=36, experience=3299, health=7650, time=45368, cost_metal=15300, cost_crystal=3825, cost_petrol=0, production=24.28, energy_usage=2.427637, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                37: BuildableItemLevelInfo(
                    level=37, experience=3567, health=8363, time=47745, cost_metal=16544, cost_crystal=4136, cost_petrol=0, production=28.36, energy_usage=2.835582, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                38: BuildableItemLevelInfo(
                    level=38, experience=3851, health=9134, time=50142, cost_metal=17861, cost_crystal=4465, cost_petrol=0, production=33.24, energy_usage=3.323869, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                39: BuildableItemLevelInfo(
                    level=39, experience=4151, health=9964, time=52551, cost_metal=19251, cost_crystal=4813, cost_petrol=0, production=39.1, energy_usage=3.910059, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                40: BuildableItemLevelInfo(
                    level=40, experience=4467, health=10857, time=54961, cost_metal=20715, cost_crystal=5179, cost_petrol=0, production=46.16, energy_usage=4.615887, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                41: BuildableItemLevelInfo(
                    level=41, experience=6445, health=12146, time=58987, cost_metal=22416, cost_crystal=5604, cost_petrol=0, production=54.33, energy_usage=5.43332, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                42: BuildableItemLevelInfo(
                    level=42, experience=7013, health=13549, time=64924, cost_metal=24392, cost_crystal=6098, cost_petrol=0, production=63.77, energy_usage=6.376906, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                43: BuildableItemLevelInfo(
                    level=43, experience=7673, health=15083, time=73238, cost_metal=26690, cost_crystal=6673, cost_petrol=0, production=74.63, energy_usage=7.462523, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                44: BuildableItemLevelInfo(
                    level=44, experience=8443, health=16772, time=84624, cost_metal=29365, cost_crystal=7341, cost_petrol=0, production=87.07, energy_usage=8.7074, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                45: BuildableItemLevelInfo(
                    level=45, experience=9340, health=18640, time=100098, cost_metal=32486, cost_crystal=8122, cost_petrol=0, production=101.3, energy_usage=10.130125, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                46: BuildableItemLevelInfo(
                    level=46, experience=10389, health=20718, time=121143, cost_metal=36135, cost_crystal=9034, cost_petrol=0, production=117.51, energy_usage=11.75062, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                47: BuildableItemLevelInfo(
                    level=47, experience=11619, health=23041, time=149933, cost_metal=40412, cost_crystal=10103, cost_petrol=0, production=135.9, energy_usage=13.5901, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                48: BuildableItemLevelInfo(
                    level=48, experience=13064, health=25654, time=189673, cost_metal=45440, cost_crystal=11360, cost_petrol=0, production=156.71, energy_usage=15.670997, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                49: BuildableItemLevelInfo(
                    level=49, experience=14768, health=28608, time=245143, cost_metal=51368, cost_crystal=12842, cost_petrol=0, production=180.17, energy_usage=18.01685, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                50: BuildableItemLevelInfo(
                    level=50, experience=49479, health=38504, time=440272, cost_metal=86050, cost_crystal=21513, cost_petrol=0, production=250.18, energy_usage=25.017943, capacity=0, attack=0, requirements=[], has_discount=0
                )
            },
        ),
        CRYSTAL_MINE: BuildableItemBaseType(
            "Crystal Mine",
            CRYSTAL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Crystal mine to extract Crystal",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=9, health=1000, time=91, cost_metal=48, cost_crystal=24, cost_petrol=0, production=0.57, energy_usage=0.1, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=12, health=1002, time=144, cost_metal=66, cost_crystal=33, cost_petrol=0, production=0.59, energy_usage=0.103318, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=17, health=1006, time=224, cost_metal=89, cost_crystal=45, cost_petrol=0, production=0.61, energy_usage=0.107115, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=23, health=1010, time=342, cost_metal=120, cost_crystal=60, cost_petrol=0, production=0.64, energy_usage=0.111434, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=30, health=1016, time=513, cost_metal=159, cost_crystal=80, cost_petrol=0, production=0.66, energy_usage=0.116323, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=39, health=1024, time=755, cost_metal=209, cost_crystal=105, cost_petrol=0, production=0.7, energy_usage=0.121842, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=51, health=1034, time=1091, cost_metal=272, cost_crystal=136, cost_petrol=0, production=0.73, energy_usage=0.128057, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=66, health=1047, time=1547, cost_metal=350, cost_crystal=175, cost_petrol=0, production=0.77, energy_usage=0.135046, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=83, health=1064, time=2151, cost_metal=444, cost_crystal=222, cost_petrol=0, production=0.82, energy_usage=0.142898, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=105, health=1085, time=2933, cost_metal=558, cost_crystal=279, cost_petrol=0, production=0.87, energy_usage=0.151715, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=130, health=1111, time=3917, cost_metal=693, cost_crystal=346, cost_petrol=0, production=0.92, energy_usage=0.161618, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=159, health=1143, time=5125, cost_metal=850, cost_crystal=425, cost_petrol=0, production=0.99, energy_usage=0.172743, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=193, health=1182, time=6565, cost_metal=1031, cost_crystal=515, cost_petrol=0, production=1.06, energy_usage=0.185249, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=232, health=1228, time=8230, cost_metal=1235, cost_crystal=618, cost_petrol=0, production=1.14, energy_usage=0.199322, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=274, health=1283, time=10092, cost_metal=1462, cost_crystal=731, cost_petrol=0, production=1.23, energy_usage=0.215174, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=320, health=1347, time=12099, cost_metal=1709, cost_crystal=854, cost_petrol=0, production=1.33, energy_usage=0.233054, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=370, health=1421, time=14174, cost_metal=1973, cost_crystal=987, cost_petrol=0, production=1.45, energy_usage=0.25325, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=422, health=1505, time=16217, cost_metal=2250, cost_crystal=1125, cost_petrol=0, production=1.58, energy_usage=0.2761, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=475, health=1600, time=18110, cost_metal=2533, cost_crystal=1266, cost_petrol=0, production=1.73, energy_usage=0.301996, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=528, health=1706, time=19729, cost_metal=2814, cost_crystal=1407, cost_petrol=0, production=1.89, energy_usage=0.331397, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=878, health=1881, time=21449, cost_metal=3122, cost_crystal=1561, cost_petrol=0, production=2.09, energy_usage=0.365038, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=973, health=2076, time=23273, cost_metal=3458, cost_crystal=1729, cost_petrol=0, production=2.31, energy_usage=0.403612, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=1076, health=2291, time=25202, cost_metal=3825, cost_crystal=1912, cost_petrol=0, production=2.56, energy_usage=0.447941, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=1188, health=2528, time=27235, cost_metal=4223, cost_crystal=2111, cost_petrol=0, production=2.85, energy_usage=0.499001, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=1309, health=2790, time=29373, cost_metal=4655, cost_crystal=2328, cost_petrol=0, production=3.19, energy_usage=0.557955, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=1441, health=3079, time=31615, cost_metal=5124, cost_crystal=2562, cost_petrol=0, production=3.58, energy_usage=0.626195, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=1584, health=3395, time=33959, cost_metal=5631, cost_crystal=2815, cost_petrol=0, production=4.03, energy_usage=0.705385, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=1737, health=3743, time=36403, cost_metal=6178, cost_crystal=3089, cost_petrol=0, production=4.56, energy_usage=0.797522, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=1903, health=4123, time=38944, cost_metal=6767, cost_crystal=3383, cost_petrol=0, production=5.17, energy_usage=0.905011, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=2081, health=4540, time=41578, cost_metal=7400, cost_crystal=3700, cost_petrol=0, production=5.89, energy_usage=1.030749, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                31: BuildableItemLevelInfo(
                    level=31, experience=2273, health=4994, time=44299, cost_metal=8080, cost_crystal=4040, cost_petrol=0, production=6.73, energy_usage=1.178243, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                32: BuildableItemLevelInfo(
                    level=32, experience=2477, health=5490, time=47101, cost_metal=8808, cost_crystal=4404, cost_petrol=0, production=7.72, energy_usage=1.351741, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                33: BuildableItemLevelInfo(
                    level=33, experience=2696, health=6029, time=49979, cost_metal=9587, cost_crystal=4793, cost_petrol=0, production=8.89, energy_usage=1.556408, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                34: BuildableItemLevelInfo(
                    level=34, experience=2930, health=6615, time=52924, cost_metal=10417, cost_crystal=5209, cost_petrol=0, production=10.28, energy_usage=1.798535, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                35: BuildableItemLevelInfo(
                    level=35, experience=3178, health=7251, time=55927, cost_metal=11301, cost_crystal=5650, cost_petrol=0, production=11.92, energy_usage=2.085807, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                36: BuildableItemLevelInfo(
                    level=36, experience=3442, health=7939, time=58978, cost_metal=12240, cost_crystal=6120, cost_petrol=0, production=13.87, energy_usage=2.427637, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                37: BuildableItemLevelInfo(
                    level=37, experience=3722, health=8684, time=62068, cost_metal=13235, cost_crystal=6618, cost_petrol=0, production=16.2, energy_usage=2.835582, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                38: BuildableItemLevelInfo(
                    level=38, experience=4019, health=9487, time=65185, cost_metal=14289, cost_crystal=7144, cost_petrol=0, production=18.99, energy_usage=3.323869, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                39: BuildableItemLevelInfo(
                    level=39, experience=4331, health=10354, time=68316, cost_metal=15401, cost_crystal=7700, cost_petrol=0, production=22.34, energy_usage=3.910059, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                40: BuildableItemLevelInfo(
                    level=40, experience=4661, health=11286, time=71449, cost_metal=16572, cost_crystal=8286, cost_petrol=0, production=26.38, energy_usage=4.615887, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                41: BuildableItemLevelInfo(
                    level=41, experience=6725, health=12631, time=76683, cost_metal=17933, cost_crystal=8967, cost_petrol=0, production=31.05, energy_usage=5.43332, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                42: BuildableItemLevelInfo(
                    level=42, experience=7318, health=14094, time=84402, cost_metal=19514, cost_crystal=9757, cost_petrol=0, production=36.44, energy_usage=6.376906, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                43: BuildableItemLevelInfo(
                    level=43, experience=8007, health=15696, time=95210, cost_metal=21352, cost_crystal=10676, cost_petrol=0, production=42.64, energy_usage=7.462523, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                44: BuildableItemLevelInfo(
                    level=44, experience=8810, health=17458, time=110011, cost_metal=23492, cost_crystal=11746, cost_petrol=0, production=49.76, energy_usage=8.7074, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                45: BuildableItemLevelInfo(
                    level=45, experience=9746, health=19407, time=130127, cost_metal=25989, cost_crystal=12995, cost_petrol=0, production=57.89, energy_usage=10.130125, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                46: BuildableItemLevelInfo(
                    level=46, experience=10841, health=21575, time=157486, cost_metal=28908, cost_crystal=14454, cost_petrol=0, production=67.15, energy_usage=11.75062, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                47: BuildableItemLevelInfo(
                    level=47, experience=12124, health=24000, time=194913, cost_metal=32330, cost_crystal=16165, cost_petrol=0, production=77.66, energy_usage=13.5901, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                48: BuildableItemLevelInfo(
                    level=48, experience=13632, health=26726, time=246575, cost_metal=36352, cost_crystal=18176, cost_petrol=0, production=89.55, energy_usage=15.670997, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                49: BuildableItemLevelInfo(
                    level=49, experience=15410, health=29808, time=318687, cost_metal=41094, cost_crystal=20547, cost_petrol=0, production=102.95, energy_usage=18.01685, capacity=0, attack=0, requirements=[], has_discount=0
                ),
                50: BuildableItemLevelInfo(
                    level=50, experience=51630, health=40134, time=572354, cost_metal=68840, cost_crystal=34420, cost_petrol=0, production=142.96, energy_usage=25.017943, capacity=0, attack=0, requirements=[], has_discount=0
                )
            },
        ),
        PETROL_MINE: BuildableItemBaseType(
            "Petrol Mine",
            PETROL_MINE,
            TYPE,
            MINE_CATEGORY,
            "Petrol mine to extract Petrol",
            {
                0: BuildableItemLevelInfo(),
                1: BuildableItemLevelInfo(
                    level=1, experience=20, health=1000, time=118, cost_metal=90, cost_crystal=60, cost_petrol=0, production=0.35, energy_usage=0.1, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=27, health=1005, time=187, cost_metal=123, cost_crystal=82, cost_petrol=0, production=0.37, energy_usage=0.103318, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=36, health=1013, time=291, cost_metal=168, cost_crystal=112, cost_petrol=0, production=0.38, energy_usage=0.107115, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=49, health=1022, time=444, cost_metal=225, cost_crystal=150, cost_petrol=0, production=0.39, energy_usage=0.111434, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=65, health=1035, time=667, cost_metal=299, cost_crystal=199, cost_petrol=0, production=0.41, energy_usage=0.116323, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=85, health=1052, time=982, cost_metal=393, cost_crystal=262, cost_petrol=0, production=0.43, energy_usage=0.121842, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=111, health=1074, time=1419, cost_metal=510, cost_crystal=340, cost_petrol=0, production=0.45, energy_usage=0.128057, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=142, health=1103, time=2011, cost_metal=656, cost_crystal=437, cost_petrol=0, production=0.48, energy_usage=0.135046, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=181, health=1139, time=2797, cost_metal=833, cost_crystal=555, cost_petrol=0, production=0.5, energy_usage=0.142898, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=227, health=1184, time=3812, cost_metal=1046, cost_crystal=698, cost_petrol=0, production=0.54, energy_usage=0.151715, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=281, health=1241, time=5092, cost_metal=1299, cost_crystal=866, cost_petrol=0, production=0.57, energy_usage=0.161618, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=345, health=1310, time=6662, cost_metal=1594, cost_crystal=1063, cost_petrol=0, production=0.61, energy_usage=0.172743, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=419, health=1393, time=8534, cost_metal=1933, cost_crystal=1289, cost_petrol=0, production=0.65, energy_usage=0.185249, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=502, health=1494, time=10699, cost_metal=2316, cost_crystal=1544, cost_petrol=0, production=0.7, energy_usage=0.199322, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=594, health=1613, time=13119, cost_metal=2741, cost_crystal=1827, cost_petrol=0, production=0.76, energy_usage=0.215174, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=694, health=1751, time=15728, cost_metal=3204, cost_crystal=2136, cost_petrol=0, production=0.82, energy_usage=0.233054, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=802, health=1912, time=18426, cost_metal=3700, cost_crystal=2467, cost_petrol=0, production=0.89, energy_usage=0.25325, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=914, health=2095, time=21082, cost_metal=4218, cost_crystal=2812, cost_petrol=0, production=0.98, energy_usage=0.2761, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=1029, health=2300, time=23543, cost_metal=4748, cost_crystal=3166, cost_petrol=0, production=1.07, energy_usage=0.301996, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=1143, health=2529, time=25647, cost_metal=5276, cost_crystal=3518, cost_petrol=0, production=1.17, energy_usage=0.331397, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=1902, health=2909, time=27884, cost_metal=5854, cost_crystal=3903, cost_petrol=0, production=1.29, energy_usage=0.365038, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=2107, health=3331, time=30255, cost_metal=6484, cost_crystal=4323, cost_petrol=0, production=1.43, energy_usage=0.403612, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=2331, health=3797, time=32762, cost_metal=7171, cost_crystal=4781, cost_petrol=0, production=1.58, energy_usage=0.447941, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=2573, health=4312, time=35405, cost_metal=7918, cost_crystal=5279, cost_petrol=0, production=1.76, energy_usage=0.499001, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=2837, health=4879, time=38185, cost_metal=8729, cost_crystal=5819, cost_petrol=0, production=1.97, energy_usage=0.557955, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=3122, health=5504, time=41099, cost_metal=9607, cost_crystal=6405, cost_petrol=0, production=2.21, energy_usage=0.626195, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=3431, health=6190, time=44147, cost_metal=10557, cost_crystal=7038, cost_petrol=0, production=2.49, energy_usage=0.705385, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=3764, health=6943, time=47324, cost_metal=11583, cost_crystal=7722, cost_petrol=0, production=2.82, energy_usage=0.797522, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=4124, health=7767, time=50627, cost_metal=12688, cost_crystal=8459, cost_petrol=0, production=3.2, energy_usage=0.905011, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=4510, health=8669, time=54051, cost_metal=13876, cost_crystal=9251, cost_petrol=0, production=3.64, energy_usage=1.030749, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                31: BuildableItemLevelInfo(
                    level=31, experience=4924, health=9654, time=57588, cost_metal=15151, cost_crystal=10100, cost_petrol=0, production=4.16, energy_usage=1.178243, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                32: BuildableItemLevelInfo(
                    level=32, experience=5368, health=10728, time=61232, cost_metal=16516, cost_crystal=11011, cost_petrol=0, production=4.78, energy_usage=1.351741, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                33: BuildableItemLevelInfo(
                    level=33, experience=5842, health=11896, time=64973, cost_metal=17975, cost_crystal=11983, cost_petrol=0, production=5.5, energy_usage=1.556408, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                34: BuildableItemLevelInfo(
                    level=34, experience=6348, health=13166, time=68801, cost_metal=19532, cost_crystal=13021, cost_petrol=0, production=6.36, energy_usage=1.798535, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                35: BuildableItemLevelInfo(
                    level=35, experience=6886, health=14543, time=72705, cost_metal=21189, cost_crystal=14126, cost_petrol=0, production=7.37, energy_usage=2.085807, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                36: BuildableItemLevelInfo(
                    level=36, experience=7459, health=16035, time=76672, cost_metal=22950, cost_crystal=15300, cost_petrol=0, production=8.58, energy_usage=2.427637, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                37: BuildableItemLevelInfo(
                    level=37, experience=8065, health=17648, time=80688, cost_metal=24817, cost_crystal=16544, cost_petrol=0, production=10.02, energy_usage=2.835582, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                38: BuildableItemLevelInfo(
                    level=38, experience=8707, health=19389, time=84740, cost_metal=26791, cost_crystal=17861, cost_petrol=0, production=11.75, energy_usage=3.323869, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                39: BuildableItemLevelInfo(
                    level=39, experience=9385, health=21266, time=88811, cost_metal=28876, cost_crystal=19251, cost_petrol=0, production=13.82, energy_usage=3.910059, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                40: BuildableItemLevelInfo(
                    level=40, experience=10099, health=23286, time=92883, cost_metal=31073, cost_crystal=20715, cost_petrol=0, production=16.31, energy_usage=4.615887, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                41: BuildableItemLevelInfo(
                    level=41, experience=14571, health=26200, time=99688, cost_metal=33624, cost_crystal=22416, cost_petrol=0, production=19.2, energy_usage=5.43332, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                42: BuildableItemLevelInfo(
                    level=42, experience=15855, health=29371, time=109722, cost_metal=36589, cost_crystal=24392, cost_petrol=0, production=22.53, energy_usage=6.376906, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                43: BuildableItemLevelInfo(
                    level=43, experience=17349, health=32841, time=123773, cost_metal=40035, cost_crystal=26690, cost_petrol=0, production=26.37, energy_usage=7.462523, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                44: BuildableItemLevelInfo(
                    level=44, experience=19088, health=36658, time=143014, cost_metal=44048, cost_crystal=29365, cost_petrol=0, production=30.77, energy_usage=8.7074, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                45: BuildableItemLevelInfo(
                    level=45, experience=21116, health=40881, time=169165, cost_metal=48730, cost_crystal=32486, cost_petrol=0, production=35.8, energy_usage=10.130125, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                46: BuildableItemLevelInfo(
                    level=46, experience=23488, health=45579, time=204732, cost_metal=54203, cost_crystal=36135, cost_petrol=0, production=41.52, energy_usage=11.75062, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                47: BuildableItemLevelInfo(
                    level=47, experience=26268, health=50833, time=253387, cost_metal=60619, cost_crystal=40412, cost_petrol=0, production=48.02, energy_usage=13.5901, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                48: BuildableItemLevelInfo(
                    level=48, experience=29536, health=56740, time=320548, cost_metal=68160, cost_crystal=45440, cost_petrol=0, production=55.37, energy_usage=15.670997, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                49: BuildableItemLevelInfo(
                    level=49, experience=33389, health=63418, time=414292, cost_metal=77052, cost_crystal=51368, cost_petrol=0, production=63.66, energy_usage=18.01685, capacity=0, attack=0, requirements=[],  has_discount=0
                ),
                50: BuildableItemLevelInfo(
                    level=50, experience=111865, health=85791, time=744060, cost_metal=129075, cost_crystal=86050, cost_petrol=0, production=88.4, energy_usage=25.017943, capacity=0, attack=0, requirements=[],  has_discount=0
                )
            },
        ),
        METAL_WAREHOUSE: BuildableItemBaseType(
            "Metal Warehouse",
            METAL_WAREHOUSE,
            TYPE,
            WAREHOUSE_CATEGORY,
            "Metal warehouse to store metal",
            {
                0: BuildableItemLevelInfo(
                    level=0, experience=0, health=0, time=0, cost_metal=0, cost_crystal=0, cost_petrol=0, production=0, energy_usage=0, capacity=1500, attack=0, requirements=[],  has_discount=0
                ),
                1: BuildableItemLevelInfo(
                    level=1, experience=78, health=2000, time=600, cost_metal=500, cost_crystal=0, cost_petrol=100, production=0, energy_usage=0, capacity=2250, attack=0, requirements=[],  has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=107, health=2021, time=938, cost_metal=681, cost_crystal=0, cost_petrol=136, production=0, energy_usage=0, capacity=2663, attack=0, requirements=[],  has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=143, health=2050, time=1423, cost_metal=911, cost_crystal=0, cost_petrol=182, production=0, energy_usage=0, capacity=3167, attack=0, requirements=[],  has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=187, health=2087, time=2094, cost_metal=1197, cost_crystal=0, cost_petrol=239, production=0, energy_usage=0, capacity=3781, attack=0, requirements=[],  has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=242, health=2136, time=2985, cost_metal=1543, cost_crystal=0, cost_petrol=309, production=0, energy_usage=0, capacity=4534, attack=0, requirements=[],  has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=306, health=2197, time=4117, cost_metal=1952, cost_crystal=0, cost_petrol=390, production=0, energy_usage=0, capacity=5460, attack=0, requirements=[],  has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=379, health=2273, time=5488, cost_metal=2422, cost_crystal=0, cost_petrol=484, production=0, energy_usage=0, capacity=6603, attack=0, requirements=[],  has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=461, health=2365, time=7064, cost_metal=2946, cost_crystal=0, cost_petrol=589, production=0, energy_usage=0, capacity=8019, attack=0, requirements=[],  has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=550, health=2475, time=8767, cost_metal=3513, cost_crystal=0, cost_petrol=703, production=0, energy_usage=0, capacity=9779, attack=0, requirements=[],  has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=643, health=2603, time=10477, cost_metal=4103, cost_crystal=0, cost_petrol=821, production=0, energy_usage=0, capacity=11977, attack=0, requirements=[],  has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=735, health=2750, time=12038, cost_metal=4693, cost_crystal=0, cost_petrol=939, production=0, energy_usage=0, capacity=14729, attack=0, requirements=[],  has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=823, health=2915, time=13277, cost_metal=5254, cost_crystal=0, cost_petrol=1051, production=0, energy_usage=0, capacity=18189, attack=0, requirements=[],  has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=1378, health=3191, time=14596, cost_metal=5867, cost_crystal=0, cost_petrol=1173, production=0, energy_usage=0, capacity=22196, attack=0, requirements=[],  has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=1535, health=3498, time=15993, cost_metal=6534, cost_crystal=0, cost_petrol=1307, production=0, energy_usage=0, capacity=26763, attack=0, requirements=[],  has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=1705, health=3839, time=17465, cost_metal=7258, cost_crystal=0, cost_petrol=1452, production=0, energy_usage=0, capacity=31878, attack=0, requirements=[],  has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=1889, health=4216, time=19010, cost_metal=8040, cost_crystal=0, cost_petrol=1608, production=0, energy_usage=0, capacity=37505, attack=0, requirements=[],  has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=2087, health=4634, time=20622, cost_metal=8884, cost_crystal=0, cost_petrol=1777, production=0, energy_usage=0, capacity=43578, attack=0, requirements=[],  has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=2300, health=5094, time=22296, cost_metal=9790, cost_crystal=0, cost_petrol=1958, production=0, energy_usage=0, capacity=49999, attack=0, requirements=[],  has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=2527, health=5599, time=24025, cost_metal=10759, cost_crystal=0, cost_petrol=2152, production=0, energy_usage=0, capacity=56635, attack=0, requirements=[],  has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=2770, health=6153, time=25801, cost_metal=11794, cost_crystal=0, cost_petrol=2359, production=0, energy_usage=0, capacity=63325, attack=0, requirements=[],  has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=3028, health=6759, time=27614, cost_metal=12893, cost_crystal=0, cost_petrol=2579, production=0, energy_usage=0, capacity=69881, attack=0, requirements=[],  has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=3302, health=7419, time=29455, cost_metal=14056, cost_crystal=0, cost_petrol=2811, production=0, energy_usage=0, capacity=76096, attack=0, requirements=[],  has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=3590, health=8137, time=31311, cost_metal=15284, cost_crystal=0, cost_petrol=3057, production=0, energy_usage=0, capacity=81753, attack=0, requirements=[],  has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=3893, health=8916, time=33171, cost_metal=16574, cost_crystal=0, cost_petrol=3315, production=0, energy_usage=0, capacity=86636, attack=0, requirements=[],  has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=5685, health=10053, time=36760, cost_metal=18153, cost_crystal=0, cost_petrol=3631, production=0, energy_usage=0, capacity=97687, attack=0, requirements=[],  has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=6289, health=11311, time=42530, cost_metal=20079, cost_crystal=0, cost_petrol=4016, production=0, energy_usage=0, capacity=116774, attack=0, requirements=[],  has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=7024, health=12716, time=51281, cost_metal=22427, cost_crystal=0, cost_petrol=4485, production=0, energy_usage=0, capacity=147509, attack=0, requirements=[],  has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=7922, health=14300, time=64336, cost_metal=25293, cost_crystal=0, cost_petrol=5059, production=0, energy_usage=0, capacity=196338, attack=0, requirements=[],  has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=9020, health=16104, time=83852, cost_metal=28800, cost_crystal=0, cost_petrol=5760, production=0, energy_usage=0, capacity=274647, attack=0, requirements=[],  has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=25887, health=21281, time=151509, cost_metal=41326, cost_crystal=0, cost_petrol=8265, production=0, energy_usage=0, capacity=499093, attack=0, requirements=[],  has_discount=0
                )
            },
        ),
        CRYSTAL_WAREHOUSE: BuildableItemBaseType(
            "Crystal Warehouse",
            CRYSTAL_WAREHOUSE,
            TYPE,
            WAREHOUSE_CATEGORY,
            "Crystal warehouse to store crystal",
            {
                0: BuildableItemLevelInfo(
                    level=0, experience=0, health=0, time=0, cost_metal=0, cost_crystal=0, cost_petrol=0, production=0, energy_usage=0, capacity=857, attack=0, requirements=[],  has_discount=0
                ),
                1: BuildableItemLevelInfo(
                    level=1, experience=150, health=2000, time=780, cost_metal=500, cost_crystal=250, cost_petrol=200, production=0, energy_usage=0, capacity=1286, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=205, health=2041, time=1219, cost_metal=681, cost_crystal=341, cost_petrol=272, production=0, energy_usage=0, capacity=1522, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=274, health=2096, time=1850, cost_metal=911, cost_crystal=456, cost_petrol=364, production=0, energy_usage=0, capacity=1809, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=360, health=2168, time=2722, cost_metal=1197, cost_crystal=598, cost_petrol=479, production=0, energy_usage=0, capacity=2161, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=464, health=2261, time=3880, cost_metal=1543, cost_crystal=771, cost_petrol=617, production=0, energy_usage=0, capacity=2591, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=587, health=2378, time=5352, cost_metal=1952, cost_crystal=976, cost_petrol=781, production=0, energy_usage=0, capacity=3120, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=728, health=2524, time=7135, cost_metal=2422, cost_crystal=1211, cost_petrol=969, production=0, energy_usage=0, capacity=3773, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=886, health=2701, time=9183, cost_metal=2946, cost_crystal=1473, cost_petrol=1179, production=0, energy_usage=0, capacity=4582, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=1056, health=2912, time=11397, cost_metal=3513, cost_crystal=1756, cost_petrol=1405, production=0, energy_usage=0, capacity=5588, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=1234, health=3159, time=13620, cost_metal=4103, cost_crystal=2052, cost_petrol=1641, production=0, energy_usage=0, capacity=6844, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=1411, health=3441, time=15649, cost_metal=4693, cost_crystal=2347, cost_petrol=1877, production=0, energy_usage=0, capacity=8417, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=1580, health=3757, time=17260, cost_metal=5254, cost_crystal=2627, cost_petrol=2102, production=0, energy_usage=0, capacity=10394, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=2646, health=4286, time=18975, cost_metal=5867, cost_crystal=2934, cost_petrol=2347, production=0, energy_usage=0, capacity=12684, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=2947, health=4876, time=20791, cost_metal=6534, cost_crystal=3267, cost_petrol=2614, production=0, energy_usage=0, capacity=15293, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=3274, health=5530, time=22705, cost_metal=7258, cost_crystal=3629, cost_petrol=2903, production=0, energy_usage=0, capacity=18216, attack=0, requirements=[], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=3627, health=6256, time=24713, cost_metal=8040, cost_crystal=4020, cost_petrol=3216, production=0, energy_usage=0, capacity=21432, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=4007, health=7057, time=26808, cost_metal=8884, cost_crystal=4442, cost_petrol=3554, production=0, energy_usage=0, capacity=24902, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=4416, health=7940, time=28985, cost_metal=9790, cost_crystal=4895, cost_petrol=3916, production=0, energy_usage=0, capacity=28571, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=4853, health=8911, time=31232, cost_metal=10759, cost_crystal=5380, cost_petrol=4304, production=0, energy_usage=0, capacity=32363, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=5319, health=9975, time=33541, cost_metal=11794, cost_crystal=5897, cost_petrol=4717, production=0, energy_usage=0, capacity=36186, attack=0, requirements=[], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=5815, health=11138, time=35898, cost_metal=12893, cost_crystal=6446, cost_petrol=5157, production=0, energy_usage=0, capacity=39932, attack=0, requirements=[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=6340, health=12406, time=38291, cost_metal=14056, cost_crystal=7028, cost_petrol=5623, production=0, energy_usage=0, capacity=43483, attack=0, requirements=[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=6894, health=13785, time=40705, cost_metal=15284, cost_crystal=7642, cost_petrol=6114, production=0, energy_usage=0, capacity=46716, attack=0, requirements=[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=7476, health=15280, time=43122, cost_metal=16574, cost_crystal=8287, cost_petrol=6630, production=0, energy_usage=0, capacity=49506, attack=0, requirements=[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=10917, health=17463, time=47788, cost_metal=18153, cost_crystal=9076, cost_petrol=7261, production=0, energy_usage=0, capacity=55821, attack=0, requirements=[], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=12075, health=19878, time=55289, cost_metal=20079, cost_crystal=10039, cost_petrol=8031, production=0, energy_usage=0, capacity=66728, attack=0, requirements=[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=13488, health=22576, time=66666, cost_metal=22427, cost_crystal=11214, cost_petrol=8971, production=0, energy_usage=0, capacity=84291, attack=0, requirements=[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=15211, health=25618, time=83636, cost_metal=25293, cost_crystal=12647, cost_petrol=10117, production=0, energy_usage=0, capacity=112193, attack=0, requirements=[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=17321, health=29082, time=109007, cost_metal=28800, cost_crystal=14400, cost_petrol=11520, production=0, energy_usage=0, capacity=156941, attack=0, requirements=[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=49707, health=39024, time=196962, cost_metal=41326, cost_crystal=20663, cost_petrol=16531, production=0, energy_usage=0, capacity=285196, attack=0, requirements=[], has_discount=0
                )
            },
        ),
        PETROL_WAREHOUSE: BuildableItemBaseType(
            "Petrol Warehouse",
            PETROL_WAREHOUSE,
            TYPE,
            WAREHOUSE_CATEGORY,
            "Petrol warehouse to store petrol",
            {
                0: BuildableItemLevelInfo(
                    level=0, experience=0, health=0, time=0, cost_metal=0, cost_crystal=0, cost_petrol=0, production=0, energy_usage=0, capacity=530, attack=0, requirements=[],  has_discount=0
                ),
                1: BuildableItemLevelInfo(
                    level=1, experience=247, health=2000, time=1014, cost_metal=750, cost_crystal=500, cost_petrol=300, production=0, energy_usage=0, capacity=795, attack=0, requirements=[], has_discount=0
                ),
                2: BuildableItemLevelInfo(
                    level=2, experience=337, health=2067, time=1585, cost_metal=1022, cost_crystal=681, cost_petrol=409, production=0, energy_usage=0, capacity=941, attack=0, requirements=[], has_discount=0
                ),
                3: BuildableItemLevelInfo(
                    level=3, experience=451, health=2158, time=2405, cost_metal=1367, cost_crystal=911, cost_petrol=547, production=0, energy_usage=0, capacity=1119, attack=0, requirements=[], has_discount=0
                ),
                4: BuildableItemLevelInfo(
                    level=4, experience=592, health=2276, time=3539, cost_metal=1795, cost_crystal=1197, cost_petrol=718, production=0, energy_usage=0, capacity=1336, attack=0, requirements=[], has_discount=0
                ),
                5: BuildableItemLevelInfo(
                    level=5, experience=763, health=2429, time=5044, cost_metal=2314, cost_crystal=1543, cost_petrol=926, production=0, energy_usage=0, capacity=1602, attack=0, requirements=[], has_discount=0
                ),
                6: BuildableItemLevelInfo(
                    level=6, experience=966, health=2622, time=6957, cost_metal=2928, cost_crystal=1952, cost_petrol=1171, production=0, energy_usage=0, capacity=1929, attack=0, requirements=[], has_discount=0
                ),
                7: BuildableItemLevelInfo(
                    level=7, experience=1198, health=2861, time=9275, cost_metal=3633, cost_crystal=2422, cost_petrol=1453, production=0, energy_usage=0, capacity=2333, attack=0, requirements=[], has_discount=0
                ),
                8: BuildableItemLevelInfo(
                    level=8, experience=1458, health=3153, time=11938, cost_metal=4419, cost_crystal=2946, cost_petrol=1768, production=0, energy_usage=0, capacity=2833, attack=0, requirements=[], has_discount=0
                ),
                9: BuildableItemLevelInfo(
                    level=9, experience=1738, health=3501, time=14816, cost_metal=5269, cost_crystal=3513, cost_petrol=2108, production=0, energy_usage=0, capacity=3456, attack=0, requirements=[], has_discount=0
                ),
                10: BuildableItemLevelInfo(
                    level=10, experience=2030, health=3907, time=17706, cost_metal=6155, cost_crystal=4103, cost_petrol=2462, production=0, energy_usage=0, capacity=4232, attack=0, requirements=[], has_discount=0
                ),
                11: BuildableItemLevelInfo(
                    level=11, experience=2322, health=4371, time=20344, cost_metal=7040, cost_crystal=4693, cost_petrol=2816, production=0, energy_usage=0, capacity=5205, attack=0, requirements=[], has_discount=0
                ),
                12: BuildableItemLevelInfo(
                    level=12, experience=2600, health=4891, time=22439, cost_metal=7881, cost_crystal=5254, cost_petrol=3153, production=0, energy_usage=0, capacity=6427, attack=0, requirements=[], has_discount=0
                ),
                13: BuildableItemLevelInfo(
                    level=13, experience=4354, health=5762, time=24667, cost_metal=8801, cost_crystal=5867, cost_petrol=3520, production=0, energy_usage=0, capacity=7843, attack=0, requirements=[], has_discount=0
                ),
                14: BuildableItemLevelInfo(
                    level=14, experience=4850, health=6732, time=27028, cost_metal=9801, cost_crystal=6534, cost_petrol=3920, production=0, energy_usage=0, capacity=9457, attack=0, requirements=[], has_discount=0
                ),
                15: BuildableItemLevelInfo(
                    level=15, experience=5387, health=7809, time=29516, cost_metal=10887, cost_crystal=7258, cost_petrol=4355, production=0, energy_usage=0, capacity=11264, attack=0, requirements=[], has_discount=0
                ),
                16: BuildableItemLevelInfo(
                    level=16, experience=5968, health=9003, time=32126, cost_metal=12060, cost_crystal=8040, cost_petrol=4824, production=0, energy_usage=0, capacity=13253, attack=0, requirements=[], has_discount=0
                ),
                17: BuildableItemLevelInfo(
                    level=17, experience=6594, health=10322, time=34851, cost_metal=13326, cost_crystal=8884, cost_petrol=5330, production=0, energy_usage=0, capacity=15399, attack=0, requirements=[], has_discount=0
                ),
                18: BuildableItemLevelInfo(
                    level=18, experience=7266, health=11775, time=37680, cost_metal=14685, cost_crystal=9790, cost_petrol=5874, production=0, energy_usage=0, capacity=17667, attack=0, requirements=[], has_discount=0
                ),
                19: BuildableItemLevelInfo(
                    level=19, experience=7986, health=13372, time=40602, cost_metal=16139, cost_crystal=10759, cost_petrol=6456, production=0, energy_usage=0, capacity=20012, attack=0, requirements=[], has_discount=0
                ),
                20: BuildableItemLevelInfo(
                    level=20, experience=8753, health=15122, time=43603, cost_metal=17690, cost_crystal=11794, cost_petrol=7076, production=0, energy_usage=0, capacity=22376, attack=0, requirements=[], has_discount=0
                ),
                21: BuildableItemLevelInfo(
                    level=21, experience=9569, health=17036, time=46668, cost_metal=19339, cost_crystal=12893, cost_petrol=7736, production=0, energy_usage=0, capacity=24693, attack=0, requirements=[], has_discount=0
                ),
                22: BuildableItemLevelInfo(
                    level=22, experience=10433, health=19123, time=49778, cost_metal=21084, cost_crystal=14056, cost_petrol=8434, production=0, energy_usage=0, capacity=26889, attack=0, requirements=[], has_discount=0
                ),
                23: BuildableItemLevelInfo(
                    level=23, experience=11344, health=21391, time=52916, cost_metal=22926, cost_crystal=15284, cost_petrol=9170, production=0, energy_usage=0, capacity=28888, attack=0, requirements=[], has_discount=0
                ),
                24: BuildableItemLevelInfo(
                    level=24, experience=12301, health=23852, time=56059, cost_metal=24861, cost_crystal=16574, cost_petrol=9944, production=0, energy_usage=0, capacity=30613, attack=0, requirements=[], has_discount=0
                ),
                25: BuildableItemLevelInfo(
                    level=25, experience=17964, health=27444, time=62124, cost_metal=27229, cost_crystal=18153, cost_petrol=10892, production=0, energy_usage=0, capacity=34518, attack=0, requirements=[], has_discount=0
                ),
                26: BuildableItemLevelInfo(
                    level=26, experience=19870, health=31418, time=71876, cost_metal=30118, cost_crystal=20079, cost_petrol=12047, production=0, energy_usage=0, capacity=41263, attack=0, requirements=[], has_discount=0
                ),
                27: BuildableItemLevelInfo(
                    level=27, experience=22194, health=35857, time=86666, cost_metal=33641, cost_crystal=22427, cost_petrol=13456, production=0, energy_usage=0, capacity=52123, attack=0, requirements=[], has_discount=0
                ),
                28: BuildableItemLevelInfo(
                    level=28, experience=25030, health=40863, time=108727, cost_metal=37940, cost_crystal=25293, cost_petrol=15176, production=0, energy_usage=0, capacity=69377, attack=0, requirements=[], has_discount=0
                ),
                29: BuildableItemLevelInfo(
                    level=29, experience=28501, health=46563, time=141709, cost_metal=43201, cost_crystal=28800, cost_petrol=17280, production=0, energy_usage=0, capacity=97048, attack=0, requirements=[], has_discount=0
                ),
                30: BuildableItemLevelInfo(
                    level=30, experience=81793, health=62922, time=256051, cost_metal=61989, cost_crystal=41326, cost_petrol=24796, production=0, energy_usage=0, capacity=176358, attack=0, requirements=[], has_discount=0
                )
            },
        ),
    }
    @staticmethod
    def valid_type(label: str) -> bool:
        return label in ResourceData.TYPES

    @staticmethod
    def get_type() -> str:
        return ResourceData.TYPE

    @staticmethod
    def get_item(key: str) -> BuildableItemBaseType:
        if key not in ResourceData.TYPES:
            raise ValueError(
                f"{key} not in {ResourceData.TYPES} for {ResourceData.TYPE}"
            )

        return ResourceData.__ITEMS[key]
