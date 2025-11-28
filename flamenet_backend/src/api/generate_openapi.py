"""
Generate and write the OpenAPI schema for the FlameNet API.

This script imports the FastAPI application and writes its OpenAPI schema
to flamenet_backend/interfaces/openapi.json. It is intended to be run from
the repository root directory.
"""

import json
import os
import sys

# Ensure the flamenet_backend/src directory is on sys.path so imports work when
# executed from the repository root.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from api.main import app  # noqa: E402

# Get the OpenAPI schema
openapi_schema = app.openapi()

# Write to file inside the container root interfaces dir
container_root = os.path.dirname(BASE_DIR)
output_dir = os.path.join(container_root, "interfaces")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "openapi.json")

with open(output_path, "w") as f:
    json.dump(openapi_schema, f, indent=2)
