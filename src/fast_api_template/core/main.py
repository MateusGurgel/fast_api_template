from fastapi import FastAPI

from src.fast_api_template.core.router import router

app = FastAPI()

app.include_router(router)