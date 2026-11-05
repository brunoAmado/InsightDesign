/**
 * `InsightDesign™` — Standards-Based Interactive TypeScript Web Component (`<insight-design>`)
 * Enforces ChronicleRAG UX Engine 2.8 & 3D/CAD/Blender/Interactive Draw/Game Studio controls.
 */

export class InsightDesignElement extends HTMLElement {
  private apiBase: string = "/api/design";

  static get observedAttributes(): string[] {
    return ["api-base"];
  }

  connectedCallback(): void {
    this.apiBase = this.getAttribute("api-base") || "/api/design";
    this.renderShell();
  }

  private renderShell(): void {
    this.innerHTML = `
      <section class="insight-design-panel" role="region" aria-label="InsightDesign™ — 3D Three.js, Blender, Parametric CAD, Interactive Draw & Games"
        style="background:#0f172a;color:#f8fafc;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:20px;font-family:Inter,system-ui,-apple-system,sans-serif;font-variant-numeric:tabular-nums;">
        <header style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #1e293b;padding-bottom:12px;">
          <div>
            <div style="font-size:11px;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;color:#94a3b8;">
              SETMIDDLE CLIENT TENANT · PORT 4024 · 3D · BLENDER · CAD · DRAW · GAMES
            </div>
            <h3 style="margin:4px 0 0;font-size:18px;font-weight:600;letter-spacing:-0.02em;line-height:1.15;color:#f8fafc;">
              InsightDesign™ — Three.js, Blender bpy, Parametric CAD (.STL), Interactive Draw & Games
            </h3>
          </div>
          <span style="padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600;background:rgba(16,185,129,0.16);color:#6ee7b7;border:1px solid rgba(16,185,129,0.35);">
            READY · :4024
          </span>
        </header>
        <form id="insight-design-form" novalidate style="display:grid;gap:12px;">
          <div style="display:grid;gap:4px;">
            <label for="idesign-prompt-input" style="font-size:13px;font-weight:600;color:#cbd5e1;">
              3D / CAD / Blender / Game Scene Prompt <span style="color:#f43f5e;">*</span>
            </label>
            <input id="idesign-prompt-input" name="prompt" type="text" required
              placeholder="e.g. Parametric IP65 enclosure 120x80x45mm with Three.js orbit preview and Blender bevel script"
              style="background:#090d16;color:#f8fafc;border:1px solid #334155;border-radius:8px;padding:9px 12px;font-size:16px;" />
          </div>
          <button id="insight-design-submit-btn" type="submit"
            style="background:#4f46e5;color:#ffffff;border:none;border-radius:8px;padding:9px 16px;font-size:13px;font-weight:600;cursor:pointer;justify-self:start;">
            Generate 3D / CAD / Game Artifact
          </button>
        </form>
        <div id="insight-design-status" aria-live="polite" style="margin-top:12px;font-size:12px;color:#94a3b8;">
          Active on <code>${this.apiBase}</code>
        </div>
      </section>
    `;
  }
}

if (typeof window !== "undefined" && !customElements.get("insight-design")) {
  customElements.define("insight-design", InsightDesignElement);
}
