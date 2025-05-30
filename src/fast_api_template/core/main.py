from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from src.fast_api_template.core.infra.database import create_db_and_tables
from src.fast_api_template.core.middlewares import add_middlewares
from src.fast_api_template.core.infra.base_router import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

add_middlewares(app)
app.include_router(router)
