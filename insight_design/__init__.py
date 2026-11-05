"""
`InsightDesign™` (`insight_design`) — 3D Three.js, Blender, Parametric CAD (`.STL`), Interactive Draw, Playable Games & Open-Source Canva Brand/Slidev Deck Engine (`:4024 /api/design`).
"""

from insight_design.engine import (
    SUPPORTED_DESIGN_MODES,
    InsightDesignEngine,
    export_open_source_canva_brand_and_slidev_deck,
    generate_design_artifact,
)

__version__ = "1.1.0"

__all__ = [
    "InsightDesignEngine",
    "SUPPORTED_DESIGN_MODES",
    "__version__",
    "export_open_source_canva_brand_and_slidev_deck",
    "generate_design_artifact",
]
