from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_redirects_to_docs():
    response = client.get("/", follow_redirects=False)
    assert response.status_code in (307, 308)
    assert response.headers["location"] == "/docs"


def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "X-Request-ID" in response.headers


def test_versioned_openapi_is_available():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "/api/v1/health" in response.text
