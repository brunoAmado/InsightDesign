"""
Standalone FastAPI Server for `InsightDesign™` (`python -m insight_design.server`).
Runs on port 4024 by default.
"""

import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from insight_design.router import mount_insight_design_plugin

app = FastAPI(
    title="InsightDesign™ — 3D Three.js, Blender bpy, Parametric CAD (.STL), Interactive Draw & Playable Games Engine",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

mount_insight_design_plugin(app, prefix="/api/design")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "InsightDesign",
        "port": 4024,
        "api_prefix": "/api/design",
        "version": "1.0.0",
    }


def main() -> None:
    port = int(os.environ.get("INSIGHT_DESIGN_PORT", "4024"))
    uvicorn.run(app, host="127.0.0.1", port=port)


if __name__ == "__main__":
    main()
