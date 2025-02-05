from src.common.dto.category import CategoryDTO

from .conftest import test_client  # noqa


async def create_category(name: str, test_client):
    cat = CategoryDTO(name=name)
    response = await test_client.post("/categories", json=cat.model_dump())
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert json_content["name"] == cat.name
    return json_content["id"]


async def test_create_category(test_client):
    await create_category("test_category", test_client)


async def test_get_category(test_client):
    category_id = await create_category("test_category", test_client)

    response = await test_client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert json_content["id"] == category_id


async def test_get_categories(test_client):
    category_ids = {
        await create_category(f"test_category_{i}", test_client)
        for i in range(10)
    }
    response = await test_client.get("/categories")
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, list)
    assert len(json_content) == len(category_ids)
    assert {c["id"] for c in json_content} == category_ids


async def test_get_categories_with_query_params(test_client):
    category_ids = [
        await create_category(f"test_category_{i}", test_client)
        for i in range(15)
    ]
    offset = 7
    limit = 5
    params = dict(offset=offset, limit=limit)
    response = await test_client.get("/categories", params=params)
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, list)
    assert len(json_content) == limit
    expected = category_ids[offset : offset + limit]
    assert {c["id"] for c in json_content} == set(expected)


async def test_delete_category(test_client):
    category_id = await create_category("test_category", test_client)

    response = await test_client.delete(f"/categories/{category_id}")
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert json_content["id"] == category_id

    response = await test_client.get(f"/categories/{category_id}")
    assert response.status_code == 404
