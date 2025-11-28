"""
Tests for OpenAPI schema availability and metadata of the FlameNet FastAPI backend.
"""

from fastapi.testclient import TestClient

# Import the application object from the backend entrypoint
from src.api.main import app  # noqa: E402


client = TestClient(app)


def test_openapi_json_endpoint_available_and_contains_title():
    # PUBLIC_INTERFACE
    """
    Verify that /openapi.json is available and includes the correct API title.
    """
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    schema = resp.json()
    assert isinstance(schema, dict)
    info = schema.get("info") or {}
    assert info.get("title") == "FlameNet API"


def test_docs_served_and_paths_include_health_and_meta():
    # PUBLIC_INTERFACE
    """
    Verify that the OpenAPI schema includes expected paths for '/' and '/meta'.
    """
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    schema = resp.json()
    paths = schema.get("paths") or {}
    assert "/" in paths
    assert "/meta" in paths
