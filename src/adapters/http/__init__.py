from core.shared.ports import ResponsePort


class HttpResponsePort(ResponsePort):
    async def publish_response(self, response):
        return response
