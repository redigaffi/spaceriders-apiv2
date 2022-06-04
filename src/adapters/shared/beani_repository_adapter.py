from __future__ import annotations
from beanie import PydanticObjectId, WriteRules, DeleteRules

from adapters.shared.beanie_models_adapter import EnergyDepositDocument, PlanetDocument, UserDocument, to_planet, \
    from_planet, EmailDocument, LevelUpRewardClaimsDocument
from core.shared.ports import UserRepositoryPort, PlanetRepositoryPort, EnergyDepositRepositoryPort, \
    EmailRepositoryPort, LevelUpRewardClaimsRepositoryPort
from core.shared.models import User, PlanetTier, Planet, UserNotFoundException, \
    LevelUpRewardClaims, EnergyDeposit, Email

from datetime import datetime, timezone


class LevelUpRewardClaimsRepositoryAdapter(LevelUpRewardClaimsRepositoryPort):
    async def create(self, lvl_up: LevelUpRewardClaims) -> LevelUpRewardClaims:
        lvl_up_document = LevelUpRewardClaimsDocument(level=lvl_up.level, completed=lvl_up.completed, planet_id=lvl_up.level)
        await lvl_up_document.save()
        return lvl_up_document.to_lvl_up()

    async def get(self, lvl_up_id: str) -> LevelUpRewardClaims|None:
        lvl_up = None
        try:
            lvl_up = await LevelUpRewardClaimsDocument.get(PydanticObjectId(lvl_up_id))
        except:
            pass

        if lvl_up is not None:
            return lvl_up.to_lvl_up()


class EmailRepositoryAdapter(EmailRepositoryPort):
    async def create(self, email: Email) -> Email:
        email_document = EmailDocument(title=email.title, sub_title=email.sub_title,template=email.template,
                                       body=email.body, sender=email.sender, read=email.read, planet=email.planet)

        await email_document.save()
        return email_document.to_email()

    async def update(self, email: Email) -> Email:
        email_document = EmailDocument.from_email(email)
        await email_document.save()
        fresh: EmailDocument = await EmailDocument.get(PydanticObjectId(email.id))
        return fresh.to_email()

    async def delete(self, email: Email):
        email_document: EmailDocument = await EmailDocument.get(PydanticObjectId(email.id))
        planet = await PlanetDocument.get(PydanticObjectId(email.planet))
        await planet.fetch_link(PlanetDocument.emails)
        planet.emails = [x.to_email() for x in planet.emails if str(x.id) != email.id]
        planet_document = from_planet(planet)
        await planet_document.save()
        await email_document.delete(link_rule=DeleteRules.DELETE_LINKS)

    async def get(self, email_id) -> Email:
        email = None
        try:
            email = await EmailDocument.get(PydanticObjectId(email_id))
        except:
            pass

        if email is not None:
            return email.to_email()


class EnergyDepositRepositoryAdapter(EnergyDepositRepositoryPort):

    async def get(self, id: str) -> EnergyDeposit | None:
        energy_deposit = None
        try:
            energy_deposit = await EnergyDepositDocument.get(PydanticObjectId(id))
        except:
            pass

        if energy_deposit is not None:
            return energy_deposit.to_energy_deposit()

    async def create_energy_deposit(self, energy_deposit: EnergyDeposit) -> EnergyDeposit:
        energy_document = EnergyDepositDocument(planet_id=energy_deposit.planet_id,
                                                was_recovered=energy_deposit.was_recovered,
                                                created_time=energy_deposit.created_time,
                                                token_amount=energy_deposit.token_amount,
                                                usd_value=energy_deposit.usd_value)

        if energy_deposit.id is not None:
            energy_document.id = PydanticObjectId(energy_deposit.id)

        await energy_document.save()

        return energy_document.to_energy_deposit()


class BeaniUserRepositoryAdapter(UserRepositoryPort):

    async def find_user(self, wallet: str) -> User | None:
        re = await UserDocument.find_one(UserDocument.wallet==wallet)
        if not re:
            return User()

        return User(id=re.id, wallet=wallet, username=re.username)

    async def find_user_or_throw(self, wallet: str) -> User:
        re = await UserDocument.find_one(UserDocument.wallet==wallet)

        if not re:
            raise UserNotFoundException()

        return User(id=re.id, wallet=re.wallet, username=re.username)

    async def create_user(self, wallet: str) -> User:
        user = UserDocument(wallet=wallet)
        await user.create()
        return User(id=user.id, wallet=wallet)


class BeaniPlanetRepositoryAdapter(PlanetRepositoryPort):

    async def all_claimed_planets(self) -> list[Planet]:

        planets = await PlanetDocument.find(PlanetDocument.claimed == True).to_list()
        return [await to_planet(planet) for planet in planets]

    async def all_user_planets(self, user_id: str) -> list[Planet]:
        planets = await PlanetDocument.find(PlanetDocument.user == user_id).to_list()
        return [await to_planet(planet) for planet in planets]

    async def update(self, planet: Planet) -> Planet:

        old: PlanetDocument = await PlanetDocument.get(PydanticObjectId(planet.id))
        old = from_planet(planet)
        await old.save()
        fresh: PlanetDocument = await PlanetDocument.get(PydanticObjectId(planet.id))
        return await to_planet(fresh)

    async def get_my_planet(self, user_id: str, planet_id: str) -> Planet | None:
        # if fetch_links provided energy_deposits comes null?
        # @README: seems like fetch_link works with emails but not with energy_deposits, only difference is that
        # on energy deposit we set our own id.
        planet = await PlanetDocument.find_one(
            PlanetDocument.id == PydanticObjectId(planet_id),
            PlanetDocument.user == user_id,
            #fetch_links=True
        )

        if planet is not None:
            return await to_planet(planet)

    async def get(self, planet_id: str) -> Planet | None:

        planet = await PlanetDocument.get(PydanticObjectId(planet_id))
        if planet is not None:
            return await to_planet(planet)

    async def has_free_planet(self, user_id: str) -> bool:

        free_planet = await PlanetDocument.find(PlanetDocument.user == user_id,
                                                PlanetDocument.price_paid == 0).limit(1).to_list()

        return len(free_planet) > 0

    async def last_created_planet(self) -> Planet | bool:

        last_planet = await PlanetDocument.all().sort(-PlanetDocument.created_at).limit(1).to_list()

        if not last_planet:
            return False

        return await to_planet(last_planet[0])

    async def create_planet(self, planet_data: Planet) -> Planet:

        user = await UserDocument.find_one(UserDocument.wallet==planet_data.user)

        planet_tier = PlanetTier()

        # id = bson.objectid.ObjectId()
        new_planet = PlanetDocument(
            name=planet_data.name,
            created_at=datetime.timestamp(datetime.now()),
            rarity=planet_data.rarity,
            image=planet_data.image,
            diameter=planet_data.diameter,
            level=0,
            experience=0,
            slots=planet_data.slots,
            slots_used=planet_data.slots_used,
            min_temperature=planet_data.min_temperature,
            max_temperature=planet_data.max_temperature,
            reserves=planet_data.reserves,
            original_total_metal_amount=planet_data.reserves.total_metal,
            original_total_crystal_amount=planet_data.reserves.total_crystal,
            original_total_petrol_amount=planet_data.reserves.total_petrol,
            galaxy=planet_data.galaxy,
            solar_system=planet_data.solar_system,
            position=planet_data.position,
            user=user.wallet,
            claimable=planet_data.claimable,
            claimed=planet_data.claimed,
            tier=planet_tier,
            resources=planet_data.resources,
            price_paid=planet_data.price_paid,
            free_tokens=0,
            resources_level=planet_data.resources_level,
            installation_level=planet_data.installation_level,
            research_level=planet_data.research_level,
            defense_items=planet_data.defense_items,
            pending_levelup_reward=[],
            energy_deposits=[]
        )

        await new_planet.save(link_rule=WriteRules.WRITE)
        user.planets.append(new_planet)
        await user.save(link_rule=WriteRules.WRITE)

        return await to_planet(new_planet)
