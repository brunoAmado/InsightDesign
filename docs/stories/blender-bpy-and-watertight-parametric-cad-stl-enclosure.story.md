---
slug: blender-bpy-and-watertight-parametric-cad-stl-enclosure
epic: insightdesign-3d-threejs-blender-cad-draw-and-games-engine
project: InsightDesign
chronicle_book: Book_Lit_Master_blender_onshape_3d_cad.md
labels:
- bdd
- three-amigos
- blender
- parametric-cad
- stl-manifold
---

# Blender bpy Automation Script & Watertight Manifold Parametric CAD .STL Compiler (`parametric_cad_stl` & `blender_bpy_script`)

### Narrative
As a **hardware CAD engineer (`CitySocket` & `CaptureNode`)**, I want to **compile watertight manifold ASCII .STL enclosures with CAS SHA-256 pointers (`cas://sha256/...`), bounding-box mm^3 volume calculation in Rust, and Blender bevel modifiers** so that **enclosures are immediately 3D-printable and verifiable via Hausdorff mesh comparison**.

### ChronicleRAG & Conversation Provenance
- **5-Tier Project Book**: `Book_Lit_Master_blender_onshape_3d_cad.md`
- **Primary AST Modules**: `insight_design/engine.py`, `rust_core/src/main.rs`
- ChronicleRAG Master Playbooks: `Book_Lit_Master_blender_onshape_3d_cad.md` (83 chapters on Blender, Onshape, Parametric CAD & 3D Printing) & `Three.js` / `React Three Fiber` books
- ChronicleRAG Code-First 3D & CAD Generators (`generate_code_first_3d_scene_or_explainer` & `compile_book_to_3d_didactic_lesson_or_cad`) and `CitySocket` / `CaptureNode` 3D magnetic enclosures (`3d printing iman` b4739a83)

### Acceptance Criteria

1. **Happy Path Execution**: `blender-bpy-and-watertight-parametric-cad-stl-enclosure` executes across `insight_design/engine.py`, `rust_core/src/main.rs` and returns a deterministic, schema-validated response.
2. **Unhappy Path & Input Validation**: Malformed, out-of-range, or unauthorized payloads are rejected with explicit `400`/`403` validation errors and zero side effects.
3. **PT/EU Statutory & Security Gate (`RULE-11`)**: `SecurityAuditAgent` and `InsightAudit (:4009)` confirm zero CWE/OWASP-LLM findings, CNPD/GDPR PII scrubbing (`Lei n.º 58/2019`), and `SHA-256` hash-chained audit receipt logging (`EU AI Act Art. 12`).

### Tasks
- [x] Mine architectural requirements from ChronicleRAG (`Book_Lit_Master_blender_onshape_3d_cad.md`) and conversation timeline
- [x] Generate Three-Amigos `docs/stories/blender-bpy-and-watertight-parametric-cad-stl-enclosure.story.md` and Gherkin `blender-bpy-and-watertight-parametric-cad-stl-enclosure.feature`
- [x] Verify metadata and Gherkin scenarios via `BusinessAnalystAgent.validate_story_metadata()`

---
🔗 Epic: [insightdesign-3d-threejs-blender-cad-draw-and-games-engine](../epics/insightdesign-3d-threejs-blender-cad-draw-and-games-engine.epic.md)  
🔗 Feature: [blender-bpy-and-watertight-parametric-cad-stl-enclosure.feature](blender-bpy-and-watertight-parametric-cad-stl-enclosure.feature)
