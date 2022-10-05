from dataclasses import dataclass
import random


@dataclass
class AsteroidData:
    """
    Data class representing in game items
    """

    LEVELS = ["1-9"]

    ASTEROIDS = {
        "1-9": {
            # Expressed in km
            "diameter": (40, 70),
            # Expressed in meters
            "distance": (3000, 8000),
            # Expressed in meters/s
            "speed": (400, 1200),
            # Health is asteroid health and also asteroid attack points
            "health_per_diameter": (30, 80),
        }
    }

    @staticmethod
    def get_asteroid_data_level(planet_level):
        for level in AsteroidData.LEVELS:
            lvl_info = level.split("-")
            if int(lvl_info[0]) <= planet_level <= int(lvl_info[1]):
                asteroid_lvl_info = AsteroidData.ASTEROIDS[level]
                diameter = random.randint(
                    asteroid_lvl_info["diameter"][0], asteroid_lvl_info["diameter"][1]
                )
                distance = random.randint(
                    asteroid_lvl_info["distance"][0], asteroid_lvl_info["distance"][1]
                )
                speed = random.randint(
                    asteroid_lvl_info["speed"][0], asteroid_lvl_info["speed"][1]
                )
                health = random.randint(
                    asteroid_lvl_info["health_per_diameter"][0],
                    asteroid_lvl_info["health_per_diameter"][1],
                )
                return diameter, distance, speed, health

        raise ValueError(f"No asteroid info for level {planet_level}")
