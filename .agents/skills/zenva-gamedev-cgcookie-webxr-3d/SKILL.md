---
name: zenva-gamedev-cgcookie-webxr-3d
description: Compact Team Playbook distilled from 238 Zenva Academy (175), GameDev.tv (46), and CGCookie (17) courses in ChronicleRAG (<9KB). Enforces WebXR 72/90Hz frame budgets, Three.js/Godot instancing, clean Blender-to-glTF topology, and VR comfort/accessibility for VoxNomen, InsightDesign, and 3D didactic scenes.
---

# Zenva, GameDev.tv & CGCookie Spatial 3D & WebXR Playbook (`238` Courses)

> **Source Corpus**: `175` Zenva Academy (`WebXR`, `Three.js`, `Godot`, `RPG Mechanics`, `AI with Ollama`), `46` GameDev.tv (`Blender Sculpting/Character/Environment`), and `17` CGCookie (`Blender Shading, Lighting, VFX & Rigging`) courses in `ChronicleRAG`.

## 1. WebXR & Real-Time Three.js `72/90 Hz` Frame-Budget Laws (`VoxNomen™ PPP10`, `InsightDesign`)
- **Hard Frame Budget**: Keep combined JS + GPU frame time `<= 11.1 ms` (`90 Hz` Quest/PCVR) or `<= 13.8 ms` (`72 Hz`).
- **Zero Per-Frame Heap Allocation**: Never allocate `new THREE.Vector3()`, `Matrix4()`, `Quaternion()`, or closures inside `renderer.setAnimationLoop` / `useFrame`; pre-allocate module-level scratch structs to eliminate GC micro-stutters.
- **Draw-Call Batching**: Merge static environment meshes by material or render repeating runes, nodes, and particles via `THREE.InstancedMesh` / GPU instancing (`<= 100` draw calls per eye, `<= 300k` visible triangles on standalone XR).
- **Resource Disposal Guard**: Explicitly `.dispose()` geometries, materials, textures, and render targets when unmounting scenes to prevent WebGL context loss (`WEBGL_lose_context`).

## 2. Blender-to-glTF (`GLB`) Clean Asset & Shader Pipeline (`GameDev.tv` + `CGCookie`)
- **Transform & Manifold Hygiene**: Before `.glb` export, apply all object scale/rotation (`Ctrl+A -> Rotation & Scale`, verifying uniform scale `1.0, 1.0, 1.0`), recalculate normals outside (`Shift+N`), and remove zero-area faces / non-manifold edges on collision or boolean meshes.
- **ORM Channel Packing & GPU Compression**: Pack **O**cclusion (`R`), **R**oughness (`G`), and **M**etallic (`B`) into a single linear texture (`sRGB` disabled on data maps!), compress geometry with **Meshopt / Draco**, and transcode textures to **KTX2 (`BasisU`)** so VRAM footprint drops `4x–8x`.
- **Lighting & Post-Processing Discipline**: Bake static ambient occlusion and lightmaps for architectural/pedagogical rooms; avoid expensive screen-space reflections (`SSR`) or multi-pass bloom in stereo WebXR (`msaa: 4` hardware antialiasing preferred).

## 3. Spatial Pedagogy, `6-DoF` Interaction & VR Comfort (`Decreto-Lei n.º 82/2022`)
- **Ergonomic Diegetic UI Placement**: Anchor spatial HUDs, glyph palettes, and captions in world/torso space at `1.2m – 2.5m` depth (never head-locked `< 0.5m` causing vergence-accommodation fatigue), with minimum angular target size `>= 2.5°` (`~44px` equivalent).
- **Motion-Sickness Prevention**: Default to **teleport / snap-turn (`30°`/`45°`)** with an optional peripheral comfort vignette during continuous locomotion; never accelerate or tilt the XR camera horizon programmatically.
- **Mandatory Dual-Mode Accessibility (`RULE-11`)**: Every WebXR/3D didactic scene (`VoxNomen™`, `ChronicleRAG` 3D explainers, `InsightDesign`) must provide a synchronized **2D Desktop/Mobile Orbit + Keyboard (`Tab`/`Arrow` + `aria-live="polite"`) mode** so learners without headsets have 100% functional parity.

## 4. Local-SLM Driven NPC & Pedagogical State Machines (`Zenva AI + Ollama` + `RULE-14`)
- Decouple real-time `60–90 Hz` physics/animation loops from asynchronous LLM/SLM dialogue turns: run deterministic finite-state / behavior-tree controllers on the main tick while streaming 4-Tier Zero-Paid-Token SLM hints asynchronously with `< 2s` fallback templates if local inference drops below `0.70` confidence.
