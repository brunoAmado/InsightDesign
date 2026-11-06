# 🛠️ How-To Guides & Practical Recipes (`InsightDesign`)

This guide provides step-by-step recipes for integrating, testing, and operating **`InsightDesign`** (`:4024` `/api/design`) across the SetMiddle & Família Insights™ ecosystem.

---

## How-To 1: Execute `InsightDesign` via REST API (`curl` / PowerShell)

```powershell
# 1. Check service status and foundation tier:
Invoke-RestMethod -Uri "http://127.0.0.1:4024/api/design/status" -Method Get

# 2. Execute the primary deterministic domain action:
$body = @{
    tenant_id = "SETMIDDLE"
} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:4024/api/design/execute" -Method Post -Body $body -ContentType "application/json"
```

---

## How-To 2: Import `InsightDesign` Directly in Python (`LATEST-HEAD` Zero-Copy Module)

Because all shared repositories are registered in `chronicle-rag/.venv/Lib/site-packages/insight_family_members.pth`, any sibling Python project can import `InsightDesign` without HTTP overhead:

```python
from insight_design.engine import InsightDesignEngine

engine = InsightDesignEngine()
status = engine.get_status()
result = engine.execute({"tenant_id": "SETMIDDLE"})
print(status["product"], "->", result["ok"])
```

---

## How-To 3: Embed the Standards-Based Web Component (`<insight-design>`)

Every UI in `InsightDesign` follows **ChronicleRAG UX Engine 2.8** (tinted dark slate `#090d16` -> `#0f172a` -> `#172033`, `tabular-nums`, concentric border radii, persistent `<label for="...">` above inputs, `"Validate on Blur, Forgive on Keystroke"`, and 4-state completeness):

```html
<script src="http://127.0.0.1:4024/api/design/widget.js" defer></script>
<insight-design api-base="http://127.0.0.1:4024/api/design"></insight-design>
```

---

## How-To 4: Trigger `InsightDesign` via `InsightChat™ (:4012)` or `context-assistant (:8080)`

You can issue natural-language inter-project orders to `InsightDesign` from any IDE (VS Code Cline/Roo Code/Continue, JetBrains) or the `context-assistant` web console:

```powershell
$chatOrder = @{
    query = "Check status and run regression verification for InsightDesign"
    sessionId = "dev-session-01"
    tenantGroup = "SETMIDDLE"
    environmentProfile = "DEV"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8080/api/dashboard/insight-chat/turn" -Method Post -Body $chatOrder -ContentType "application/json"
```

---

## How-To 5: Scrub PT/EU PII & Verify CAS Storage Separation (`RULE-11`)

Before persisting any user text or document payload in `InsightDesign`, run the built-in CNPD/GDPR scrubber and CAS guard:

```powershell
$scrubReq = @{
    text = "Cliente NIF 123456789, IBAN PT50000201231234567890154, key sk-proj1234567890abcdef"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:4024/api/design/scrub" -Method Post -Body $scrubReq -ContentType "application/json"
```

---

## How-To 6: Sync Git Branches & Managed Mirror in `context-assistant`

When you commit changes in `C:\Users\bruno\PycharmProjects\InsightDesign`, keep GitHub (`main`, `dev`, `demo`) and `context-assistant/projects/InsightDesign` synchronized:

```powershell
cd "C:\Users\bruno\PycharmProjects\InsightDesign"
git add -A
git commit -m "feat(insightdesign): describe your change with passing tests"
git push origin main
git push origin main:dev
git push origin main:demo
```
