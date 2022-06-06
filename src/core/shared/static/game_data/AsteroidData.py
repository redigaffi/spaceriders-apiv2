from dataclasses import dataclass
import random


@dataclass
class AsteroidData:
    """
     Data class representing in game items
    """
    LEVELS = [
        "0-9"
    ]

    ASTEROIDS = {
        "0-9": {
            # Expressed in km
            "diameter": (5, 15),
            # Expressed in meters
            "distance": (10000, 12000),
            # Expressed in meters/s
            "speed": (100, 200),
            # Health is asteroid health and also asteroid attack points
            "health_per_diameter": (10, 50)
        }
    }

    @staticmethod
    def get_asteroid_data_level(planet_level):
        for level in AsteroidData.LEVELS:
            lvl_info = level.split("-")
            if int(lvl_info[0]) <= planet_level <= int(lvl_info[1]):
                asteroid_lvl_info = AsteroidData.ASTEROIDS[level]
                diameter = random.randint(asteroid_lvl_info['diameter'][0], asteroid_lvl_info['diameter'][1])
                distance = random.randint(asteroid_lvl_info['distance'][0], asteroid_lvl_info['distance'][1])
                speed = random.randint(asteroid_lvl_info['speed'][0], asteroid_lvl_info['speed'][1])
                health = random.randint(asteroid_lvl_info['health_per_diameter'][0], asteroid_lvl_info['health_per_diameter'][1])
                return diameter, distance, speed, health

        raise ValueError(f"No asteroid info for level {planet_level}")

