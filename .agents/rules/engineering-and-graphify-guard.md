---
trigger: always_on
description: Immune-to-Graphify-Install Engineering & High-Core Windows (<=61 workers) Guard.
---

## Mandatory High-Core Windows Graphify Guard & 5-Step Engineering Pipeline

> **Why this file is named `engineering-and-graphify-guard.md`**: `graphify antigravity install` unconditionally overwrites `.agents/rules/graphify.md` (`_antigravity_finalize` in `graphify/install.py`) and any exact `## graphify` H2 section in `AGENTS.md` / `GEMINI.md` (`_replace_or_append_section`). Keeping this rule in `engineering-and-graphify-guard.md` guarantees `graphify install` can never overwrite it.

1. **72-Core Windows `ProcessPoolExecutor <= 61` Guard**:
   - Always update Graphify via `.\run_graphify_update.ps1` (which caps `$env:GRAPHIFY_MAX_WORKERS = 61` and guards against `[WinError 1920]` on `docling_models`).
2. **Mandatory 5-Step Pipeline on Every Code / Architecture Change**:
   - **(1) Create/Update Tests** $\rightarrow$ **(2) Run Regression Verification (`exit code 0`)** $\rightarrow$ **(3) Update `docs/` & `wiki/`** $\rightarrow$ **(4) Run `.\run_graphify_update.ps1`** $\rightarrow$ **(5) Automatic `git commit` when green**.
3. **Additive-Only Rule Protection & `"Skip"` Default-First Semantics**:
   - Never overwrite `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, or `.cursorrules` destructively.
   - If the user clicks **"Skip"** on an `ask_question` prompt, execute Option 1 `(Recommended)` by default.
4. **Non-Blocking Asynchronous Background Execution & Chrome MV3 Manifest Invariant (`RULE-10`)**:
   - Never run long tasks (`>2s`, crawls, batch exports, AI loops) synchronously inside ephemeral UI popups (`popup.js`) or click/reload the user's active tab. Execute asynchronously in persistent Background Service Workers (`background.js`) or backend queues with live badge/status telemetry (`chrome.action.setBadgeText`, `aria-live="polite"`) and automatic progress reconnection (`attachPopupToBackgroundProgress`) so the user can freely close the popup, switch focus, or close the tab without data loss.
   - Never use suffix host wildcards (`http://192.168.*/*`, `http://10.*/*`) in Chrome MV3 `manifest.json` (`content_scripts[0].matches` / `host_permissions`); use valid MV3 patterns (`http://*/*`, `https://*/*`) and filter LAN IPs at runtime.
5. **Mandatory Portugal (`PT`) & European Union (`EU`) Statutory AI, Privacy, Accessibility, Cybersecurity & Fiscal Verification (`RULE-11`)**:
   - **CNPD / GDPR & Lei n.º 58/2019 (Art. 5(1)(c), Art. 25, Art. 28)**: Automatically scrub Portuguese NIF (`9` digits), NISS (`11` digits), SNS (`9` digits), IBAN (`PT50...`), emails, phones, `<USER_HOME>` paths, and BYOK Cloud API keys (`scrub_pii_and_secrets`) before persisting logs, books, or SFT/DPO datasets.
   - **EU AI Act — Regulamento (UE) 2024/1689 (Art. 10, 12, 14, 15, 50)**: Enforce Level 5.5 epistemic veracity scoring (Art. 10), `SHA-256` hash-chained immutable audit logs (Art. 12), human-in-the-loop abortable/background execution (Art. 14), pre-action regression gates (Art. 15), and AI transparency attribution (Art. 50).
   - **Portugal Digital Accessibility — Decreto-Lei n.º 82/2022 & DL 83/2018 (EN 301 549 / WCAG 2.2 AA/AAA)**: Non-blocking async UI workers, `aria-live="polite"` announcements, `2px solid #818cf8` `:focus-visible` rings, roving `tabindex`, and `375px` mobile touch readiness.
   - **NIS2 (CNCS Portugal — DL n.º 65/2021) & Cyber Resilience Act (Reg. (UE) 2024/2847)**: Enforce Zero-Trust BYOK key isolation, 20-rule Polyglot/OWASP-LLM SAST, OSV reachability, CycloneDX 1.5 SBOM, and SARIF 2.1.0 reporting.
   - **Portugal AT Fiscal Rules (Decreto-Lei n.º 28/2019 SAF-T/ATCUD, CIRC Art. 51.º, CIRS, CIVA, EBF Art. 43.º-C Lei das Startups)**.
6. **Token-Budget Guard, Inline MCP Payload Compaction (`< 10 KB`) & Compact `< 9 KB` Skill Distillation (`RULE-12`)**:
   - Keep all `ChronicleRAG` MCP retrieval calls in default `compact=True` / `max_chars=9500` mode (`< 10 KB`) so MCP outputs never spill to `.system_generated/steps/*/output.txt`.
   - Keep `.agents/skills/*/SKILL.md` files distilled under `< 9 KB` (`_distill_compact_skill_markdown`) while storing full 400KB+ Master Books in `books/master_books/`. Always use explicit `StartLine`/`EndLine` ranges on `read_file`.
7. **Mandatory `ChronicleRAG`-First Retrieval Gate & Continue-on-Missing Fallback (`RULE-13`)**:
   - **Always query `ChronicleRAG` first** (`search_books`, `extract_learned_playbook`, `query_graphrag`, `query_code_map`, or `read_book` in `compact=True` mode, or `.agents/skills/00-golden-cortex/SKILL.md`) before broad file scans (`Grep`/`Glob`) or external web searches (`search_web`).
   - **If `ChronicleRAG` has full coverage** (`abstention_triggered: false`), apply its verified rules and architecture directly.
   - **If information is missing or partial** (`abstention_triggered: true` or live file lines are needed), **continue seamlessly** to: `(a) Graphify AST Graph` $\rightarrow$ `(b) Targeted read_file (StartLine..EndLine)` $\rightarrow$ `(c) External search_web`.
   - Enforce the **4-Tier Zero-Paid-Token LLM Failover Chain** (`Tier 1: Local PC Gemma 4` $\rightarrow$ `Tier 2: InsightCV LiteLLM Proxy :4000` $\rightarrow$ `Tier 3: EVO Tailscale 100.91.34.106:1234` $\rightarrow$ `Tier 4: Calling IDE Agent Handover`).



