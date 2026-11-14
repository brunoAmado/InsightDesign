---
name: context-topology-compress-and-stacked-git
description: Clean-room 4-Axis Product Topology (InsightCode + InsightGravity v1.2.1), Sub-10KB Anchor-Preserving Salience & Matryoshka/CHIM Compression (InsightCompress v1.2.0), Stacked Merkle Predecessor & Mutation DAGs (InsightContextGit v1.2.0 PPP13), Deterministic Invariant Compilers (EU AI Act Art. 15), and Blind A/B Skill-Eval Triad.
---

# Context Topology, Sub-10KB Compression & Stacked Merkle Git Playbook

> **Governance**: Clean-room first-principles synthesis (`0% GPL-2.0` code; preserves commercial licensing & Portugal `CIRC Art. 50.º-A` Patent Box). Enforces `RULE-10` (`<2 ms` cached KPIs), `RULE-11` (`EU AI Act Art. 12/15`), `RULE-12` (`<10 KB` MCP / `<9 KB` skills), and `PPP3`/`PPP5`/`PPP13`.

## 1. 4-Axis Product Topology & `0.20x` Orphan-Route Gravity (`InsightCode` + `InsightGravity v1.2.1`)
- **Extract 4 Orthogonal Axes** (`POST /api/code/topology` / `extract_4axis_product_topology`):
  1. **Surfaces**: User-facing routes, screens, custom elements (`<insight-*>`), CLI/MCP entrypoints.
  2. **Features**: HTTP handlers (`@router.get/post`), GraphQL/RPC mutations, background jobs.
  3. **Entities**: Pydantic/SQLAlchemy/Prisma/TypeScript domain schemas and `pgvector`/`Apache AGE` tables.
  4. **Compartments**: Bounded architectural packages with explicit import fan-in/fan-out contracts.
- **Orphan-Surface Drift & Gravity Suppression**:
  - Cross-check UI `fetch('/api/...')` calls against backend route decorators (`POST /api/changed/surface-drift`).
  - Pass `alive_route_flags` and `surface_reachability_weights` into `InsightGravityEngine`: unreachable orphan routes receive a **`0.20x` gravitational mass decay** so dead handlers never pollute top-$k$ agent prompts.
  - For large manifolds (`N >= 64`), combine exact triangle-inequality `EMeans` pruning (`arXiv:2611.09501`), Barnes-Hut $O(N \log K)$ multipole ($\theta = 0.5$), and `PUPPI` (`arXiv:1407.6013`) local pileup suppression.

## 2. Triple-Layer Compression & `< 10 KB` Anchor Retention (`InsightCompress v1.2.0` — `PPP3`)
- **Layer 1 — MCP & Prompt Salience (`compact_mcp_payload_salience`, `RULE-12`)**:
  - Keep every MCP/context payload `<= 9,500` chars (`< 10 KB`) without blind `text[:max_chars]` head truncation.
  - Guarantee **100% retention** of Markdown `#`/`##` headers, `SHA-256` digests, statutory/arXiv citations (`EPC Art. 54`, `EU AI Act`, `arXiv:...`), and fenced signatures (`arXiv:2310.05736` / `2310.06839` contrast).
- **Layer 2 — Matryoshka + `Int8` / `1-Bit` Vector Quantization (`quantizer.py`)**:
  - Slice prefix dimensions (`Matryoshka`, `arXiv:2205.13147`) + symmetric `Int8` (`3.97x` compression, `>= 94.8%` Recall@10) or `1-Bit` Hamming (`32x` coarse filter + exact rescore, `arXiv:2405.12497`).
- **Layer 3 — Lossless `CHIM\x02` 22-Byte Coordinate Frames (`chim_codec.py`)**:
  - Pack 64-bit block offsets + oscillating/stride opcodes into 22-byte `CHIM\x02` frames (`23.06x` lossless recipe compression) verified by `SHA-256` before vaulting.

## 3. Clean-Room Merkle Predecessor & Mutation DAG (`InsightContextGit v1.2.0` — `PPP13`)
- Never mutate reasoning history destructively or replay bloated linear chat transcripts:
  - **`amend` / `unamend`**: Rewrite a branch tip while recording `predecessors: [old_sha]` in the `SHA-256` Merkle node and append-only `oplog`; `unamend` restores the exact prior tip in $O(1)$.
  - **`fold` / `split` / `undo`**: Coalesce exploratory turns into one clean synthesis commit (`fold`), decompose compound commits into reviewable atomic layers (`split`), or invert any `oplog` mutation (`undo`).
  - **`smartlog` Projection**: Render only active bookmarks, mutated heads, and `LCA` fork points while suppressing inactive trunk noise (`>= 60%` prompt token reduction vs. linear history; `POST /api/chat/branches/{id}/smartlog` & `POST /api/timeline/smartlog`).

## 4. `EU AI Act Art. 15` Plain-Language Invariant Compilers & Stacked Interdiff
- **Security & Polyglot SAST (`InsightGuard v1.2.0`, `POST /api/guard/compile-invariant`)**: Compile plain-language architectural rules into deterministic AST/regex checks + `SAST-21` (`CWE-833` Rust `MutexGuard` held across `.await`) + `SAST-22` (`CWE-178` Cross-OS case-insensitive filename collision).
- **Accessibility Gate (`InsightInclude v1.2.0`, `POST /api/include/compile-invariant`)**: Enforce WCAG 2.2 AA/AAA, PT `DL 82/2022`, `16px` mobile inputs, `:focus-visible`, and `aria-live="polite"` per stacked commit (`CERTIFIED_ACCESSIBLE` vs. `BLOCKED_WCAG_VIOLATION`).
- **React 19 Anti-Slop (`InsightUIUX v1.2.0`, `POST /api/uiux/audit-react19`)**: Flag sequential `await fetch` waterfalls, derived-state `useEffect` anti-patterns, and missing `AbortController` signals.

## 5. Blind A/B Skill-Eval Triad (`context-assistant` + `InsightCompare v1.2.0`)
- Evaluate every new skill/prompt upgrade with the 3-part Triad (`arXiv:2306.05685`):
  1. **Post-Hoc Analyzer**: Inspect failure ledger + diff coverage.
  2. **Blind A/B Comparator** (`POST /api/compare/blind-arena`): Mask candidate identities as `Model_Alpha` / `Model_Beta` with deterministic position-bias swap before judging.
  3. **Rubric Grader**: Require weighted rubric score `>= 0.80` + zero regression gates broken before promotion.
