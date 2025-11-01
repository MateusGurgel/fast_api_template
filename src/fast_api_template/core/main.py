from contextlib import asynccontextmanager
from typing import AsyncIterator

import stripe
from fastapi import FastAPI

from fast_api_template.core.infra.database import create_db_and_tables
from fast_api_template.core.infra.env import env
from fast_api_template.core.middlewares import add_middlewares
from fast_api_template.core.infra.base_router import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await create_db_and_tables()
    stripe.api_key = env.stripe_api_key
    yield


app = FastAPI(lifespan=lifespan)

add_middlewares(app)
app.include_router(router)
