# 🛡️ Security Policy & Statutory Compliance (`InsightDesign`)

> **Project**: `InsightDesign` (`:4024` `/api/design`)
> **Governance Hub**: [`context-assistant (:8080)`](https://github.com/brunoAmado/context-assistant) · [`InsightAudit™ (:4009)`](https://github.com/brunoAmado/InsightAudit) · [`InsightGuard™ (:4019)`](https://github.com/brunoAmado/InsightGuard) · [`InsightRedact™ (:4022)`](https://github.com/brunoAmado/InsightRedact)

---

## 1. Supported Versions & Environment Profiles

| Environment Profile | Git Branch | Security Posture & Secret Resolution | Supported |
| :--- | :---: | :--- | :---: |
| **`DEV`** | `dev` | Local developer sandbox, editable `LATEST-HEAD` modules (`insight_family_members.pth`), offline SAST & unit gates | ✅ Yes |
| **`DEMO_SHARED`** | `demo` | Pre-production showcase, masked PII, rate-limited public/demo endpoints | ✅ Yes |
| **`CLIENT_PROD`** | `main` | Hardened production, strict HS256/OIDC JWT RBAC, `pgsodium` envelope encryption, immutable `SHA-256` audit chain | ✅ Yes |

---

## 2. Reporting a Vulnerability & Pre-INPI IP Protection

1. **Private Disclosure Only (Pre-INPI Patent Guard)**:
   - Do **not** open public GitHub issues containing raw exploit payloads, unredacted customer data, or unpublished INPI/EPO provisional patent claims (`PPP #1`–`PPP #6`, `PT-EPO-SG-AST-2026-001`).
   - Report security findings via the local **Context-Assistant Security Scanner** (`POST http://127.0.0.1:8080/api/dashboard/security-scan`) or **InsightGuard™** (`POST http://127.0.0.1:4019/api/guard/execute`).
2. **Automated Pre-Commit & CI Gate**:
   - Every code modification is scanned against the **20-Rule Polyglot & OWASP-LLM Top 10 SAST Matrix** (`CWE-22` path traversal, `CWE-78` OS command injection, `CWE-89` SQL/Cypher injection, `CWE-798` hardcoded BYOK keys, `CVE-2021-42574` Trojan-Source bidirectional Unicode, and `OWASP-LLM01` prompt injection).

---

## 3. Mandatory 5-Pillar Portugal (`PT`) & European Union (`EU`) Statutory Compliance (`RULE-11`)

### Pillar 1 — CNPD / GDPR & Portuguese `Lei n.º 58/2019` (Art. 5(1)(c), Art. 17, Art. 25, Art. 28)
- **Zero-Leakage PII Scrubbing**: All inputs, logs, and RAG chunks pass through `scrub_pt_eu_pii_and_byok_secrets()` (`insight_core_io` / `InsightRedact™ :4022`), automatically masking:
  - Portuguese **NIF** (`9` digits, Modulo-11 verified), **NISS** (`11` digits), **SNS** (`9` digits), and **IBAN** (`PT50...`);
  - Emails, phone numbers, `<USER_HOME>` filesystem paths, and BYOK cloud API keys (`sk-...`, `AIza...`, `ghp_...`).
- **CAS Storage Separation**: Raw binary blobs (`data:image/...;base64,...` or raw byte streams) are rejected at the database boundary (`assert_no_binary_blob_in_db_row`) in favor of content-addressable pointers (`cas://sha256/<digest>`).

### Pillar 2 — EU AI Act (`Regulamento (UE) 2024/1689` — Art. 10, 12, 14, 15, 50)
- **Art. 10 (Data Governance & Non-Discrimination)**: Audited by `InsightInclude™ (:4020)` enforcing Four-Fifths Disparate Impact Ratio (`DIR >= 0.80`) and `INPI PPP #4` double-blind Romance gender neutralization.
- **Art. 12 (Immutable Record-Keeping)**: Every state-mutating action appends a `SHA-256` hash-chained receipt (`AuditReceiptChainService` / `InsightAudit™ :4009`).
- **Art. 14 (Human Oversight)**: 5-state abortable execution, `1:1` single responsible user per specialist agent (`ProjectAndAgentAuthorizationService`), and circuit-breaker isolation.
- **Art. 50 (AI Transparency)**: Explicit attribution headers and confidence abstention gates (`confidence < 0.35` abstains rather than hallucinating).

### Pillar 3 — Portugal Digital Accessibility (`Decreto-Lei n.º 82/2022` & `DL n.º 83/2018` / `EN 301 549` / `WCAG 2.2 AA/AAA`)
- Enforced by `InsightInclude™ (:4020)` and `InsightUIUX™ (:4023)` (`UX Engine 2.8`):
  - Tinted dark slate surfaces (`#090d16` -> `#0f172a` -> `#172033`, forbidding pure `#000000` OLED halation);
  - `2px solid #818cf8` `:focus-visible` keyboard rings, `.skip-to-content-link`, `aria-live="polite"` status regions, persistent `<label for="...">` above every input, and `375px` mobile touch readiness (`>= 44x44px` targets).

### Pillar 4 — NIS2 (`CNCS Portugal — DL n.º 65/2021`) & EU Cyber Resilience Act (`Reg. (UE) 2024/2847`)
- Enforces granular project ACLs (`SEE`, `EDIT`, `ELIMINATE`, `NONE`), cross-tenant firewall isolation (`SETMIDDLE` vs. `INSIGHTCV_ECOSYSTEM`), OSV AST reachability analysis, signed **CycloneDX 1.5 SBOM**, and **SARIF 2.1.0** security reporting.

### Pillar 5 — Portuguese Tax Authority (`AT — Decreto-Lei n.º 28/2019`, `CIRC`, `EBF`)
- Fiscal and settlement workflows validate Modulo-11 NIF, `ATCUD` document codes, `SAF-T (PT) v1.04_01` XML schemas, `SIFIDE II` R&D tax credits, and `CIRC Art. 50.º-A` Patent Box exemptions via `InsightFiscal™ (:4017)` and `InsightExpense™ (:4002)`.
