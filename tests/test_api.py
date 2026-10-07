from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_order_returns_order_data():
    response = client.get("/orders/12345")

    assert response.status_code == 200

    data = response.json()

    assert data["order_id"] == "12345"
    assert data["status"] == "shipped"
    assert data["tracking_number"] == "TRK123456"
    assert data["estimated_delivery"] == "2026-10-05"


def test_get_order_accepts_string_order_id():
    response = client.get("/orders/ABC-123")

    assert response.status_code == 200
    assert response.json()["order_id"] == "ABC-123"


def test_get_order_with_empty_order_id_returns_not_found():
    response = client.get("/orders/")

    assert response.status_code == 404
