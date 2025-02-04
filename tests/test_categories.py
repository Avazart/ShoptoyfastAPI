from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool

from src.__main__ import app
from src.common.dto.category import CategoryDTO
from src.core.session import get_session
from src.database.models.base import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"
BASE_URL = "http://127.0.0.1:8000"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@pytest.fixture()
async def test_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url=BASE_URL,
    ) as client:
        yield client


async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
    TestingSessionLocal = async_sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with TestingSessionLocal() as session:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        yield session


app.dependency_overrides[get_session] = get_test_session


async def test_categories(test_client):
    cat = CategoryDTO(name="test_category")
    response = await test_client.post("/categories", json=cat.model_dump())
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert json_content["name"] == cat.name

    response = await test_client.get("/categories")
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, list)
    assert len(json_content) == 1
    assert json_content[0]["name"] == cat.name
    category_id = json_content[0]["id"]

    response = await test_client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert json_content["name"] == cat.name
    assert json_content["id"] == category_id

    response = await test_client.delete(f"/categories/{category_id}")
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert json_content["id"] == category_id

    response = await test_client.get(f"/categories/{category_id}")
    assert response.status_code == 404
