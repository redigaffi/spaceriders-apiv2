from dataclasses import dataclass

from pydantic import BaseModel

from core.shared.models import Email
from core.shared.ports import ResponsePort, EmailRepositoryPort, PlanetRepositoryPort


class OpenseaAttributeStandardResponse(BaseModel):
    display_type: str = None
    trait_type: str = None
    value: str = None


@dataclass
class PlanetEmails:
    planet_repository_port: PlanetRepositoryPort
    email_repository_port: EmailRepositoryPort
    response_port: ResponsePort

    async def asd(self, planet_id: str):
        planet = await self.planet_repository_port.get(planet_id)

        email = Email(title="asd",sub_title="asd",template="asd",body="asd",sender="as",read=False,planet=planet_id)
        email = await self.email_repository_port.create(email)
        planet.emails.append(email)
        await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(email)

