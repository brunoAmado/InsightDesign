Feature: Procedural Three.js WebGL/WebGPU 3D Scene & Orbit Camera Generator (`threejs_3d_scene`) (InsightDesign)
  As a 3D technical artist and digital-twin engineer
  I want to generate deterministic Three.js scenes with orbit camera rigs and ControlNet Depth/Normal/Wireframe passes
  So that smart-city nodes and didactic explainers render interactively in the browser at 60 FPS

  @positive @happy_path @chroniclerag
  Scenario: Happy path - Procedural Three.js WebGL/WebGPU 3D Scene & Orbit Camera Generator (`threejs_3d_scene`) succeeds with verified parameters
    Given the "InsightDesign" subsystem and epic "insightdesign-3d-threejs-blender-cad-draw-and-games-engine" are initialized
    And ChronicleRAG provenance from "Book_Lit_Master_blender_onshape_3d_cad.md" is active
    When the 3D technical artist and digital-twin engineer triggers "threejs-procedural-3d-scene-and-controlnet-pass-generator" with valid parameters
    Then the operation succeeds with deterministic output and appends an EU AI Act Art. 12 SHA-256 receipt

  @negative @unhappy_path @validation
  Scenario: Negative edge case - Procedural Three.js WebGL/WebGPU 3D Scene & Orbit Camera Generator (`threejs_3d_scene`) rejects malformed or out-of-bounds input
    Given the "InsightDesign" subsystem and epic "insightdesign-3d-threejs-blender-cad-draw-and-games-engine" are initialized
    When the 3D technical artist and digital-twin engineer triggers "threejs-procedural-3d-scene-and-controlnet-pass-generator" with empty or malformed parameters
    Then the system returns a 400 validation error without mutating state

  @security @pt_eu_compliance @rule_11
  Scenario: Security boundary - Procedural Three.js WebGL/WebGPU 3D Scene & Orbit Camera Generator (`threejs_3d_scene`) enforces CNPD/GDPR PII scrubbing and blocks injection payloads
    Given the SecurityAuditAgent, InsightAudit (:4009), and Blue-Team guards are active
    When an untrusted caller submits path traversal, prompt injection, or raw PT NIF/IBAN PII to "threejs-procedural-3d-scene-and-controlnet-pass-generator"
    Then sensitive tokens are scrubbed or blocked and a security audit event is recorded
