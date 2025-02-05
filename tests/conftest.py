from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.__main__ import app
from src.core.session import get_session
from src.database.models.base import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"
BASE_URL = "http://127.0.0.1:8000"

engine = create_async_engine(DATABASE_URL)
TestingSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_session] = get_test_session


@pytest.fixture(autouse=True, scope="function")
async def init_session() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        yield session
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def test_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url=BASE_URL
    ) as client:
        yield client
