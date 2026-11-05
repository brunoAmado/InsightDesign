Feature: Blender bpy Automation Script & Watertight Manifold Parametric CAD .STL Compiler (`parametric_cad_stl` & `blender_bpy_script`) (InsightDesign)
  As a hardware CAD engineer (`CitySocket` & `CaptureNode`)
  I want to compile watertight manifold ASCII .STL enclosures with CAS SHA-256 pointers (`cas://sha256/...`), bounding-box mm^3 volume calculation in Rust, and Blender bevel modifiers
  So that enclosures are immediately 3D-printable and verifiable via Hausdorff mesh comparison

  @positive @happy_path @chroniclerag
  Scenario: Happy path - Blender bpy Automation Script & Watertight Manifold Parametric CAD .STL Compiler (`parametric_cad_stl` & `blender_bpy_script`) succeeds with verified parameters
    Given the "InsightDesign" subsystem and epic "insightdesign-3d-threejs-blender-cad-draw-and-games-engine" are initialized
    And ChronicleRAG provenance from "Book_Lit_Master_blender_onshape_3d_cad.md" is active
    When the hardware CAD engineer (`CitySocket` & `CaptureNode`) triggers "blender-bpy-and-watertight-parametric-cad-stl-enclosure" with valid parameters
    Then the operation succeeds with deterministic output and appends an EU AI Act Art. 12 SHA-256 receipt

  @negative @unhappy_path @validation
  Scenario: Negative edge case - Blender bpy Automation Script & Watertight Manifold Parametric CAD .STL Compiler (`parametric_cad_stl` & `blender_bpy_script`) rejects malformed or out-of-bounds input
    Given the "InsightDesign" subsystem and epic "insightdesign-3d-threejs-blender-cad-draw-and-games-engine" are initialized
    When the hardware CAD engineer (`CitySocket` & `CaptureNode`) triggers "blender-bpy-and-watertight-parametric-cad-stl-enclosure" with empty or malformed parameters
    Then the system returns a 400 validation error without mutating state

  @security @pt_eu_compliance @rule_11
  Scenario: Security boundary - Blender bpy Automation Script & Watertight Manifold Parametric CAD .STL Compiler (`parametric_cad_stl` & `blender_bpy_script`) enforces CNPD/GDPR PII scrubbing and blocks injection payloads
    Given the SecurityAuditAgent, InsightAudit (:4009), and Blue-Team guards are active
    When an untrusted caller submits path traversal, prompt injection, or raw PT NIF/IBAN PII to "blender-bpy-and-watertight-parametric-cad-stl-enclosure"
    Then sensitive tokens are scrubbed or blocked and a security audit event is recorded
