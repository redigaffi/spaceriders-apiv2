from dataclasses import dataclass

from pydantic import BaseModel

from core.shared.models import Email, AppBaseException
from core.shared.ports import ResponsePort, EmailRepositoryPort, PlanetRepositoryPort


class EmailNotFoundException(AppBaseException):
    msg = "Email not found"


@dataclass
class PlanetEmails:
    planet_repository_port: PlanetRepositoryPort
    email_repository_port: EmailRepositoryPort
    response_port: ResponsePort

    async def create(self, planet_id: str):
        planet = await self.planet_repository_port.get(planet_id)
        email = Email(title="asd",sub_title="asd",template="asd",body="asd",sender="as",read=False,planet=planet_id)
        email = await self.email_repository_port.create(email)
        planet.emails.append(email)
        await self.planet_repository_port.update(planet)

        return await self.response_port.publish_response(email)

    async def mark_as_read(self, email_id: str):
        email: Email = await self.email_repository_port.get(email_id)

        if email is None:
            raise EmailNotFoundException()

        email.read = True
        await self.email_repository_port.update(email)
        return await self.response_port.publish_response({})

    async def delete(self, email_id: str):
        email: Email = await self.email_repository_port.get(email_id)

        if email is None:
            raise EmailNotFoundException()

        await self.email_repository_port.delete(email)
        return await self.response_port.publish_response({})

