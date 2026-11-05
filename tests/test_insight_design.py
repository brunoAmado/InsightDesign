"""
Unit, Unhappy-Path & Regression Tests for `InsightDesign™` (`insight_design`).
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi.testclient import TestClient
from insight_design.engine import InsightDesignEngine, generate_design_artifact
from insight_design.server import app


class TestInsightDesign(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = InsightDesignEngine()
        self.client = TestClient(app)

    def test_01_health_status_and_supported_modes(self) -> None:
        r_health = self.client.get("/health")
        self.assertEqual(r_health.status_code, 200)
        self.assertEqual(r_health.json()["service"], "InsightDesign")
        self.assertEqual(r_health.json()["port"], 4024)

        r_status = self.client.get("/api/design/status")
        self.assertEqual(r_status.status_code, 200)
        self.assertTrue(r_status.json()["ok"])

        r_modes = self.client.get("/api/design/modes")
        self.assertEqual(r_modes.status_code, 200)
        self.assertIn("threejs_3d_scene", r_modes.json()["modes"])
        self.assertIn("parametric_cad_stl", r_modes.json()["modes"])
        self.assertIn("blender_bpy_script", r_modes.json()["modes"])
        self.assertIn("interactive_draw_canvas", r_modes.json()["modes"])
        self.assertIn("playable_3d_game", r_modes.json()["modes"])

    def test_02_execute_happy_path_3d_cad_blender_draw_and_game(self) -> None:
        r_exec = self.client.post(
            "/api/design/execute",
            json={
                "mode": "parametric_cad_stl",
                "prompt": "CitySocket IP65 enclosure",
                "dimensions_mm": {"width_mm": 100.0, "depth_mm": 50.0, "height_mm": 20.0},
            },
        )
        self.assertEqual(r_exec.status_code, 200)
        res = r_exec.json()
        self.assertTrue(res["ok"])
        self.assertEqual(res["member"], "InsightDesign")
        art = res["design_artifact"]
        self.assertTrue(art["watertight_manifold_mesh"])
        self.assertEqual(art["bounding_box_volume_mm3"], 100000.0)
        self.assertIn("THREE.Scene", art["threejs_scene_code"])
        self.assertIn("import bpy", art["blender_bpy_script"])
        self.assertIn("solid InsightDesignEnclosure", art["parametric_stl_preview"])
        self.assertIn("WASD_CONTROLS", art["playable_game_loop_js"])

        r_widget = self.client.get("/api/design/widget.js")
        self.assertEqual(r_widget.status_code, 200)
        self.assertIn("customElements.define('insight-design'", r_widget.text)

    def test_03_unhappy_path_unknown_mode_graceful_fallback(self) -> None:
        art = generate_design_artifact(mode="non_existent_mode")
        self.assertEqual(art["mode"], "threejs_3d_scene")
        self.assertTrue(art["cas_stl_uri"].startswith("cas://sha256/"))

    def test_04_unhappy_path_binary_blob_rejected_and_pii_scrubbed(self) -> None:
        bad_res = self.engine.execute({"raw_blob": "data:image/png;base64," + ("A" * 600)})
        self.assertFalse(bad_res["ok"])
        self.assertEqual(bad_res["error"], "BINARY_BLOB_REJECTED_USE_CAS_URI")

        r_scrub = self.client.post(
            "/api/design/scrub",
            json={"text": "NIF 123456789 e key sk-proj1234567890abcdef\u200b"},
        )
        self.assertEqual(r_scrub.status_code, 200)
        scrub_body = r_scrub.json()
        self.assertTrue(scrub_body["cnpd_gdpr_compliant"])
        self.assertNotIn("123456789", scrub_body["scrubbed_text"])


if __name__ == "__main__":
    unittest.main()
