"""
FastAPI `APIRouter` Plugin for `InsightDesign™` (`insight_design.router`).
Can be mounted standalone (`:4024`) or inside `ChronicleRAG` (`:8765`).
"""

from typing import Any, Dict
from fastapi import APIRouter, Body, FastAPI, Query
from fastapi.responses import JSONResponse, Response

from insight_design.engine import (
    InsightDesignEngine,
    SUPPORTED_DESIGN_MODES,
    export_open_source_canva_brand_and_slidev_deck,
    generate_product_surface_flow_atlas,
)


def create_insight_design_router() -> APIRouter:
    engine = InsightDesignEngine()
    router = APIRouter(tags=["InsightDesign"])

    @router.get("/status")
    def get_status() -> Dict[str, Any]:
        return engine.get_status()

    @router.get("/modes")
    def get_modes() -> Dict[str, Any]:
        return {"ok": True, "modes": SUPPORTED_DESIGN_MODES}

    @router.get("/brand-deck")
    def get_open_source_canva_deck(
        title: str = Query(default="SetMiddle Smart-City & Família Insights™ Pitch Deck"),
        subtitle: str = Query(default="100% Open-Source SVG + Slidev / Marp Deck"),
    ) -> Dict[str, Any]:
        return export_open_source_canva_brand_and_slidev_deck(title=title, subtitle=subtitle)

    @router.post("/execute")
    def execute_action(payload: Dict[str, Any] = Body(default={})) -> Dict[str, Any]:
        return engine.execute(payload)

    @router.post("/parametric-mold")
    def generate_parametric_mold_and_game_plan(payload: Dict[str, Any] = Body(default={})) -> Dict[str, Any]:
        req = dict(payload or {})
        req.setdefault("mode", "onshape_parametric_mold_plan")
        return engine.execute(req)

    @router.post("/surface-atlas")
    def post_surface_flow_atlas(payload: Dict[str, Any] = Body(default={})) -> Any:
        res = generate_product_surface_flow_atlas(
            title=str(payload.get("title", "SetMiddle 4-Axis Product-Surface & User-Flow Atlas")),
            surfaces=payload.get("surfaces"),
            features=payload.get("features"),
            entities=payload.get("entities"),
        )
        return res if res.get("ok") else JSONResponse(status_code=400, content=res)

    @router.post("/scrub")
    def scrub_text(payload: Dict[str, Any] = Body(default={})) -> Dict[str, Any]:
        return engine.scrub_input(str(payload.get("text", "")))

    @router.get("/widget.js")
    def get_web_component_js() -> Response:
        js = """
(function() {
  if (typeof window === 'undefined' || customElements.get('insight-design')) return;
  class InsightDesignElement extends HTMLElement {
    connectedCallback() {
      const apiBase = this.getAttribute('api-base') || '/api/design';
      this.innerHTML = `<section role="region" aria-label="InsightDesign Widget" style="background:#0f172a;color:#f8fafc;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:16px;font-family:Inter,system-ui,sans-serif;"><h3 style="margin:0;font-size:15px;font-weight:600;">InsightDesign™ (3D · Blender · CAD · Draw · Games · Slidev/SVG)</h3><div aria-live="polite" style="font-size:12px;color:#94a3b8;margin-top:6px;font-variant-numeric:tabular-nums;">Active on ${apiBase}</div></section>`;
    }
  }
  customElements.define('insight-design', InsightDesignElement);
})();
""".strip()
        return Response(content=js, media_type="application/javascript")

    return router


def mount_insight_design_plugin(app: FastAPI, prefix: str = "/api/design") -> bool:
    app.include_router(create_insight_design_router(), prefix=prefix)
    return True
