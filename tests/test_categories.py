from pprint import pprint
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from fastapi.testclient import TestClient

from src.__main__ import app
from src.core.session import get_session
from src.database.models.base import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"
client = TestClient(app)


async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(DATABASE_URL, echo=False)
    TestingSessionLocal = async_sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with TestingSessionLocal() as session:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        yield session

app.dependency_overrides[get_session] = get_test_session


def test_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    pprint(response.json(), sort_dicts=False)
