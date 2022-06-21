import bson

from core.shared.models import Planet, Reserves, BuildableItem
from core.shared.static.game_data.Common import BuildableItemBaseType, BuildableItemLevelInfo
from core.shared.static.game_data.ResourceData import ResourceData
from core.shared.static.game_data.InstallationData import InstallationData
from core.shared.static.game_data.ResearchData import ResearchData
from core.shared.static.game_data.DefenseData import DefenseData
from core.shared.static.game_data.PlanetData import PlanetData
import random
import math


def resource_reserve_als(label: str, planet: Planet, next_level_info: BuildableItemLevelInfo) -> Planet:
    if label not in [ResourceData.METAL_MINE, ResourceData.CRYSTAL_MINE, ResourceData.PETROL_MINE]:
        return planet

    fields = {
        ResourceData.METAL_MINE: {
            'total_reserve': 'original_total_metal_amount',
            'reserve_left': 'total_metal',
            'visible_reserve': 'metal'
        },
        ResourceData.CRYSTAL_MINE: {
            'total_reserve': 'original_total_crystal_amount',
            'reserve_left': 'total_crystal',
            'visible_reserve': 'crystal'
        },
        ResourceData.PETROL_MINE: {
            'total_reserve': 'original_total_petrol_amount',
            'reserve_left': 'total_petrol',
            'visible_reserve': 'petrol'
        },
    }

    reserve_upgrade_percentage = next_level_info.new_reserve_found_percentage
    total_reserve = getattr(planet, fields[label]['total_reserve'])
    reserve_left = getattr(planet.reserves, fields[label]['reserve_left'])
    visible_reserve = getattr(planet.reserves, fields[label]['visible_reserve'])

    next_visible_reserve = total_reserve * (reserve_upgrade_percentage / 100)

    setattr(planet.reserves, fields[label]['reserve_left'], reserve_left - next_visible_reserve)
    setattr(planet.reserves, fields[label]['visible_reserve'], visible_reserve + next_visible_reserve)

    return planet


def get_new_planet(user: str, name: str, last_planet: Planet, price_paid: int, planet_images_bucket_path: str,
                   claimed: bool, claimable: int = None) -> Planet:
    galaxy, solar_system, position = get_new_planet_position(last_planet)

    resource_levels, installation_level, research_level, defense_items = create_levels()

    (
        initial_reserve, image, rarity, diameter, slots, metal_mine_amount, crystal_mine_amount,
        petrol_mine_amount, min_temperature, max_temperature
    ) = get_planet_data(is_free=True)

    planet = Planet(user=user,
                    price_paid=price_paid,
                    name=name,
                    rarity=rarity,
                    resources_level=resource_levels,
                    installation_level=installation_level,
                    research_level=research_level,
                    defense_items=defense_items)

    planet.reserves = Reserves()
    planet.position = position
    planet.solar_system = solar_system
    planet.galaxy = galaxy
    planet.resources.metal = initial_reserve["metal"]
    planet.resources.petrol = initial_reserve["petrol"]
    planet.resources.crystal = initial_reserve["crystal"]
    planet.resources.energy = initial_reserve["energy"]
    planet.image = image
    planet.set_image_url(planet_images_bucket_path)
    planet.diameter = diameter
    planet.slots = slots
    planet.slots_used = 7
    planet.min_temperature = min_temperature
    planet.max_temperature = max_temperature

    planet.reserves.total_metal = metal_mine_amount
    planet.reserves.total_crystal = crystal_mine_amount
    planet.reserves.total_petrol = petrol_mine_amount

    planet.original_total_metal_amount = metal_mine_amount
    planet.original_total_crystal_amount = crystal_mine_amount
    planet.original_total_petrol_amount = petrol_mine_amount

    planet.claimed = claimed
    planet.claimable = claimable

    return planet


def get_new_planet_position(latest_planet: Planet | bool) -> tuple:
    galaxy = 0
    solar_system = 0
    position = 1

    if latest_planet:
        position = latest_planet.position + 1
        solar_system = latest_planet.solar_system
        galaxy = latest_planet.galaxy

        if position > 13:
            position = 1
            solar_system += 1

            if solar_system > 100:
                solar_system = 0
                galaxy += 1

    return galaxy, solar_system, position


def get_planet_data(is_free: bool):
    rarity = random.choices(PlanetData.RARITIES, weights=PlanetData.RARITY_WEIGHTS, k=1)[0]

    if is_free:
        rarity = PlanetData.UNCOMMON

    image = f"{random.randint(1, PlanetData.IMAGES)}"
    diameter_range = PlanetData.DATA[rarity]["diameter"]["range"]
    diameter = random.randint(diameter_range[0], diameter_range[1])
    slots = math.floor(diameter / 1000)

    reserve_range = PlanetData.DATA[rarity]["reserves"]["range"]
    metal_mine_amount = random.randint(reserve_range[0], reserve_range[1])
    crystal_mine_amount = random.randint(reserve_range[0], reserve_range[1])
    petrol_mine_amount = random.randint(reserve_range[0], reserve_range[1])

    min_temperature = random.randint(-60, 0)
    max_temperature = random.randint(1, 150)

    return PlanetData.DATA[rarity]["initial_resources"], image, rarity, diameter, slots, metal_mine_amount, \
           crystal_mine_amount, petrol_mine_amount, min_temperature, max_temperature


def create_levels() -> tuple:
    resource_levels = []
    installation_level = []
    research_level = []
    defense_items = []

    for resource_data in ResourceData.TYPES:
        item: BuildableItemBaseType = ResourceData.get_item(resource_data)
        level_info: BuildableItemLevelInfo = item.get_level_info()

        rl = BuildableItem(label=item.label,
                           type=ResourceData.TYPE,
                           current_level=0,
                           health=level_info.health )
        resource_levels.append(rl)

    for installation_type in InstallationData.TYPES:
        item: BuildableItemBaseType = InstallationData.get_item(installation_type)
        il = BuildableItem(label=item.label, type=InstallationData.TYPE, current_level=0)
        installation_level.append(il)

    for research_type in ResearchData.TYPES:
        item: BuildableItemBaseType = ResearchData.get_item(research_type)
        rl = BuildableItem(label=item.label, type=ResearchData.TYPE, current_level=0)
        research_level.append(rl)

    for defense_item in DefenseData.TYPES:
        di = BuildableItem(label=defense_item, type=DefenseData.TYPE, quantity=0)
        defense_items.append(di)

    return resource_levels, installation_level, research_level, defense_items
