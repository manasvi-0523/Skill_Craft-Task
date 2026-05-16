import { useState, useEffect, useRef, useCallback } from "react";

/* ── Design tokens ─────────────────────────────────────────────────────────
   One accent, one warning, one danger. No gradients, no glow, no neon.
   Spacing scale: 4 8 12 16 24 32 48. Border-radius: 6px everywhere.
───────────────────────────────────────────────────────────────────────────── */
const T = {
  bg: "#0d1117",
  surface: "#161b22",
  border: "#21262d",
  text: "#e6edf3",
  muted: "#7d8590",
  accent: "#58a6ff",
  ok: "#3fb950",
  warn: "#d29922",
  danger: "#f85149",
  mono: "'Courier New', monospace",
  sans: "system-ui, -apple-system, sans-serif",
};

/* ── Helpers ───────────────────────────────────────────────────────────── */
const KEYBOARD_ROWS = [
  ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
  ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "↵"],
  ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", " -", "="],
];

function calcWPM(chars, ms) {
  if (ms < 1000) return 0;
  return Math.round((chars / 5) / (ms / 60000));
}

function heatColor(count, max) {
  if (!count || !max) return { bg: T.surface, color: T.muted };
  const t = count / max;
  if (t < 0.33) return { bg: "#1c2d3f", color: T.accent };
  if (t < 0.66) return { bg: "#1b4332", color: T.ok };
  return { bg: "#3d1f1f", color: T.danger };
}

/* ── Tiny SVG line chart ───────────────────────────────────────────────── */
function WpmChart({ data }) {
  if (!data || data.length < 2) return (
    <p style={{ color: T.muted, fontSize: 11, fontFamily: T.mono, margin: 0 }}>
      Data appears every 3 s of typing
    </p>
  );
  const W = 400, H = 60, pl = 32, pb = 16, pt = 4, pr = 4;
  const iw = W - pl - pr, ih = H - pt - pb;
  const maxY = Math.max(...data.map(d => d.wpm), 1);
  const pts = data.map((d, i) =>
    `${pl + (i / (data.length - 1)) * iw},${pt + (1 - d.wpm / maxY) * ih}`
  ).join(" ");
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: H, display: "block" }}>
      <text x={pl - 4} y={pt + 4} fontSize={9} fill={T.muted} textAnchor="end">{maxY}</text>
      <text x={pl - 4} y={pt + ih} fontSize={9} fill={T.muted} textAnchor="end">0</text>
      <line x1={pl} y1={pt} x2={pl} y2={pt + ih} stroke={T.border} />
      <line x1={pl} y1={pt + ih} x2={pl + iw} y2={pt + ih} stroke={T.border} />
      <polyline points={pts} fill="none" stroke={T.accent} strokeWidth={1.5} />
      <text x={pl} y={H} fontSize={9} fill={T.muted}>{data[0].t}s</text>
      <text x={pl + iw} y={H} fontSize={9} fill={T.muted} textAnchor="end">{data[data.length - 1].t}s</text>
    </svg>
  );
}

/* ── Stat block ────────────────────────────────────────────────────────── */
function Stat({ label, value, color, sub }) {
  return (
    <div>
      <div style={{ fontSize: 28, fontWeight: 700, fontFamily: T.mono, color: color || T.text, lineHeight: 1 }}>{value}</div>
      <div style={{ fontSize: 11, color: T.muted, marginTop: 4 }}>{label}</div>
      {sub && <div style={{ fontSize: 10, color: T.muted, fontFamily: T.mono, marginTop: 2 }}>{sub}</div>}
    </div>
  );
}

/* ── Main component ────────────────────────────────────────────────────── */
export default function TypingBehaviorResearch() {
  // phase: "idle" | "recording" | "review"
  const [phase, setPhase] = useState("idle");
  const [inputText, setInputText] = useState("");
  const [keyLog, setKeyLog] = useState([]);
  const [keyFreq, setKeyFreq] = useState({});
  const [wpmHistory, setWpmHistory] = useState([]);
  const [totalKeys, setTotalKeys] = useState(0);
  const [backspaces, setBackspaces] = useState(0);
  const [dwell, setDwell] = useState([]);

  const sessionRef = useRef(null);
  const lastTimeRef = useRef(null);
  const totalKeysRef = useRef(0);
  const isRecRef = useRef(false);
  const wpmTimer = useRef(null);
  const textRef = useRef(null);

  /* Start */
  const startSession = useCallback(() => {
    sessionRef.current = Date.now();
    lastTimeRef.current = null;
    totalKeysRef.current = 0;
    isRecRef.current = true;
    setPhase("recording");
    setInputText(""); setKeyLog([]); setKeyFreq({});
    setWpmHistory([]); setTotalKeys(0); setBackspaces(0); setDwell([]);
    setTimeout(() => textRef.current?.focus(), 50);
  }, []);

  /* Stop */
  const stopSession = useCallback(() => {
    isRecRef.current = false;
    clearInterval(wpmTimer.current);
    setPhase("review");
  }, []);

  /* Reset */
  const reset = useCallback(() => {
    setPhase("idle");
    setInputText(""); setKeyLog([]); setKeyFreq({});
    setWpmHistory([]); setTotalKeys(0); setBackspaces(0); setDwell([]);
    totalKeysRef.current = 0;
  }, []);

  /* WPM interval — reads refs only, one setState */
  useEffect(() => {
    if (phase !== "recording") return;
    wpmTimer.current = setInterval(() => {
      if (!sessionRef.current) return;
      const elapsed = Date.now() - sessionRef.current;
      const wpm = calcWPM(totalKeysRef.current, elapsed);
      setWpmHistory(h => [...h.slice(-29), { t: Math.round(elapsed / 1000), wpm }]);
    }, 3000);
    return () => clearInterval(wpmTimer.current);
  }, [phase]);

  /* Key handler — stable, uses refs */
  const handleKeyDown = useCallback((e) => {
    if (!isRecRef.current) return;
    const key = e.key;
    const now = Date.now();
    let type = "other";
    if (key.length === 1 && key !== " ") type = "letter";
    else if (key === " ") type = "space";
    else if (key === "Backspace") type = "backspace";
    else if (key === "Enter") type = "enter";

    const display = { space: "SPC", backspace: "⌫", enter: "↵" }[type] ?? key;
    setKeyLog(l => [...l.slice(-49), { key: display, type }]);
    setKeyFreq(f => { const k = key.toUpperCase(); return { ...f, [k]: (f[k] || 0) + 1 }; });
    setTotalKeys(t => { const n = t + 1; totalKeysRef.current = n; return n; });
    if (key === "Backspace") setBackspaces(b => b + 1);
    if (lastTimeRef.current) {
      const iv = now - lastTimeRef.current;
      if (iv < 2000) setDwell(d => [...d.slice(-49), iv]);
    }
    lastTimeRef.current = now;
  }, []);

  /* Export */
  const exportData = useCallback(() => {
    const elapsed = sessionRef.current ? Date.now() - sessionRef.current : 0;
    const blob = new Blob([JSON.stringify({
      timestamp: new Date().toISOString(),
      session_duration_s: Math.round(elapsed / 1000),
      total_keystrokes: totalKeys,
      backspaces,
      accuracy_pct: totalKeys ? Math.max(0, Math.round(((totalKeys - backspaces) / totalKeys) * 100)) : 100,
      avg_wpm: calcWPM(totalKeys, elapsed),
      avg_key_interval_ms: dwell.length ? Math.round(dwell.reduce((a, b) => a + b, 0) / dwell.length) : 0,
      key_frequency: keyFreq,
      wpm_timeline: wpmHistory,
    }, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `typing_session_${Date.now()}.json`;
    a.click();
  }, [totalKeys, backspaces, dwell, keyFreq, wpmHistory]);

  /* Derived */
  const elapsed = sessionRef.current ? Date.now() - sessionRef.current : 0;
  const currentWPM = calcWPM(totalKeys, elapsed);
  const accuracy = totalKeys === 0 ? 100 : Math.max(0, Math.round(((totalKeys - backspaces) / totalKeys) * 100));
  const avgInterval = dwell.length ? Math.round(dwell.reduce((a, b) => a + b, 0) / dwell.length) : 0;
  const maxFreq = Math.max(...Object.values(keyFreq), 1);
  const topKeys = Object.entries(keyFreq).sort((a, b) => b[1] - a[1]).slice(0, 8).map(([k, v]) => ({ key: k, count: v }));
  const wpmColor = currentWPM >= 60 ? T.ok : currentWPM >= 30 ? T.warn : T.muted;
  const accColor = accuracy >= 95 ? T.ok : accuracy >= 80 ? T.warn : T.danger;

  /* Shared styles */
  const card = { background: T.surface, borderRadius: 6, padding: 20 };
  const label = { fontSize: 11, color: T.muted, textTransform: "uppercase", letterSpacing: "0.06em" };
  const hr = { border: "none", borderTop: `1px solid ${T.border}`, margin: "24px 0" };

  const Btn = ({ onClick, disabled, children, variant = "accent" }) => {
    const colors = {
      accent: { bg: T.accent, fg: "#0d1117" },
      ghost: { bg: "transparent", fg: T.muted, border: `1px solid ${T.border}` },
      danger: { bg: "transparent", fg: T.danger, border: `1px solid ${T.danger}` },
    }[variant];
    return (
      <button onClick={onClick} disabled={disabled} style={{
        padding: "9px 20px", borderRadius: 6, fontSize: 14, fontWeight: 600,
        fontFamily: T.sans, cursor: disabled ? "not-allowed" : "pointer",
        border: colors.border || "none", background: colors.bg, color: colors.fg,
        opacity: disabled ? 0.4 : 1, transition: "opacity 0.15s",
      }}>{children}</button>
    );
  };

  /* ── RENDER ─────────────────────────────────────────────────────────── */
  return (
    <div style={{ minHeight: "100vh", background: T.bg, color: T.text, fontFamily: T.sans }}>
      <div style={{ maxWidth: 720, margin: "0 auto", padding: "48px 24px" }}>

        {/* ── Top identity ── */}
        <div style={{ marginBottom: 48 }}>
          <p style={{ ...label, marginBottom: 8 }}>SkillCraft Technology · Task 03</p>
          <h1 style={{ fontSize: 32, fontWeight: 700, margin: "0 0 8px", lineHeight: 1.2 }}>
            Typing Behavior Research
          </h1>
          <p style={{ fontSize: 14, color: T.muted, margin: 0, lineHeight: 1.6 }}>
            Measures your WPM, accuracy, and keystroke patterns in-browser.<br />
            All data stays local — nothing is transmitted.
          </p>
        </div>

        {/* ════════════════════════════════════════
            PHASE: IDLE
        ════════════════════════════════════════ */}
        {phase === "idle" && (
          <div>
            <div style={{ ...card, marginBottom: 16 }}>
              <p style={{ ...label, marginBottom: 12 }}>Before you begin</p>
              <p style={{ fontSize: 14, color: T.muted, margin: 0, lineHeight: 1.7 }}>
                This tool listens to keyboard events <strong style={{ color: T.text }}>only inside the text box below</strong>.
                It captures key type, timing intervals, and frequency — never passwords or sensitive fields.
                Data is stored in memory and exported as JSON on request.
              </p>
            </div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 12, marginBottom: 32 }}>
              {[
                ["WPM", "Live words-per-minute as you type"],
                ["Accuracy", "Backspace rate vs total keystrokes"],
                ["Heatmap", "Which keys you use most often"],
              ].map(([title, desc]) => (
                <div key={title} style={{ background: T.surface, borderRadius: 6, padding: 16 }}>
                  <div style={{ fontSize: 13, fontWeight: 600, marginBottom: 6 }}>{title}</div>
                  <div style={{ fontSize: 12, color: T.muted, lineHeight: 1.6 }}>{desc}</div>
                </div>
              ))}
            </div>

            <Btn onClick={startSession}>Start Session</Btn>
          </div>
        )}

        {/* ════════════════════════════════════════
            PHASE: RECORDING
        ════════════════════════════════════════ */}
        {phase === "recording" && (
          <div>
            {/* Live stats — compact, above the textarea */}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 12, marginBottom: 20 }}>
              <Stat label="WPM" value={currentWPM} color={wpmColor} />
              <Stat label="Accuracy" value={`${accuracy}%`} color={accColor} />
              <Stat label="Keystrokes" value={totalKeys} sub={`${backspaces} ⌫`} />
              <Stat label="Interval" value={avgInterval ? `${avgInterval}ms` : "—"} />
            </div>

            {/* Typing area */}
            <div style={{ marginBottom: 12 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                <span style={{ width: 7, height: 7, borderRadius: "50%", background: T.ok, display: "inline-block", animation: "pulse 1.5s infinite" }} />
                <span style={{ fontSize: 12, color: T.muted }}>Recording</span>
              </div>
              <textarea
                ref={textRef}
                value={inputText}
                onChange={e => setInputText(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Type anything here…"
                style={{
                  width: "100%", minHeight: 140, background: T.surface, border: `1px solid ${T.ok}33`,
                  borderRadius: 6, padding: 16, fontFamily: T.mono, fontSize: 14,
                  color: T.text, resize: "vertical", outline: "none", boxSizing: "border-box",
                  lineHeight: 1.7,
                }}
              />
            </div>

            {/* Live key stream */}
            <div style={{ display: "flex", flexWrap: "wrap", gap: 3, minHeight: 32, marginBottom: 20 }}>
              {keyLog.length === 0 && <span style={{ fontSize: 11, color: T.muted, fontFamily: T.mono }}>Keys will appear here…</span>}
              {keyLog.map((k, i) => {
                const clr = { letter: T.accent, space: T.ok, backspace: T.danger, enter: T.warn, other: T.muted }[k.type];
                return (
                  <span key={i} style={{ fontSize: 10, fontFamily: T.mono, color: clr, padding: "1px 5px", background: `${clr}15`, borderRadius: 3 }}>{k.key}</span>
                );
              })}
            </div>

            <Btn onClick={stopSession} variant="danger">Stop &amp; Review</Btn>
          </div>
        )}

        {/* ════════════════════════════════════════
            PHASE: REVIEW
        ════════════════════════════════════════ */}
        {phase === "review" && (
          <div>
            {/* Summary */}
            <div style={{ marginBottom: 8 }}>
              <p style={{ ...label, marginBottom: 16 }}>Session summary</p>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16 }}>
                <Stat label="Avg WPM" value={currentWPM} color={wpmColor} />
                <Stat label="Accuracy" value={`${accuracy}%`} color={accColor} />
                <Stat label="Keystrokes" value={totalKeys} sub={`${backspaces} backspaces`} />
                <Stat label="Key interval" value={avgInterval ? `${avgInterval}ms` : "—"} sub={avgInterval ? `${Math.round(1000 / avgInterval)} keys/s` : ""} />
              </div>
            </div>

            <hr style={hr} />

            {/* Speed classification */}
            <div style={{ marginBottom: 24 }}>
              <p style={{ ...label, marginBottom: 12 }}>Speed classification</p>
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                {[
                  ["Beginner", "< 30", currentWPM < 30],
                  ["Intermediate", "30–60", currentWPM >= 30 && currentWPM < 60],
                  ["Advanced", "60–90", currentWPM >= 60 && currentWPM < 90],
                  ["Professional", "> 90", currentWPM >= 90],
                ].map(([name, range, active]) => (
                  <div key={name} style={{
                    padding: "8px 14px", borderRadius: 6, fontSize: 13,
                    background: active ? `${T.accent}18` : T.surface,
                    border: `1px solid ${active ? T.accent : T.border}`,
                    color: active ? T.accent : T.muted,
                  }}>
                    {name} <span style={{ fontFamily: T.mono, fontSize: 11 }}>{range} WPM</span>
                  </div>
                ))}
              </div>
            </div>

            <hr style={hr} />

            {/* WPM chart */}
            <div style={{ marginBottom: 24 }}>
              <p style={{ ...label, marginBottom: 12 }}>WPM over time</p>
              <WpmChart data={wpmHistory} />
            </div>

            <hr style={hr} />

            {/* Keyboard heatmap */}
            <div style={{ marginBottom: 24 }}>
              <p style={{ ...label, marginBottom: 12 }}>Key frequency heatmap</p>
              <div style={{ display: "flex", flexDirection: "column", gap: 3 }}>
                {KEYBOARD_ROWS.map((row, ri) => (
                  <div key={ri} style={{ display: "flex", gap: 3 }}>
                    {row.map(k => {
                      const { bg, color } = heatColor(keyFreq[k] || 0, maxFreq);
                      return (
                        <div key={k} style={{
                          width: 36, height: 36, borderRadius: 4, display: "flex",
                          alignItems: "center", justifyContent: "center",
                          background: bg, color, fontSize: 10, fontFamily: T.mono, fontWeight: 500,
                          flexShrink: 0,
                        }}>{k}</div>
                      );
                    })}
                  </div>
                ))}
              </div>
              <div style={{ display: "flex", gap: 16, marginTop: 12, fontSize: 11, color: T.muted, fontFamily: T.mono }}>
                <span style={{ color: T.accent }}>■ low</span>
                <span style={{ color: T.ok }}>■ mid</span>
                <span style={{ color: T.danger }}>■ high</span>
              </div>
            </div>

            {/* Top keys bar chart */}
            {topKeys.length > 0 && (
              <>
                <hr style={hr} />
                <div style={{ marginBottom: 24 }}>
                  <p style={{ ...label, marginBottom: 12 }}>Most-used keys</p>
                  <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                    {topKeys.map(({ key, count }) => (
                      <div key={key} style={{ display: "flex", alignItems: "center", gap: 10 }}>
                        <span style={{ width: 22, fontSize: 11, fontFamily: T.mono, color: T.muted, textAlign: "right" }}>{key}</span>
                        <div style={{ flex: 1, height: 12, background: T.border, borderRadius: 3, overflow: "hidden" }}>
                          <div style={{ width: `${(count / topKeys[0].count) * 100}%`, height: "100%", background: T.accent, borderRadius: 3 }} />
                        </div>
                        <span style={{ width: 24, fontSize: 11, fontFamily: T.mono, color: T.muted }}>{count}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            )}

            <hr style={hr} />

            {/* Actions */}
            <div style={{ display: "flex", gap: 10 }}>
              <Btn onClick={exportData}>Export JSON</Btn>
              <Btn onClick={reset} variant="ghost">New Session</Btn>
            </div>
          </div>
        )}

        {/* Footer */}
        <p style={{ fontSize: 11, color: T.muted, marginTop: 48, fontFamily: T.mono }}>
          All processing is client-side. Zero network requests.
        </p>
      </div>

      <style>{`
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
        textarea::placeholder { color: #7d8590; }
        button:hover:not(:disabled) { opacity: 0.85 !important; }
      `}</style>
    </div>
  );
}
