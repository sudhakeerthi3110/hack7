<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>SafeRadius – SOS & Geo-Fencing</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    :root {
      --bg: #020617;
      --card: #020617;
      --accent-sos: #ef4444;
      --accent-safe: #22c55e;
      --accent-warn: #f97316;
      --text: #e5e7eb;
      --muted: #9ca3af;
      --border: #1f2937;
      --radius-lg: 18px;
      --radius-sm: 10px;
      --shadow: 0 20px 45px rgba(15, 23, 42, 0.95);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
        sans-serif;
    }

    body {
      background: radial-gradient(circle at top, #020617, #000000 60%);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: stretch;
      padding: 16px;
    }

    .app {
      width: 100%;
      max-width: 430px;
      background: linear-gradient(150deg, #020617 0%, #020617 40%, #020617 100%);
      border-radius: 28px;
      border: 1px solid rgba(148, 163, 184, 0.2);
      box-shadow: var(--shadow);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* HEADER */
    .app-header {
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border);
      background: radial-gradient(circle at top left, #020617, #020617);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-logo {
      width: 34px;
      height: 34px;
      border-radius: 999px;
      background: conic-gradient(from 210deg, #f97316, #ef4444, #ec4899, #6366f1);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 18px;
      box-shadow: 0 0 18px rgba(239, 68, 68, 0.7);
    }

    .brand-text {
      display: flex;
      flex-direction: column;
    }

    .brand-title {
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 0.05em;
    }

    .brand-subtitle {
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }

    .status-pill {
      font-size: 11px;
      padding: 4px 11px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.5);
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.15em;
    }

    .status-pill.safe {
      border-color: rgba(34, 197, 94, 0.85);
      color: #bbf7d0;
      background: rgba(22, 163, 74, 0.12);
    }

    .status-pill.sos {
      border-color: rgba(248, 113, 113, 0.95);
      color: #fecaca;
      background: rgba(220, 38, 38, 0.14);
    }

    /* TABS */
    .tabs {
      display: flex;
      padding: 6px;
      gap: 6px;
      border-bottom: 1px solid var(--border);
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(14px);
    }

    .tab {
      flex: 1;
      text-align: center;
      font-size: 12px;
      padding: 8px 0;
      border-radius: 999px;
      color: var(--muted);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.16s ease-out;
    }

    .tab span {
      display: block;
      font-size: 10px;
      opacity: 0.7;
      text-transform: uppercase;
      letter-spacing: 0.16em;
    }

    .tab.active {
      color: #f9fafb;
      border-color: rgba(148, 163, 184, 0.7);
      background: radial-gradient(circle at top, #111827, #020617);
      box-shadow: 0 0 20px rgba(79, 70, 229, 0.5);
    }

    /* BODY */
    .app-body {
      flex: 1;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      overflow-y: auto;
    }

    .card {
      background: radial-gradient(circle at top left, #020617, #020617 55%, #000000);
      border-radius: var(--radius-lg);
      border: 1px solid rgba(51, 65, 85, 0.9);
      padding: 14px;
      box-shadow: 0 14px 34px rgba(15, 23, 42, 0.86);
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .card-title {
      font-size: 14px;
      font-weight: 600;
    }

    .card-subtitle {
      font-size: 11px;
      color: var(--muted);
    }

    .pill {
      font-size: 11px;
      padding: 3px 9px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.55);
      color: var(--muted);
    }

    .pill.warn {
      border-color: rgba(249, 115, 22, 0.95);
      color: #fed7aa;
      background: rgba(234, 88, 12, 0.16);
    }

    /* SAFETY / SOS */
    .section {
      display: none;
      flex-direction: column;
      gap: 10px;
    }

    .section.active {
      display: flex;
    }

    .sos-area {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      margin-top: 6px;
    }

    .sos-circle {
      width: 180px;
      height: 180px;
      border-radius: 999px;
      background: radial-gradient(circle at 30% 20%, #f97316, #ef4444 45%, #7f1d1d 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow:
        0 0 0 1px rgba(248, 250, 252, 0.16),
        0 0 46px rgba(248, 113, 113, 0.84),
        0 0 120px rgba(248, 250, 252, 0.16);
      cursor: pointer;
      position: relative;
      transition: transform 0.12s ease-out, box-shadow 0.12s ease-out;
      touch-action: manipulation;
    }

    .sos-circle:active {
      transform: scale(0.96);
      box-shadow:
        0 0 0 1px rgba(248, 250, 252, 0.16),
        0 0 32px rgba(248, 113, 113, 0.8),
        0 0 90px rgba(248, 250, 252, 0.16);
    }

    .sos-ring {
      position: absolute;
      width: 220px;
      height: 220px;
      border-radius: 999px;
      border: 1px dashed rgba(252, 165, 165, 0.7);
      animation: pulse 2.3s infinite;
    }

    @keyframes pulse {
      0% {
        transform: scale(0.9);
        opacity: 0.95;
      }
      70% {
        transform: scale(1.06);
        opacity: 0;
      }
      100% {
        transform: scale(1.06);
        opacity: 0;
      }
    }

    .sos-icon {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }

    .sos-symbol {
      width: 40px;
      height: 40px;
      border-radius: 999px;
      border: 2px solid #fee2e2;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 4px;
    }

    .sos-symbol svg {
      width: 24px;
      height: 24px;
      fill: #fee2e2;
    }

    .sos-label {
      font-size: 34px;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #fef2f2;
    }

    .sos-hint {
      font-size: 11px;
      color: #fee2e2;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      margin-top: 2px;
      opacity: 0.96;
    }

    .sos-meta {
      text-align: center;
      font-size: 11px;
      color: var(--muted);
      max-width: 260px;
    }

    .btn-row {
      display: flex;
      gap: 8px;
      margin-top: 10px;
      width: 100%;
    }

    .btn {
      flex: 1;
      padding: 10px 0;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.7);
      background: rgba(15, 23, 42, 0.95);
      color: var(--text);
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.16s ease-out;
    }

    .btn.primary {
      background: linear-gradient(135deg, #22c55e, #16a34a);
      border-color: rgba(34, 197, 94, 0.85);
      color: #022c22;
      box-shadow: 0 0 24px rgba(22, 163, 74, 0.72);
    }

    .btn.destructive {
      background: rgba(127, 29, 29, 0.5);
      border-color: rgba(248, 113, 113, 0.94);
      color: #fecaca;
    }

    .btn:active {
      transform: translateY(1px);
      box-shadow: none;
    }

    .btn[disabled] {
      opacity: 0.5;
      cursor: default;
      box-shadow: none;
    }

    .info-row {
      margin-top: 8px;
      padding: 8px;
      border-radius: var(--radius-sm);
      background: radial-gradient(circle at top left, #020617, #000000 70%);
      border: 1px solid rgba(30, 64, 175, 0.78);
      font-size: 11px;
    }

    .info-row strong {
      font-size: 11px;
      color: #bfdbfe;
      text-transform: uppercase;
      letter-spacing: 0.16em;
    }

    .info-value {
      margin-top: 3px;
      color: #e5e7eb;
    }

    .info-muted {
      color: var(--muted);
      font-size: 11px;
    }

    .badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }

    .badge {
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 999px;
      border: 1px solid rgba(75, 85, 99, 0.9);
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.14em;
    }

    .badge.critical {
      border-color: rgba(248, 113, 113, 0.94);
      color: #fecaca;
    }

    .badge.geo {
      border-color: rgba(96, 165, 250, 0.94);
      color: #bfdbfe;
    }

    /* CONFIRM BAR */
    .confirm-bar {
      position: fixed;
      left: 50%;
      bottom: 14px;
      transform: translateX(-50%);
      width: 100%;
      max-width: 430px;
      padding: 10px 12px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.98);
      border: 1px solid rgba(248, 113, 113, 0.9);
      color: #fecaca;
      font-size: 11px;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 12px 30px rgba(15, 23, 42, 0.96);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease-out, transform 0.2s ease-out;
      z-index: 60;
    }

    .confirm-bar.visible {
      opacity: 1;
      transform: translate(-50%, -4px);
      pointer-events: auto;
    }

    .confirm-text {
      flex: 1;
    }

    .confirm-count {
      font-weight: 700;
      margin-left: 4px;
    }

    .confirm-cancel-btn {
      border-radius: 999px;
      border: 1px solid rgba(248, 250, 252, 0.9);
      padding: 5px 11px;
      font-size: 11px;
      background: rgba(15, 23, 42, 1);
      color: #f9fafb;
      cursor: pointer;
    }

    /* FORMS & LISTS */
    .field-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 8px;
    }

    .field-label {
      font-size: 11px;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.16em;
    }

    .field-input,
    .field-select {
      padding: 8px 10px;
      border-radius: 999px;
      border: 1px solid rgba(55, 65, 81, 0.9);
      background: rgba(15, 23, 42, 0.98);
      color: var(--text);
      font-size: 12px;
      outline: none;
      width: 100%;
    }

    .field-input::placeholder {
      color: rgba(148, 163, 184, 0.75);
    }

    .pill-list {
      margin-top: 8px;
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .item-pill {
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.98);
      border: 1px solid rgba(55, 65, 81, 0.96);
      font-size: 11px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .item-pill span {
      color: #e5e7eb;
    }

    .item-pill small {
      color: var(--muted);
      font-size: 10px;
    }

    .item-icon {
      width: 18px;
      height: 18px;
      border-radius: 999px;
      background: rgba(30, 64, 175, 0.18);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
    }

    .item-remove {
      border: none;
      background: transparent;
      color: #fca5a5;
      font-size: 16px;
      line-height: 1;
      cursor: pointer;
    }

    /* TOAST */
    .toast {
      position: fixed;
      left: 50%;
      bottom: 16px;
      transform: translateX(-50%);
      padding: 8px 14px;
      border-radius: 999px;
      font-size: 11px;
      background: rgba(15, 23, 42, 0.98);
      color: #e5e7eb;
      border: 1px solid rgba(148, 163, 184, 0.9);
      box-shadow: 0 10px 26px rgba(15, 23, 42, 0.96);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease-out, transform 0.2s ease-out;
      max-width: 320px;
      text-align: center;
      z-index: 50;
    }

    .toast.visible {
      opacity: 1;
      transform: translate(-50%, -4px);
      pointer-events: auto;
    }

    .toast.warn {
      border-color: rgba(249, 115, 22, 0.96);
      color: #fed7aa;
    }

    .toast.error {
      border-color: rgba(248, 113, 113, 0.96);
      color: #fecaca;
    }

    .toast-success {
      border-color: rgba(52, 211, 153, 0.95);
      color: #a7f3d0;
    }

    @media (max-width: 480px) {
      body {
        padding: 10px;
      }
      .app {
        border-radius: 22px;
      }
      .sos-circle {
        width: 160px;
        height: 160px;
      }
      .sos-label {
        font-size: 30px;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <header class="app-header">
      <div class="brand">
        <div class="brand-logo">S</div>
        <div class="brand-text">
          <div class="brand-title">SafeRadius</div>
          <div class="brand-subtitle">SOS • GEO-FENCE</div>
        </div>
      </div>
      <div id="globalStatusPill" class="status-pill safe">Status: Safe</div>
    </header>

    <nav class="tabs">
      <button class="tab active" data-target="safety">
        Safety
        <span>Home</span>
      </button>
      <button class="tab" data-target="geofences">
        Geo-Fences
        <span>Zones</span>
      </button>
      <button class="tab" data-target="profile">
        Profile
        <span>Contacts</span>
      </button>
    </nav>

    <main class="app-body">
      <!-- SAFETY SECTION -->
      <section id="safety" class="section active">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">Emergency SOS</div>
              <div class="card-subtitle">
                Press & hold if you feel unsafe or need help.
              </div>
            </div>
            <div class="pill warn">High priority</div>
          </div>

          <div class="sos-area">
            <div id="sosCircle" class="sos-circle" aria-label="Press and hold to trigger SOS">
              <div class="sos-ring"></div>
              <div class="sos-icon">
                <div class="sos-symbol">
                  <!-- Alert icon (bell/triangle) -->
                  <svg viewBox="0 0 24 24" aria-hidden="true">
                    <path d="M12 2a1 1 0 0 1 .93.64l8 18A1 1 0 0 1 20 22H4a1 1 0 0 1-.93-1.36l8-18A1 1 0 0 1 12 2zm0 6a1 1 0 0 0-.99 1.14l.75 5A1 1 0 0 0 12.75 15h.5a1 1 0 0 0 .99-1.14l-.75-5A1 1 0 0 0 12.75 8h-.5zM12 17a1.25 1.25 0 1 0 0 2.5A1.25 1.25 0 0 0 12 17z" />
                  </svg>
                </div>
                <div class="sos-label">SOS</div>
                <div id="sosHint" class="sos-hint">Press & Hold</div>
              </div>
            </div>
            <p id="sosMeta" class="sos-meta">
              Your location is used only when SOS is active or you choose to share it.
            </p>
          </div>

          <div class="btn-row">
            <button id="btnSafe" class="btn primary">
              I’m Safe
            </button>
            <button id="btnCancelSos" class="btn destructive" disabled>
              Cancel SOS
            </button>
          </div>

          <div class="badge-row">
            <div class="badge critical">Women & Elderly</div>
            <div class="badge geo">Time-aware zones</div>
            <div class="badge">Privacy-first</div>
          </div>

          <div class="info-row">
            <strong>Live Status</strong>
            <div id="statusText" class="info-value">
              Safe. No active SOS.
            </div>
            <div id="statusMeta" class="info-muted">
              Last updated just now.
            </div>
          </div>

          <div class="info-row" style="margin-top: 6px;">
            <strong>Location snapshot</strong>
            <div id="locationText" class="info-value">
              Location not requested yet.
            </div>
            <div id="locationMeta" class="info-muted">
              Your browser will ask for permission when needed.
            </div>
          </div>
        </div>
      </section>

      <!-- GEOFENCES SECTION -->
      <section id="geofences" class="section">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">Safe Zones</div>
              <div class="card-subtitle">
                Mark home/office and choose when alerts should happen.
              </div>
            </div>
            <div class="pill">Local demo</div>
          </div>

          <form id="geofenceForm" autocomplete="off">
            <div class="field-group">
              <label class="field-label" for="gfName">Zone name</label>
              <input
                id="gfName"
                class="field-input"
                type="text"
                placeholder="e.g., Home, Office"
                required
              />
            </div>

            <div class="field-group">
              <label class="field-label" for="gfRadius">Radius (meters)</label>
              <input
                id="gfRadius"
                class="field-input"
                type="number"
                min="50"
                max="3000"
                step="50"
                value="300"
                required
              />
            </div>

            <div class="field-group">
              <label class="field-label" for="gfTime">Alert time rule</label>
              <select id="gfTime" class="field-select">
                <option value="any">Any time</option>
                <option value="night">Night only (10pm–5am)</option>
                <option value="day">Day only (5am–10pm)</option>
              </select>
            </div>

            <div class="field-group">
              <label class="field-label" for="gfNote">Location hint</label>
              <input
                id="gfNote"
                class="field-input"
                type="text"
                placeholder="Short note (e.g., near gate / 3rd floor)"
              />
            </div>

            <div class="btn-row" style="margin-top: 12px;">
              <button type="submit" class="btn primary">
                Save Zone
              </button>
            </div>
          </form>

          <div class="pill-list" id="geofenceList">
            <!-- geofence chips -->
          </div>
        </div>
      </section>

      <!-- PROFILE SECTION -->
      <section id="profile" class="section">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">Profile & Contacts</div>
              <div class="card-subtitle">
                Decide who gets alerts and how you’re described.
              </div>
            </div>
            <div class="pill">Local only</div>
          </div>

          <div class="field-group">
            <label class="field-label" for="profileName">Your name</label>
            <input
              id="profileName"
              class="field-input"
              type="text"
              placeholder="e.g., Aditi Sharma"
            />
          </div>

          <div class="field-group">
            <label class="field-label" for="profileRole">Profile type</label>
            <select id="profileRole" class="field-select">
              <option value="woman">Woman</option>
              <option value="elderly">Elderly</option>
              <option value="guardian">Guardian / Family</option>
            </select>
          </div>

          <hr style="border-color: rgba(30,64,175,0.5); margin: 10px 0;" />

          <form id="contactForm" autocomplete="off">
            <div class="field-group">
              <label class="field-label" for="contactName">Contact name</label>
              <input
                id="contactName"
                class="field-input"
                type="text"
                placeholder="e.g., Mom"
                required
              />
            </div>

            <div class="field-group">
              <label class="field-label" for="contactRelation">Relation</label>
              <input
                id="contactRelation"
                class="field-input"
                type="text"
                placeholder="e.g., Mother, Friend"
              />
            </div>

            <div class="field-group">
              <label class="field-label" for="contactPhone">Phone / WhatsApp</label>
              <input
                id="contactPhone"
                class="field-input"
                type="tel"
                placeholder="e.g., +91-98765-43210"
                required
              />
            </div>

            <div class="btn-row" style="margin-top: 10px;">
              <button type="submit" class="btn primary">
                Add Contact
              </button>
              <button type="button" id="btnClearLocal" class="btn destructive">
                Clear Local Data
              </button>
            </div>
          </form>

          <div class="pill-list" id="contactList">
            <!-- contact chips -->
          </div>
        </div>
      </section>
    </main>
  </div>

  <!-- Smart confirmation bar -->
  <div id="confirmBar" class="confirm-bar">
    <div class="confirm-text">
      Sending SOS alert in
      <span id="confirmCount" class="confirm-count">3</span>
      seconds…
    </div>
    <button id="confirmCancelBtn" class="confirm-cancel-btn">
      Cancel
    </button>
  </div>

  <!-- Toast -->
  <div id="toast" class="toast"></div>

  <script>
    // Simple front-end state
    const state = {
      sosActive: false,
      lastLocation: null,
      lastLocationTime: null,
      geofences: [],
      contacts: [],
    };

    // DOM refs
    const tabs = document.querySelectorAll(".tab");
    const sections = document.querySelectorAll(".section");
    const globalStatusPill = document.getElementById("globalStatusPill");
    const statusText = document.getElementById("statusText");
    const statusMeta = document.getElementById("statusMeta");
    const locationText = document.getElementById("locationText");
    const locationMeta = document.getElementById("locationMeta");
    const sosCircle = document.getElementById("sosCircle");
    const sosHint = document.getElementById("sosHint");
    const sosMeta = document.getElementById("sosMeta");
    const btnSafe = document.getElementById("btnSafe");
    const btnCancelSos = document.getElementById("btnCancelSos");
    const geofenceForm = document.getElementById("geofenceForm");
    const geofenceList = document.getElementById("geofenceList");
    const contactForm = document.getElementById("contactForm");
    const contactList = document.getElementById("contactList");
    const btnClearLocal = document.getElementById("btnClearLocal");
    const toastEl = document.getElementById("toast");
    const confirmBar = document.getElementById("confirmBar");
    const confirmCountEl = document.getElementById("confirmCount");
    const confirmCancelBtn = document.getElementById("confirmCancelBtn");

    // Local storage helpers
    const STORAGE_KEY = "saferadius-demo-v1";

    function loadState() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return;
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed.geofences)) state.geofences = parsed.geofences;
        if (Array.isArray(parsed.contacts)) state.contacts = parsed.contacts;
      } catch (e) {
        console.warn("Could not load saved state", e);
      }
    }

    function saveState() {
      try {
        localStorage.setItem(
          STORAGE_KEY,
          JSON.stringify({
            geofences: state.geofences,
            contacts: state.contacts,
          })
        );
      } catch (e) {
        console.warn("Could not save state", e);
      }
    }

    function clearLocalData() {
      localStorage.removeItem(STORAGE_KEY);
      state.geofences = [];
      state.contacts = [];
      renderGeofences();
      renderContacts();
      showToast("Local demo data cleared for this browser.", "warn");
    }

    // Toasts
    let toastTimer = null;
    function showToast(message, type = "info") {
      toastEl.textContent = message;
      toastEl.className = "toast visible";
      if (type === "warn") toastEl.classList.add("warn");
      if (type === "error") toastEl.classList.add("error");
      if (type === "success") toastEl.classList.add("toast-success");

      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        toastEl.classList.remove("visible");
      }, 2600);
    }

    // Global status
    function setGlobalStatus(isSos) {
      state.sosActive = isSos;
      if (isSos) {
        globalStatusPill.textContent = "Status: SOS Active";
        globalStatusPill.classList.remove("safe");
        globalStatusPill.classList.add("sos");
        statusText.textContent = "SOS triggered. Your location is being shared.";
        statusMeta.textContent = "Keep your phone powered and reachable.";
        sosHint.textContent = "SOS Active";
      } else {
        globalStatusPill.textContent = "Status: Safe";
        globalStatusPill.classList.add("safe");
        globalStatusPill.classList.remove("sos");
        statusText.textContent = "Safe. No active SOS.";
        statusMeta.textContent = "Last updated just now.";
        sosHint.textContent = "Press & Hold";
      }
    }

    // Render location
    function renderLocation() {
      if (!state.lastLocation) {
        locationText.textContent = "Location not requested yet.";
        locationMeta.textContent = "Your browser will ask for permission when needed.";
        return;
      }
      const { lat, lng, accuracy } = state.lastLocation;
      locationText.textContent = `Lat: ${lat.toFixed(5)}, Lng: ${lng.toFixed(
        5
      )} (±${Math.round(accuracy)} m)`;
      locationMeta.textContent = state.lastLocationTime
        ? `Last updated at ${state.lastLocationTime.toLocaleTimeString()}`
        : "Location updated.";
    }

    // Geofence rendering
    function renderGeofences() {
      geofenceList.innerHTML = "";
      if (!state.geofences.length) {
        const span = document.createElement("span");
        span.className = "info-muted";
        span.textContent = "No zones yet. Add a home or office zone above.";
        geofenceList.appendChild(span);
        return;
      }

      state.geofences.forEach((zone, index) => {
        const pill = document.createElement("div");
        pill.className = "item-pill";

        const icon = document.createElement("div");
        icon.className = "item-icon";
        icon.textContent =
          zone.name.toLowerCase().includes("home") ? "🏠" : "📍";

        const main = document.createElement("span");
        main.textContent = zone.name;

        const detail = document.createElement("small");
        const timeLabel =
          zone.time === "night"
            ? "Night alerts"
            : zone.time === "day"
            ? "Day alerts"
            : "Any time";
        detail.textContent = `${zone.radius} m · ${timeLabel}`;

        const remove = document.createElement("button");
        remove.className = "item-remove";
        remove.innerHTML = "&times;";
        remove.title = "Remove zone";
        remove.addEventListener("click", () => {
          state.geofences.splice(index, 1);
          saveState();
          renderGeofences();
          showToast("Zone removed from this demo.", "warn");
        });

        pill.appendChild(icon);
        pill.appendChild(main);
        pill.appendChild(detail);
        remove && pill.appendChild(remove);
        geofenceList.appendChild(pill);
      });
    }

    // Contact rendering
    function renderContacts() {
      contactList.innerHTML = "";
      if (!state.contacts.length) {
        const span = document.createElement("span");
        span.className = "info-muted";
        span.textContent = "No emergency contacts yet. Add at least one above.";
        contactList.appendChild(span);
        return;
      }

      state.contacts.forEach((contact, index) => {
        const pill = document.createElement("div");
        pill.className = "item-pill";

        const icon = document.createElement("div");
        icon.className = "item-icon";
        icon.textContent = "👤";

        const main = document.createElement("span");
        main.textContent = contact.name;

        const detail = document.createElement("small");
        detail.textContent = `${contact.relation || "Contact"} · ${
          contact.phone
        }`;

        const remove = document.createElement("button");
        remove.className = "item-remove";
        remove.innerHTML = "&times;";
        remove.title = "Remove contact";
        remove.addEventListener("click", () => {
          state.contacts.splice(index, 1);
          saveState();
          renderContacts();
          showToast("Contact removed from this demo.", "warn");
        });

        pill.appendChild(icon);
        pill.appendChild(main);
        pill.appendChild(detail);
        pill.appendChild(remove);
        contactList.appendChild(pill);
      });
    }

    // Tabs
    tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        const targetId = tab.getAttribute("data-target");
        tabs.forEach((t) => t.classList.remove("active"));
        sections.forEach((s) => s.classList.remove("active"));
        tab.classList.add("active");
        document.getElementById(targetId).classList.add("active");
      });
    });

    // Geolocation / SOS
    function requestLocationForSos() {
      if (!("geolocation" in navigator)) {
        showToast("Geolocation not supported in this browser.", "error");
        locationText.textContent = "Geolocation not supported.";
        locationMeta.textContent = "Try a modern mobile browser.";
        return;
      }

      locationMeta.textContent = "Requesting GPS location…";
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude, accuracy } = position.coords;
          state.lastLocation = {
            lat: latitude,
            lng: longitude,
            accuracy: accuracy || 0,
          };
          state.lastLocationTime = new Date();
          renderLocation();
          showToast("Location captured for SOS demo.", "success");
        },
        (err) => {
          console.warn("Geolocation error", err);
          locationText.textContent =
            "Could not get location. Check permissions or GPS.";
          locationMeta.textContent =
            "Please enable location permission and try again.";
          showToast("Location failed. Check GPS permission.", "error");
        },
        {
          enableHighAccuracy: true,
          timeout: 8000,
          maximumAge: 0,
        }
      );
    }

    function finaliseSosSend() {
      setGlobalStatus(true);
      sosMeta.textContent =
        "In a real system, your trusted contacts and helpers would now be notified.";
      btnCancelSos.disabled = false;
      requestLocationForSos();
      showToast("SOS sent in this UI demo.", "success");
    }

    let confirmTimer = null;
    let confirmCountdownTimer = null;

    function startConfirmCountdown() {
      let remaining = 3;
      confirmCountEl.textContent = String(remaining);
      confirmBar.classList.add("visible");

      clearTimeout(confirmTimer);
      clearInterval(confirmCountdownTimer);

      confirmCountdownTimer = setInterval(() => {
        remaining -= 1;
        confirmCountEl.textContent = String(remaining);
        if (remaining <= 0) {
          clearInterval(confirmCountdownTimer);
        }
      }, 1000);

      confirmTimer = setTimeout(() => {
        confirmBar.classList.remove("visible");
        finaliseSosSend();
      }, 3000);
    }

    function cancelConfirmCountdown() {
      confirmBar.classList.remove("visible");
      clearTimeout(confirmTimer);
      clearInterval(confirmCountdownTimer);
      showToast("SOS cancelled before sending.", "warn");
    }

    confirmCancelBtn.addEventListener("click", cancelConfirmCountdown);

    let sosHoldTimer = null;
    const SOS_HOLD_MS = 900;

    function handleSosStart() {
      sosHint.textContent = "Hold…";
      sosCircle.style.transform = "scale(0.97)";
      sosHoldTimer = setTimeout(() => {
        sosCircle.style.transform = "";
        startConfirmCountdown();
      }, SOS_HOLD_MS);
    }

    function handleSosEnd() {
      sosCircle.style.transform = "";
      if (sosHoldTimer) {
        clearTimeout(sosHoldTimer);
        sosHoldTimer = null;
        if (!state.sosActive && !confirmBar.classList.contains("visible")) {
          sosHint.textContent = "Press & Hold";
          showToast("Hold a bit longer to trigger SOS.", "info");
        }
      }
    }

    sosCircle.addEventListener("mousedown", handleSosStart);
    sosCircle.addEventListener("mouseup", handleSosEnd);
    sosCircle.addEventListener("mouseleave", handleSosEnd);
    sosCircle.addEventListener("touchstart", (e) => {
      e.preventDefault();
      handleSosStart();
    });
    sosCircle.addEventListener("touchend", (e) => {
      e.preventDefault();
      handleSosEnd();
    });

    btnSafe.addEventListener("click", () => {
      setGlobalStatus(false);
      sosMeta.textContent =
        "Tap SOS if you ever feel unsafe. Tap “I’m Safe” when you reach home.";
      btnCancelSos.disabled = true;
      cancelConfirmCountdown();
      showToast("Status set to safe.", "success");
    });

    btnCancelSos.addEventListener("click", () => {
      setGlobalStatus(false);
      sosMeta.textContent =
        "Location is only used when SOS is active or you choose to share it.";
      btnCancelSos.disabled = true;
      cancelConfirmCountdown();
    });

    // Geofence form
    geofenceForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("gfName").value.trim();
      const radius = Number(document.getElementById("gfRadius").value);
      const timeRule = document.getElementById("gfTime").value;
      const note = document.getElementById("gfNote").value.trim();

      if (!name || !radius || radius <= 0) {
        showToast("Enter a valid zone name and radius.", "error");
        return;
      }

      state.geofences.push({
        name,
        radius,
        time: timeRule,
        note,
        createdAt: Date.now(),
      });
      saveState();
      renderGeofences();
      geofenceForm.reset();
      document.getElementById("gfRadius").value = 300;
      showToast("Zone saved locally for this demo.", "success");
    });

    // Contacts form
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("contactName").value.trim();
      const relation = document
        .getElementById("contactRelation")
        .value.trim();
      const phone = document.getElementById("contactPhone").value.trim();

      if (!name || !phone) {
        showToast("Name and phone are required.", "error");
        return;
      }

      state.contacts.push({
        name,
        relation,
        phone,
        createdAt: Date.now(),
      });
      saveState();
      renderContacts();
      contactForm.reset();
      showToast("Contact added (demo only, no real SMS).", "success");
    });

    btnClearLocal.addEventListener("click", clearLocalData);

    // Init
    loadState();
    renderGeofences();
    renderContacts();
    setGlobalStatus(false);
    renderLocation();
  </script>
</body>
</html>
<audio id="emergencySound" src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" preload="auto"></audio>

