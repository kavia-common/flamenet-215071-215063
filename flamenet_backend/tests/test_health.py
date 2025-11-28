"""
Tests for health and metadata endpoints of the FlameNet FastAPI backend.
"""

from fastapi.testclient import TestClient

# Import the application object from the backend entrypoint
from src.api.main import app  # noqa: E402


client = TestClient(app)


def test_health_endpoint_returns_200_and_expected_payload():
    # PUBLIC_INTERFACE
    """
    Verify that GET / returns 200 and the expected JSON payload structure.
    """
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    # Expected minimal payload
    assert isinstance(data, dict)
    assert data.get("message") == "Healthy"


def test_meta_endpoint_returns_name_version_and_status():
    # PUBLIC_INTERFACE
    """
    Verify that GET /meta returns 200 and includes name, version, and status.
    Ensure the project name is 'FlameNet'.
    """
    resp = client.get("/meta")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data.get("name") == "FlameNet"
    # Version should match app.version
    assert data.get("version") == app.version
    # Status should be ok
    assert data.get("status") == "ok"
