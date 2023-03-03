import logging as log

from beanie import init_beanie
import beanie.exceptions
from decouple import config
from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
import motor.motor_asyncio
from starlette.background import BackgroundTask
from starlette.middleware.base import BaseHTTPMiddleware

# Info, seems like this need to be at the top, also some have src before and others not (maybe due to relationship?)
from adapters.shared.beanie_models_adapter import (
    BKMTransactionDocument,
    CurrencyMarketOrderDocument,
    CurrencyMarketTradeDocument,
    EmailDocument,
    EnergyDepositDocument,
    PlanetDocument,
    UserDocument, VoucherDocument,
)
import apps.http.dependencies as dependencies
from apps.http.dependencies import get_middleware
import apps.http.settings
from apps.http.urls import register_fastapi_routes
from core.buildable_items import FinishBuildRequest
from core.planet_resources import PlanetResourcesUpdateRequest
from core.shared.models import AppBaseException
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
import elasticapm
import logging

# @TODO: Add logger port
# @TODO: Websockets: https://github.com/tiangolo/fastapi/issues/685 --- https://fastapi.tiangolo.com/advanced/websockets/

app = FastAPI()
# apm_logger = logging.getLogger("elasticapm")
# apm_logger.setLevel(logging.DEBUG)


# https://fastapi.tiangolo.com/tutorial/metadata/


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SpaceRiders API",
        version="2.0.0",
        description="SpaceRiders API",
        routes=app.routes,
    )
    # openapi_schema["info"]["x-logo"] = {
    #     "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    # }
    openapi_schema["paths"]["/jwt"]["post"][
        "description"
    ] = "Get a JWT token to access protected resources"
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


async def exception_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        apm.capture_exception()

        if isinstance(exc, AppBaseException):
            return JSONResponse(
                status_code=exc.code,
                content={"message": exc.msg},
            )

        if isinstance(exc, beanie.exceptions.RevisionIdWasChanged):
            log.critical("revision id changed", exc)

            return await call_next(request)

        log.critical("Something unexpected happened", exc)
        return JSONResponse(
            status_code=500,
            content={"message": "Error, something went wrong..."},
        )


# FastAPI hack to send back cors headers on exceptions. https://github.com/tiangolo/fastapi/issues/775
app.middleware("http")(exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)




class MyBaseHTTPMiddleware(BaseHTTPMiddleware):
    async def __call__(self, scope, receive, send):
        try:
            await super().__call__(scope, receive, send)
        except RuntimeError as exc:
            if str(exc) == "No response returned.":
                request = Request(scope, receive=receive)
                if await request.is_disconnected():
                    return
            raise

    async def dispatch(self, request, call_next):
        raise NotImplementedError()


class UpdateDataMiddleWare(MyBaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            if request.method == "OPTIONS":
                return await call_next(request)

            (
                items_use_case,
                planet_resources_use_case,
                planet_staking,
            ) = await get_middleware()
            active_planet = request.headers.get("x-active-planet")
            if active_planet is not None:
                await planet_staking.tier_expired_reset(planet_id=active_planet)
                await items_use_case.finish_item(
                    FinishBuildRequest(planet_id=active_planet)
                )
                await planet_resources_use_case(
                    PlanetResourcesUpdateRequest(planet_id=active_planet)
                )
        except Exception as e:
            pass

        return await call_next(request)


app.add_middleware(UpdateDataMiddleWare)

apm = elasticapm.get_client()
if apm is None:
    apm = make_apm_client({
        'SERVICE_NAME': 'spaceriders-api',
        'SERVER_URL': 'http://apmserver:8200',
        'ENVIRONMENT': config('ENV')
    })
app.add_middleware(ElasticAPM, client=apm)


@app.on_event("startup")
async def app_init():
    await dependencies.logging_adapter.info("App started v2")

    client = motor.motor_asyncio.AsyncIOMotorClient(
        host=config("DB_URL"),
        # username="root",
        # password="example"
    )

    db = client[config("DB_NAME")]
    await init_beanie(
        database=db,
        document_models=[
            UserDocument,
            EnergyDepositDocument,
            BKMTransactionDocument,
            PlanetDocument,
            EmailDocument,
            CurrencyMarketOrderDocument,
            CurrencyMarketTradeDocument,
            VoucherDocument
        ],
    )

    http_controller = await dependencies.http_controller()
    urls = await register_fastapi_routes(http_controller)
    for url in urls:
        app.router.add_api_route(**url)


# if __name__ == "__main__":
#    uvicorn.run("__main__:app", port=8010, host='0.0.0.0', reload=True, workers=1, debug=True)
