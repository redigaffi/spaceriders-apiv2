from dataclasses import dataclass

from core.planet_email import PlanetEmail, PlanetSendEmailRequest
from core.planet_level import PlanetLevel, GivePlanetExperienceRequest
from core.shared.models import BuildableItem
from core.shared.ports import ResponsePort, PlanetRepositoryPort
from core.shared.static.game_data.AsteroidData import AsteroidData
from random import shuffle

from core.shared.static.game_data.DefenseData import DefenseData
import random
import math
from core.shared.static.game_data.ResearchData import ResearchData
from core.shared.static.game_data.StakingData import StakingData
import json


@dataclass
class Asteroid:
    planet_repository_port: PlanetRepositoryPort
    planet_level: PlanetLevel
    planet_email: PlanetEmail
    response_port: ResponsePort

    async def __call__(self, planet_id: str):
        report = {}

        planet = await self.planet_repository_port.get(planet_id)

        try:
            diameter, distance, speed, health = AsteroidData.get_asteroid_data_level(planet.level)
        except:
            print("error retrieving asteroid information")
            return

        asteroid_attack = diameter * health

        report['asteroid'] = {
            "size": diameter,
            "distance": distance,
            "speed": speed,
            "attack_points": asteroid_attack
        }

        attack_points = 0
        defense_items = list(planet.defense_items)
        shuffle(defense_items)

        report["defense"] = {}
        report["defense"]["items"] = {}
        for defense_item in defense_items:
            item_data = DefenseData.get_item(defense_item.label).get_level_info()
            attack = defense_item.quantity * item_data.attack

            report["defense"]["items"][defense_item.label] = {
                "label": defense_item.label,
                "type": defense_item.type,
                "quantity": defense_item.quantity,
                "attack_points": attack
            }

            attack_points += attack

        report["defense"]["general"] = {
            "attack_points": attack_points,
            "total_shots": 0,
            "missed_shots": 0,
            "hit_shots": 0,
            "accuracy": 0,
            "fail_rate": 0,
            "total_damage": 0,
        }

        # Actual attacking the asteroid
        # Shooting missing chance
        percentage_miss = 50
        asteroid_precision_info: BuildableItem = [x for x in planet.research_level if x.label == ResearchData.ASTEROID_PRECISION][0]

        percentage_miss -= asteroid_precision_info.current_level

        # Rounds
        rounds = math.floor(distance / speed)
        if attack_points > 0:
            for _ in range(rounds):
                # No damage left to do...
                if asteroid_attack <= 0:
                    break

                report["defense"]["general"]["total_shots"] += 100

                # miss chance
                if random.randint(1, 100) >= percentage_miss:
                    if attack_points > asteroid_attack:
                        attack_points = asteroid_attack

                    asteroid_attack -= attack_points
                    report["defense"]["general"]["total_damage"] += attack_points
                    report["defense"]["general"]["hit_shots"] += 100
                else:
                    report["defense"]["general"]["missed_shots"] += 100

            report["defense"]["general"]["accuracy"] = round(
                (report["defense"]["general"]["hit_shots"] / report["defense"]["general"]["total_shots"]) * 100, 2)
            report["defense"]["general"]["fail_rate"] = round(100 - report["defense"]["general"]["accuracy"], 2)

        # Damage defense structures
        report["result"] = {}
        for defense_item in defense_items:
            item_data = DefenseData.get_item(defense_item.label).get_level_info(0)
            item_health = item_data.health

            max_damage = math.floor(asteroid_attack * 0.4)
            max_kill = math.floor(max_damage / item_health)

            if max_kill >= 1:
                damage = random.randint(1, max_kill)

                # No damage to do here, lets do damage to other defense items! :)
                if defense_item.quantity <= 0:
                    continue

                old_quantity = defense_item.quantity
                if (defense_item.quantity - damage) <= 0:
                    damage = defense_item.quantity

                defense_item.quantity -= damage
                defense_item.health -= damage * item_health
                # defense_item.save()

                qty = round((defense_item.quantity / old_quantity) * 100, 2)

                report["result"][defense_item.label] = {
                    "damage_taken": damage,
                    "damage_taken_percentage": (100 - qty),
                    "label": defense_item.label,
                    "type": defense_item.type
                }

        # Damage resource buildings
        if asteroid_attack > 0:
            resource_levels = list(planet.resources_level)
            shuffle(resource_levels)

            for resource_level in resource_levels:
                # No more damage left
                if asteroid_attack <= 0:
                    break

                # No damage to do here, lets do damage to other buildings! :)
                if resource_level.health <= 0:
                    continue

                min_damage_building = math.floor(asteroid_attack * 0.2)
                max_damage_building = math.floor(asteroid_attack * 0.7)

                damage = random.randint(min_damage_building, max_damage_building)

                old_health = resource_level.health
                if (resource_level.health - damage) <= 0:
                    damage = resource_level.health

                resource_level.health -= damage
                health_percentage = round((resource_level.health / old_health) * 100, 2)

                report["result"][resource_level.label] = {
                    "damage_taken": damage,
                    "damage_taken_percentage": round((100 - health_percentage), 2),
                    "label": resource_level.label,
                    "type": resource_level.type
                }

                asteroid_attack -= damage

        planet = await self.planet_repository_port.update(planet)

        # No damage done, give XP
        if len(report["result"]) == 0:
            planet_tier = planet.tier.tier_code
            xp_boost = StakingData.DATA[planet_tier].experience_boost / 100

            experience = math.ceil((report["defense"]["general"]["total_damage"] / 10))
            experience = math.ceil(experience + (experience * xp_boost))

            await self.planet_level.give_planet_experience(GivePlanetExperienceRequest(planet_id=str(planet.id), experience_amount=experience))
            report["experience"] = {
                "experience": experience
            }

        await self.planet_email.create(PlanetSendEmailRequest(
            planet_id_receiver=str(planet.id),
            title="Asteroid Collision",
            sub_title="Howdy Rider! unfortunate news...",
            template="asteroid_collision",
            body=json.dumps(report),
            sender="Universe"
        ))

        return await self.response_port.publish_response(report)