---
name: insight-patent-ip-clearance
description: Delegate Patent Claim Novelty/Inventive-Step Stress-Testing (EPC Art. 54/56, INPI PPP Art. 62, Patent Box CIRC Art. 50-A), Trademark Registration Clearance (INPI CPI Art. 209/232, EUIPO EUTMR Art. 7/8, USPTO, WIPO Nice Classes 1..45), Zero-Leak Verisign/PIR RDAP Domain Checks, Live Steam/AppStore/GitHub/OpenAlex Prior-Use Discovery, and Coined Brand Candidate Synthesis directly to `InsightPatent` v2.0 via `ChronicleRAG` (`RULE-17` + `RULE-14` Second-Eyes Audit).
---

# InsightPatent™ v2.0 Autonomous IP, Trademark & RDAP Delegation Skill (`RULE-17`)

> **MANDATORY SERVICE-FIRST DELEGATION (`RULE-17` & `ERR-AGENT-01`)**:
> Whenever the user asks to verify whether a **product/game/company name or trademark is registered**, check **domain availability (`.com`, `.gg`, `.io`, `.pt`, `.ai`)**, generate **coined candidate titles**, or evaluate **patent novelty / prior art / INPI PPP claims**, **NEVER** run ad-hoc manual web/RDAP loops inline first. Always delegate execution to **`InsightPatent™` v2.0** first, and then act as the user's **Second Pair of Eyes (`RULE-14`)** auditing `InsightPatent`'s SHA-256-receipted dossier.

## 1. Primary Delegation Channels (Choose Fastest Available)

1. **`chronicle-rag` MCP Tool (Preferred in Any Workspace)**:
   - Call `delegate_patent_and_trademark_verification(candidate_mark, product_description, core_mechanics_csv, claim_text, invention_title, priority_date, allow_live_discovery=True, generate_candidates_limit=5, use_local_slm_counsel=True)` (`< 9.5 KB` `RULE-12` compact JSON).
2. **Warm REST Endpoint (`ChronicleRAG` `:8765` or Standalone `InsightPatent` `:8096` / `:8771`)**:
   - `POST http://127.0.0.1:8765/api/patent/delegate/verify-ip` (or `:8096/api/patent/delegate/verify-ip`) using IPv4 `curl.exe -4` (`ERR-AGENT-03`).
3. **Interactive UX Engine 2.8 Clearance Lab UI**:
   - `http://localhost:8765/projects/insight-patent/tm-lab` (co-hosted) or `/api/patent/trademark/lab`.
4. **Background Drip-Queue (`SetMiddleSpecialtyDispatcher` when `ChronicleRAG` is Occupied)**:
   - Enqueue `task_type="patent_or_trademark_clearance"` (`specialty_service="InsightPatent"`).

## 2. What `InsightPatent™` v2.0 Executes Autonomously

1. **Absolute Grounds (`INPI CPI Art. 209.º` & `EUIPO EUTMR Art. 7`)**: Scores Generic $\rightarrow$ Descriptive $\rightarrow$ Crowded Portmanteau $\rightarrow$ Suggestive $\rightarrow$ Coined/Fanciful.
2. **Bilingual Nice Classes (`1..45`) & EUIPO SME Fund Grant Math**: Outputs copy-ready PT (`INPI`) & EN (`EUIPO/WIPO`) specs + 75% Voucher 2 net fees (`~€38.00` INPI 1-class; `~€212.50` EUIPO 27-state).
3. **Phonetic Skeleton (`Metaphone` + Portmanteau Elision) & `ChronicleRAG` `10,346+` Book Corpus**: Catches phonetic twins (`Mathgic == Math Magic == MTJK`).
4. **Live Multi-Source Registry Probes (`IPv4 curl.exe -4`)**: Queries **Steam Store**, **Apple App Store**, **GitHub Repos**, and **OpenAlex Works** in parallel, classifying hits into `NAME_PUN_ONLY_ZERO_MECHANIC_COLLISION` vs. `BRAND_AND_FEATURE_OVERLAP`.
5. **Zero-Front-Running Authoritative RDAP**: Queries official Verisign (`.com/.net`), PIR (`.org`), Google Registry (`.app/.dev`), and Passive DNS (`.gg/.io/.ai/.pt`) — **never** retail domain registrars.
6. **Sanitized Patent Stress-Tester (`EPC Art. 54/56` + `InsightTimeline` Cutoff)**: Strips secret identifiers/couplings via `sanitize_claim_to_non_enabling_taxonomy_keywords` before OpenAlex queries.
7. **4-Tier Local SLM Counsel + `RULE-14` Second-Eyes Receipt**: Uses `Local Gemma 4 (:1234/:8011)` $\rightarrow$ `LiteLLM (:4000)` $\rightarrow$ `EVO (100.91.34.106:1234)` $\rightarrow$ `Antigravity Second-Eyes Takeover Banner`.
