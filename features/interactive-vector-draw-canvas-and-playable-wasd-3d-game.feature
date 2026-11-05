Feature: Interactive 2D/3D Vector Draw Canvas & Playable WASD 3D Physics Game Studio (`interactive_draw_canvas` & `playable_3d_game`) (InsightDesign)
  As a interactive designer and simulation developer
  I want to render interactive SVG/HTML5 drawing canvases and playable WASD 3D physics game loops inside `<insight-design>`
  So that unifies interactive drawing, 3D simulation, and game prototyping in one service on :4024

  @positive @happy_path @chroniclerag
  Scenario: Happy path - Interactive 2D/3D Vector Draw Canvas & Playable WASD 3D Physics Game Studio (`interactive_draw_canvas` & `playable_3d_game`) succeeds with verified parameters
    Given the "InsightDesign" subsystem and epic "insightdesign-3d-threejs-blender-cad-draw-and-games-engine" are initialized
    And ChronicleRAG provenance from "Book_Lit_Master_blender_onshape_3d_cad.md" is active
    When the interactive designer and simulation developer triggers "interactive-vector-draw-canvas-and-playable-wasd-3d-game" with valid parameters
    Then the operation succeeds with deterministic output and appends an EU AI Act Art. 12 SHA-256 receipt

  @negative @unhappy_path @validation
  Scenario: Negative edge case - Interactive 2D/3D Vector Draw Canvas & Playable WASD 3D Physics Game Studio (`interactive_draw_canvas` & `playable_3d_game`) rejects malformed or out-of-bounds input
    Given the "InsightDesign" subsystem and epic "insightdesign-3d-threejs-blender-cad-draw-and-games-engine" are initialized
    When the interactive designer and simulation developer triggers "interactive-vector-draw-canvas-and-playable-wasd-3d-game" with empty or malformed parameters
    Then the system returns a 400 validation error without mutating state

  @security @pt_eu_compliance @rule_11
  Scenario: Security boundary - Interactive 2D/3D Vector Draw Canvas & Playable WASD 3D Physics Game Studio (`interactive_draw_canvas` & `playable_3d_game`) enforces CNPD/GDPR PII scrubbing and blocks injection payloads
    Given the SecurityAuditAgent, InsightAudit (:4009), and Blue-Team guards are active
    When an untrusted caller submits path traversal, prompt injection, or raw PT NIF/IBAN PII to "interactive-vector-draw-canvas-and-playable-wasd-3d-game"
    Then sensitive tokens are scrubbed or blocked and a security audit event is recorded
