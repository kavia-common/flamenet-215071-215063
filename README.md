# flamenet-215071-215063

## Backend tests (FlameNet)

Pytest-based tests are included for the FastAPI backend to validate health, metadata, and OpenAPI schema.

- Location: `flamenet_backend/tests`
- Requirements: packages are listed in `flamenet_backend/requirements.txt`
- Run tests from the backend container root:

```bash
cd flamenet-215071-215063/flamenet_backend
pytest -q
```

This executes:
- `test_health.py` — validates `/` (health) and `/meta`
- `test_openapi.py` — validates OpenAPI availability and title "FlameNet API"