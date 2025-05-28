from fastapi import FastAPI

from src.fast_api_template.core.middlewares import add_middlewares
from src.fast_api_template.core.router import router

app = FastAPI()

add_middlewares(app)

app.include_router(router)
