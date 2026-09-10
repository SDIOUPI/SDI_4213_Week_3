from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_route_returns_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the SDI 4213 automated testing lab"


def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_items_returns_count_and_items():
    response = client.get("/items")
    body = response.json()

    assert response.status_code == 200
    assert body["count"] == 2
    assert body["total_quantity"] == 8
    assert body["items"][0]["name"] == "Laptop"


def test_read_item_returns_one_item():
    response = client.get("/items/1")
    body = response.json()

    assert response.status_code == 200
    assert body["item"]["id"] == 1
    assert body["item"]["name"] == "Laptop"
    assert body["low_stock"] is False


def test_read_item_returns_404_for_missing_item():
    response = client.get("/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_add_item_creates_item():
    payload = {"id": 3, "name": "Webcam", "quantity": 7, "category": "equipment"}

    response = client.post("/items", json=payload)
    body = response.json()

    assert response.status_code == 201
    assert body["item"]["name"] == "Webcam"


def test_add_item_rejects_duplicate_id():
    payload = {"id": 1, "name": "Duplicate laptop", "quantity": 1, "category": "equipment"}

    response = client.post("/items", json=payload)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]
