"""
FlameNet Backend API module.

This module initializes and configures the FastAPI application for FlameNet.
It sets application-wide metadata, CORS, and exposes core health and metadata
endpoints used by the FlameNet frontend and tools.
"""

from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Define OpenAPI tags to organize the documentation view
openapi_tags = [
    {
        "name": "Health",
        "description": "System health and readiness checks for the FlameNet backend.",
    },
    {
        "name": "Meta",
        "description": "Metadata and version information for the FlameNet platform.",
    },
]

# Initialize the FastAPI application with FlameNet-specific metadata
app = FastAPI(
    title="FlameNet API",
    description="REST API for the FlameNet platform providing core backend services, health checks, and metadata.",
    version="0.1.0",
    openapi_tags=openapi_tags,
)

# Keep CORS permissive for local development and integration with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For localhost:3000 and dev usage; tighten for production if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get(
    "/",
    tags=["Health"],
    summary="Health Check",
    description="Returns a simple status payload indicating the FlameNet backend is running.",
    responses={
        200: {
            "description": "Application is healthy.",
            "content": {"application/json": {}},
        }
    },
)
def health_check() -> Dict[str, str]:
    """Basic health check endpoint for the FlameNet backend."""
    return {"message": "Healthy"}


# PUBLIC_INTERFACE
@app.get(
    "/meta",
    tags=["Meta"],
    summary="FlameNet Metadata",
    description=(
        "Returns basic metadata about the FlameNet backend including name, version, "
        "and a simple service status indicator."
    ),
    responses={
        200: {
            "description": "Metadata returned successfully.",
            "content": {"application/json": {}},
        }
    },
    operation_id="flamenet_meta_get",
)
def get_metadata() -> Dict[str, str]:
    """Return FlameNet service metadata including name, version, and status."""
    return {"name": "FlameNet", "version": app.version, "status": "ok"}
