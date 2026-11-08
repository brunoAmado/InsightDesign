---
name: ux-engine
description: Compact Team Master Playbook for UI UX Engineering distilled from ChronicleRAG (Book_Lit_Master_UI_UX_Engineering.md). Enforces core architectural, UI/UX, and implementation rules with <9KB context footprint.
---

# ⚡ Compact Specialist Skill: UI UX Engineering (`lit_Master_UI_UX_Engineering`)
> **Token-Budget Guard (`RULE-12`)**: This skill is pre-distilled (`< 9 KB`) from `books/master_books/Book_Lit_Master_UI_UX_Engineering.md` (`413 KB`) to prevent context bloat.
> **Hierarchical Progressive Disclosure & Backtrace**:
> - **Full Chapter TOC**: `chronicle-rag:read_book(identifier='lit_Master_UI_UX_Engineering', section='toc')`
> - **Surgical Single Chapter + Origin Backtrace**: `chronicle-rag:read_book(identifier='lit_Master_UI_UX_Engineering', section='chapter:<N>')` or `section='chapter:<keyword>'`
> - **Recursive 'New Eyes' Critique**: `chronicle-rag:read_book(identifier='lit_Master_UI_UX_Engineering', section='new_eyes')`

## 🌟 Executive Synopsis (Level 1)
Team-shared Master Thematic Book consolidating **111 chapters** and **89 source books** on `UI_UX_Engineering`.

## 📑 Key Chapters Index (Showing 25 of 111 Chapters)
- **Chapter 1**: Anti-AI-Slop Dashboard Architecture
- **Chapter 2**: Typography as a 7-Decision Mathematical System
- **Chapter 3**: Concentric Border Radii, Cards vs. Panels & Dark-Mode Elevation
- **Chapter 4**: Form UX, Validation Timing & Control Selection
- **Chapter 5**: Desktop Data Tables, Bulk Selection & Mobile Row Stacking
- **Chapter 6**: Cursor Pagination, URL State & Scroll Restoration
- **Chapter 7**: Modals vs. Sheets vs. Drawers, Command Palette (`⌘K`) & Context Menus
- **Chapter 8**: Perceived Instant Speed (Raycast Pattern), Skeleton CLS & Drag-and-Drop Physics
- **Chapter 9**: Danger Actions, 5s Soft-Delete Undo Toasts & Specific "Done" Screens
- **Chapter 10**: Defensive CSS for Real Data, Resizable Panels & Mobile Hover Guards
- **Chapter 11**: Zero-JS Modern CSS (`:has()`, `@container`, View Transitions & Scroll-Snap)
- **Chapter 12**: Micro-Component Polish: Clipboard, Avatars, Voice/Swipe Physics & Pricing UX
- **Chapter 13**: UX Engine 2.0 Architecture: `design-system`, `visual-character` 4-Axis Law & `/restyle`
- **Chapter 14**: Honest Dashboard Charts, Data Visualization & Pro Number Formatting
- **Chapter 15**: Specialized High-Conversion Inputs: AI Prompt Box, Stripe Checkout, Card, OTP, Password, Date Picker, Slider & Color Picker
- **Chapter 16**: Navigation Systems, 4-Level File Trees, Non-Jumping Tabs, Search, Filter Chips & Multi-Step Wizards
- **Chapter 17**: Reactive State Machines: Auto-Save, Optimistic UI, Button Click Lifecycle, Double-Tap Guard & Disabled Button Explanations
- **Chapter 18**: SaaS Workspace Systems: Linear Aesthetic, Chat Threads, 40-Event Calendar Week View, Settings Page, Notifications, Multiplayer & Z-Index Scale
- **Chapter 19**: Cognitive Psychology Laws, Organic Motion Timing, Golden Ratio & Anti-AI Landing Page Tells
- **Chapter 20**: UX Engine 2.4 (`375px` Mobile Readiness), Full Keyboard Navigation Architecture & WCAG 2.2 AA Accessibility
- **Chapter 21**: UX Engine 2.4: Effortless Search (5 Decisions), First-Run Onboarding (5 Pieces) & Permission Prompts (5 Rules)
- **Chapter 22**: UX Engine 2.5: Notion Zero-Friction Blank Canvas, Live Multi-Page Reactive Dashboards, Visual Diagnostic Matrix & Contrast Eye-Tracking
- **Chapter 23**: brunoAmado/chronicle-rag — README.md > **Source Link**: https://github.com/brunoAmado (🛡️ 9.5/10 | PT: 9.8/10)
- **Chapter 24**: Home (🛡️ 9.7/10 | PT: 9.9/10)
- **Chapter 25**: README > **Source Link**: J:/bobcat/bobcat300-recycle/README.md (🛡️ 9.1/10 | PT: 9.4/10)
- *(+86 additional chapters indexed in `Book_Lit_Master_UI_UX_Engineering.md`)*

## 📐 Distilled Engineering Rules & Actionable Patterns
### Chapter 1 [Anti-AI-Slop Dashboard Architecture]
1. **Eliminate Decorative Gradients**: AI-generated UIs paint purple-to-blue gradients on headers, buttons, and chart fills where they have nothing to say. Use **one flat semantic accent** (`indigo-600`) so color carries meaning.
2. **Drop Pastel Icon Tiles on Metric Cards**: Putting blue, green, purple, and orange icon squares on 4 KPI cards is decoration, not information. Drop the pastel tiles — **the metric number is the hero**.
3. **Break Equal-Card Monotony**: Four identical cards with the same size, weight, and green badge is "a spreadsheet with padding." Render **1 primary metric large** and **3 secondary metrics compact** so the user's eye lands once.
4. **Never Ship Database-Shaped Schemas**: Do not dump all 12 database columns onto a screen with `Delete` sitting right next to `Edit` on every row. Rank columns by user intent, limit to 1 primary CTA per view, and spec all **4 mandatory states** (*Loading sk

### Chapter 2 [Typography as a 7-Decision Mathematical System]
1. **5 Sizes Max (1.25 Modular Scale)**: Never hand-pick 11 arbitrary pixel sizes; collapse to 5 steps on a `1.25` ratio.
2. **3 Text Colors Rank Inside a Line**: Use `Primary` (`slate-50`), `Secondary` (`slate-300`), and `Muted` (`slate-400`). Color ranks *within* a line; font size ranks *between* blocks.
3. **2 Font Weights Do All the Work**: `400` (Regular) for reading prose and `600` (Semi-bold) for scanning headings/labels. When everything is bold, nothing is bold.
4. **Line-Height Moves Opposite to Size**: Use `1.1–1.15` on display headings and `1.5–1.6` on body copy (using `1.5` everywhere is an AI-slop tell).
5. **Scale-Dependent Letter-Spacing**: Tighten tracking `-2%` (`-0.02em`) above `24px`; open tracking `+5%` (`+0.05em`) on small uppercase section labels.

### Chapter 3 [Concentric Border Radii, Cards vs. Panels & Dark-Mode Elevation]
1. **Concentric Border Radius Formula**: Using the same border-radius on outer and inner nested containers makes the inner corner bulge. Enforce:
2. **Size-Matched Radius Scale**: `4px` (Small: inputs/badges), `8px` (Medium: buttons/inner tiles), `16px` (Large: modals/cards), and `9999px` (Pill: strictly single-line chips/toggles). Sheets docked to the screen edge get `0px` radius on the touching edge.
3. **Cards vs. Panels**: A **Card** represents one entity with one click action across its entire surface. If a container holds multiple interactive buttons or form sections, it is a **Panel**, not a card. **Never nest cards inside cards** — use flat surfaces 
4. **Pure Black (`#000000`) Isn't Dark Mode — It's a Terminal (`fb_4527950214187522`)**: Pure `#000000` causes OLED smearing, harsh contrast halation on white text, and makes elevation impossible because you cannot cast a shadow on `#000000`. Use **tinted dark

### Chapter 4 [Form UX, Validation Timing & Control Selection]
1. **"Validate on Blur, Forgive on Keystroke" (`onBlur` $\rightarrow$ `onChange`)**:
* Never fire red errors on the first keystroke while the user is mid-word, and never wait until Submit across 10 fields.
* **Rule**: Validate first **on `blur`** (when the user leaves the field). Once a field is marked invalid, switch *that field* to **live keystroke validation** so the error clears the exact instant it is fixed.
2. **5 Signup Form Mistakes to Eliminate (`fb_1440498064725043`) & Readable Input States (`fb_26902587206039051`)**:
3. **Checkbox vs. Switch vs. Radio vs. Segmented Control (`fb_1458518826177868`, `fb_27114469058187838`)**:

### Chapter 5 [Desktop Data Tables, Bulk Selection & Mobile Row Stacking]
1. **Desktop Table Alignment & Chrome**: Left-align text, **right-align numeric/currency columns** with `tabular-nums`, replace noisy zebra stripes with `1px` hairlines + row hover highlight, never leave cells blank (render `—` or `0`), and pin both the header
2. **3 Row-Height Density Modes**: Support `Compact (40px)`, `Default (48px)`, and `Comfortable (56px)`.
3. **Mobile Table Restructuring (Stack, Don't Shrink)**: On mobile viewports, drop raw IDs first and restructure into a **2-line thumb-sized row**: *Identity/Name* top-left, *Amount/Metric* top-right in `tabular-nums` (so numbers still form a vertical scannabl
4. **Bulk Action State Machine**: Header checkbox must support `indeterminate` (clicking `indeterminate` selects all). Explicitly offer *"Select all 247 matching rows"* beyond the current page, support `Shift+Click` range selection, and persist selection acros
