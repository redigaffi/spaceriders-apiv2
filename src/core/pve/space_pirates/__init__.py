import json
import math
from dataclasses import dataclass
import random

from core.planet_email import PlanetEmail, PlanetSendEmailRequest
from core.planet_level import PlanetLevel
from core.shared.models import BuildableItem
from core.shared.ports import ResponsePort, PlanetRepositoryPort
from pydantic import BaseModel

from core.shared.static.game_data.DefenseData import DefenseData
from core.shared.static.game_data.ResearchData import ResearchData
from core.shared.static.game_data.SpacePiratesData import SpacePiratesData


class SpacePirateRequest(BaseModel):
    planet_id: str


@dataclass
class SpacePirates:
    planet_repository_port: PlanetRepositoryPort
    planet_level: PlanetLevel
    planet_email: PlanetEmail
    response_port: ResponsePort

    async def __call__(self, request: SpacePirateRequest):
        report = {}

        planet = await self.planet_repository_port.get(request.planet_id)

        try:
            amount, distance, speed, health, steal_per_space_ship = SpacePiratesData.get_space_pirate_data_level(
                planet.level)
        except:
            print("error retrieving space pirate information, planet outside of space pirate level range")
            return

        total_health = amount * health

        attack_points = 0
        defense_items = list(planet.defense_items)
        random.shuffle(defense_items)

        report["general"] = {
            "amount_space_ships": amount,
            "distance": distance,
            "speed": speed,
            "health_per_ship": health,
            "total_health": total_health
        }

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
        percentage_miss = 80
        asteroid_precision_info: BuildableItem = [x for x in planet.research_level if x.label ==
                                                  ResearchData.ASTEROID_PRECISION][0]

        percentage_miss -= asteroid_precision_info.current_level * 3

        # Rounds
        rounds = math.floor(distance / speed)
        report["general"]["rounds"] = rounds

        if attack_points > 0:
            for _ in range(rounds):

                report["defense"]["general"]["total_shots"] += 100

                # miss chance
                if random.randint(1, 100) >= percentage_miss:
                    if attack_points > total_health:
                        attack_points = total_health

                    total_health -= attack_points
                    report["defense"]["general"]["total_damage"] += attack_points
                    report["defense"]["general"]["hit_shots"] += 100
                else:
                    report["defense"]["general"]["missed_shots"] += 100

            report["defense"]["general"]["accuracy"] = round((report["defense"]["general"]["hit_shots"] /
                                                              report["defense"]["general"]["total_shots"]) * 100, 2)

            report["defense"]["general"]["fail_rate"] = round(100 - report["defense"]["general"]["accuracy"], 2)

        space_pirates_left = math.ceil(total_health / health)
        total_to_steal = round(steal_per_space_ship * space_pirates_left, 2)
        if space_pirates_left > 0:
            total_to_steal_left = total_to_steal

            resources_to_steal = [0, 0, 0]  # metal, crystal, petrol (in that order)
            resource = 0
            max_multiplier = 0.4
            i = 0
            while total_to_steal_left > 0:

                steal_amount = total_to_steal_left

                if total_to_steal_left >= 100:
                    min_to_steal = round(total_to_steal_left * 0.2, 2)

                    if max_multiplier <= 0.8:
                        max_multiplier += i

                    max_to_steal = round(total_to_steal_left * max_multiplier, 2)
                    steal_amount = round(random.uniform(min_to_steal, max_to_steal), 2)

                total_to_steal_left -= steal_amount
                resources_to_steal[resource] += round(steal_amount, 2)

                if resource == 2:
                    resource = 0

                resource += 1
                i += 0.01

            if planet.resources.metal >= resources_to_steal[0]:
                planet.resources.metal -= resources_to_steal[0]
            else:
                total_to_steal -= resources_to_steal[0]
                total_to_steal += planet.resources.metal

                resources_to_steal[0] = planet.resources.metal
                planet.resources.metal = 0

            if planet.resources.crystal >= resources_to_steal[1]:
                planet.resources.crystal -= resources_to_steal[1]
            else:
                total_to_steal -= resources_to_steal[1]
                total_to_steal += planet.resources.crystal

                resources_to_steal[1] = planet.resources.crystal
                planet.resources.crystal = 0

            if planet.resources.petrol >= resources_to_steal[2]:
                planet.resources.petrol -= resources_to_steal[2]
            else:
                total_to_steal -= resources_to_steal[2]
                total_to_steal += planet.resources.petrol

                resources_to_steal[2] = planet.resources.petrol
                planet.resources.petrol = 0

            await self.planet_repository_port.update(planet)

            report["result"] = {}
            report["result"]["ships_left"] = space_pirates_left
            report["result"]["total_health_ships_left"] = total_health

            report["result"]["loss"] = {}

            report["result"]["loss"]["total"] = total_to_steal
            report["result"]["loss"]["metal"] = resources_to_steal[0]
            report["result"]["loss"]["crystal"] = resources_to_steal[1]
            report["result"]["loss"]["petrol"] = resources_to_steal[2]

        await self.planet_email.create(PlanetSendEmailRequest(
            planet_id_receiver=str(planet.id),
            title="Space Pirates invasion",
            sub_title="Howdy Rider! unfortunate news...",
            template="space_pirates",
            body=json.dumps(report),
            sender="Universe"
        ))
