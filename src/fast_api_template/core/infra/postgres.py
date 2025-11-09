from contextlib import asynccontextmanager
from typing import AsyncGenerator, AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

engine = create_async_engine(str(env.postgres_url), echo=True)

@asynccontextmanager
async def get_session_with_context_manager() -> AsyncIterator[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session


async def create_db_and_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
