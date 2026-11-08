@setmiddle_tenant @dev_latest_modules @ux_engine_2_8 @no_feature_placeholders
Feature: InsightDesign Reverse-Engineered Contract, Live DEV Module Resolution & Anti-AI-Slop UI Certification
  As the SetMiddle Dev Team (setmiddle-dev-team)
  I want InsightDesign (InsightDesign™ — 3D Three.js, Blender bpy, Parametric CAD .STL & Slidev Deck) certified with BDD scenarios and zero feature placeholders
  So that every backend endpoint and frontend control works as expected in DEV and CI

  Background:
    Given the client tenant is "SETMIDDLE" and the active team is "setmiddle-dev-team"
    And the environment profile is "DEV" resolving shared modules from "LATEST-HEAD"

  Scenario: 1. Backend health and primary domain action execute with zero feature placeholders
    When the SetMiddle Dev Team calls GET "/api/design/status" or invokes "/api/design/execute" on port 4024
    Then the service responds with deterministic domain output and zero unimplemented stubs

  Scenario: 2. Frontend Web Component enforces persistent labels, input placeholders, and 4-state UX
    Given the "<insightdesign>" component is rendered
    Then every input control has an explicit "<label for=...>" above it and a descriptive "placeholder" attribute inside the input box
    And submitting the form triggers "/api/design/execute" with loading skeleton, aria-live status, and inline retry support
