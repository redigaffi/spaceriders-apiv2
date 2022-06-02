from core.shared.ports import ResponsePort


class BlackHoleResponsePort(ResponsePort):
    async def publish_response(self, response) -> str:
        pass
