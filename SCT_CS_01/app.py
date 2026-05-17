"""
app.py — SecureText Studio
SkillCraft Cybersecurity Internship | Task 01
Run: python -m streamlit run app.py
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from caesar import encrypt, decrypt, brute_force, letter_frequency, cipher_stats, ENGLISH_FREQ

# ─── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CAESAR CIPHER",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Session state init ───────────────────────────────────────────────────────
if "result_text"  not in st.session_state: st.session_state.result_text  = ""
if "mode_label"   not in st.session_state: st.session_state.mode_label   = "OUTPUT"
if "accent_color" not in st.session_state: st.session_state.accent_color = "#8b949e"

# ─── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --bg:      #0d1117;
    --surface: #161b22;
    --border:  #30363d;
    --accent:  #00e5a0;
    --accent2: #58a6ff;
    --danger:  #ff6b6b;
    --warn:    #ffa94d;
    --text:    #e6edf3;
    --muted:   #8b949e;
}

.stApp { background: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; }
.main .block-container { padding: 1.5rem 2rem 3rem; max-width: 1100px; }
#MainMenu, footer, header { visibility: hidden; }

.stTabs [data-baseweb="tab-list"] {
    gap: 4px; background: var(--surface);
    border-radius: 10px; padding: 4px; border: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 7px; color: var(--muted);
    font-family: 'Space Mono', monospace; font-size: 13px;
    padding: 8px 20px; border: none; background: transparent;
}
.stTabs [aria-selected="true"] {
    background: var(--accent) !important; color: #000 !important; font-weight: 700;
}
.stTextArea textarea {
    background: var(--surface) !important; border: 1px solid var(--border) !important;
    border-radius: 8px !important; color: var(--text) !important;
    font-family: 'Space Mono', monospace !important; font-size: 14px !important;
}
.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(0,229,160,0.15) !important;
}
.stButton > button {
    background: var(--accent) !important; color: #000 !important;
    border: none !important; border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important; font-weight: 700 !important;
    font-size: 13px !important; padding: 10px 24px !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(0,229,160,0.3) !important;
}
[data-testid="metric-container"] {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 10px; padding: 14px !important;
}
[data-testid="stMetricValue"] {
    color: var(--accent) !important;
    font-family: 'Space Mono', monospace !important; font-size: 22px !important;
}
[data-testid="stMetricLabel"] { color: var(--muted) !important; font-size: 12px !important; }
hr { border-color: var(--border) !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:2rem 0 1.5rem;">
    <div style="font-family:'Space Mono',monospace; font-size:11px;
                color:#00e5a0; letter-spacing:6px; margin-bottom:10px;">
        SKILLCRAFT · CYBERSECURITY · TASK 01
    </div>
    <h1 style="font-family:'Space Mono',monospace; font-size:2.6rem;
               font-weight:700; color:#e6edf3; margin:0; letter-spacing:-1px;">
        🔐 SecureText Studio
    </h1>
    <p style="color:#8b949e; font-size:15px; margin-top:10px;">
        Caesar Cipher &nbsp;·&nbsp; Brute-Force Attack &nbsp;·&nbsp; Frequency Analysis
    </p>
    <div style="width:60px; height:2px; background:#00e5a0;
                margin:16px auto 0; border-radius:2px;"></div>
</div>
""", unsafe_allow_html=True)

# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "⚡  Encrypt / Decrypt",
    "💥  Brute-Force Attack",
    "📊  Frequency Analysis"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — Encrypt / Decrypt
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.2, 1], gap="large")

    # ── Left: inputs and output ───────────────────────────────────────────────
    with col_left:
        st.markdown("""
        <p style="font-family:'Space Mono',monospace; font-size:12px;
                  color:#00e5a0; letter-spacing:2px; margin-bottom:6px;">
            INPUT MESSAGE
        </p>""", unsafe_allow_html=True)

        input_text = st.text_area(
            label="input", label_visibility="collapsed",
            placeholder="Type or paste your message here...",
            height=160, key="enc_input"
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <p style="font-family:'Space Mono',monospace; font-size:12px;
                  color:#00e5a0; letter-spacing:2px; margin-bottom:6px;">
            SHIFT KEY <span style="color:#8b949e">(1 – 25)</span>
        </p>""", unsafe_allow_html=True)

        shift = st.slider("shift", 1, 25, 3, label_visibility="collapsed")

        st.markdown(f"""
        <div style="background:#161b22; border:1px solid #30363d; border-radius:8px;
                    padding:12px 16px; display:flex; align-items:center;
                    gap:12px; margin-top:4px;">
            <span style="font-family:'Space Mono',monospace; font-size:28px;
                         color:#00e5a0; font-weight:700;">{shift}</span>
            <div>
                <div style="color:#e6edf3; font-size:13px;">positions shifted</div>
                <div style="color:#8b949e; font-size:11px; font-family:'Space Mono',monospace;">
                    A → {chr(ord('A') + shift % 26)} &nbsp;|&nbsp;
                    Z → {chr(ord('A') + (25 + shift) % 26)}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)

        if b1.button("🔒 Encrypt", use_container_width=True):
            if input_text.strip():
                st.session_state.result_text  = encrypt(input_text, shift)
                st.session_state.mode_label   = "ENCRYPTED OUTPUT"
                st.session_state.accent_color = "#00e5a0"
            else:
                st.session_state.result_text  = "__empty__"

        if b2.button("🔓 Decrypt", use_container_width=True):
            if input_text.strip():
                st.session_state.result_text  = decrypt(input_text, shift)
                st.session_state.mode_label   = "DECRYPTED OUTPUT"
                st.session_state.accent_color = "#58a6ff"
            else:
                st.session_state.result_text  = "__empty__"

        if b3.button("🗑 Clear", use_container_width=True):
            st.session_state.result_text  = ""
            st.session_state.mode_label   = "OUTPUT"
            st.session_state.accent_color = "#8b949e"

        # ── Output section ────────────────────────────────────────────────────
        result = st.session_state.result_text
        mlabel = st.session_state.mode_label
        acolor = st.session_state.accent_color

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <p style="font-family:'Space Mono',monospace; font-size:12px;
                  color:{acolor}; letter-spacing:2px; margin-bottom:6px;">
            {mlabel}
        </p>""", unsafe_allow_html=True)

        if result and result != "__empty__":
            bg = "#0d2b1a" if acolor == "#00e5a0" else "#0d1a2b"
            # Render output via st.code — never injected into HTML
            st.markdown(f"""
            <div style="background:{bg}; border:1.5px solid {acolor}; border-radius:8px;
                        padding:4px 8px 8px;">
            """, unsafe_allow_html=True)
            st.code(result, language=None)
            st.markdown("</div>", unsafe_allow_html=True)

            # Stats
            stats = cipher_stats(result)
            st.markdown("<br>", unsafe_allow_html=True)
            m1, m2, m3 = st.columns(3)
            m1.metric("Characters", stats['total_chars'])
            m2.metric("Letters",    stats['letters'])
            m3.metric("Symbols",    stats['symbols'])

            # Cipher map
            st.markdown("<br>", unsafe_allow_html=True)
            plain_alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            cipher_alpha = "".join(
                chr((ord(c) - ord('A') + shift) % 26 + ord('A')) for c in plain_alpha
            )
            st.markdown(f"""
            <p style="font-family:'Space Mono',monospace; font-size:11px;
                      color:#8b949e; letter-spacing:2px; margin-bottom:8px;">
                CIPHER ALPHABET MAP
            </p>
            <div style="background:#161b22; border:1px solid #30363d; border-radius:8px;
                        padding:14px 16px; font-family:'Space Mono',monospace; font-size:12px;">
                <div style="color:#8b949e; margin-bottom:6px;">Plain &nbsp;: {plain_alpha}</div>
                <div style="color:#00e5a0;">Cipher : {cipher_alpha}</div>
            </div>
            """, unsafe_allow_html=True)

        elif result == "__empty__":
            st.markdown("""
            <div style="background:#1c1010; border:1px dashed #ff6b6b;
                        border-radius:8px; padding:32px; text-align:center;">
                <div style="font-size:24px;">⚠️</div>
                <div style="color:#ff6b6b; font-family:'Space Mono',monospace;
                             font-size:12px; margin-top:8px;">
                    Please enter a message first
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background:#161b22; border:1px dashed #30363d; border-radius:8px;
                        padding:32px; text-align:center; min-height:155px;
                        display:flex; flex-direction:column;
                        align-items:center; justify-content:center;">
                <div style="font-size:32px; opacity:0.25;">🔐</div>
                <div style="color:#30363d; font-family:'Space Mono',monospace;
                             font-size:12px; margin-top:12px;">
                    Output will appear here
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── Right: Interactive Cipher Wheel ──────────────────────────────────────
    with col_right:
        st.markdown("""
        <p style="font-family:'Space Mono',monospace; font-size:12px;
                  color:#00e5a0; letter-spacing:2px; margin-bottom:10px;">
            INTERACTIVE CIPHER WHEEL
        </p>""", unsafe_allow_html=True)
        
        wheel_html = f"""
        <div style="background:#161b22; border:1px solid #30363d; border-radius:12px; 
                    padding:20px; margin-bottom:20px; user-select:none; -webkit-user-select:none; 
                    -moz-user-select:none; -ms-user-select:none;">
            <div id="wheel-container" style="position:relative; width:100%; max-width:450px; 
                                             margin:0 auto; aspect-ratio:1; user-select:none;">
                <svg id="cipher-wheel" viewBox="0 0 400 400" 
                     style="width:100%; height:100%; cursor:grab; user-select:none; 
                            -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none;">
                    <!-- Background -->
                    <circle cx="200" cy="200" r="200" fill="#0d1117"/>
                    
                    <!-- Decorative crosses -->
                    <text x="50" y="50" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="350" y="50" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="50" y="350" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="350" y="350" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="200" y="30" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="370" y="200" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="30" y="200" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    <text x="200" y="370" fill="#30363d" font-size="16" text-anchor="middle" 
                          style="pointer-events:none; user-select:none;">+</text>
                    
                    <!-- Outer circle -->
                    <circle cx="200" cy="200" r="180" fill="none" stroke="#00e5a0" stroke-width="2" 
                            style="pointer-events:none;"/>
                    
                    <!-- Outer ring letters (fixed plaintext) -->
                    <g id="outer-letters" style="pointer-events:none; user-select:none;">
                        {"".join(f'<text x="{200 + 160 * np.sin(i * 2 * np.pi / 26)}" y="{200 - 160 * np.cos(i * 2 * np.pi / 26)}" fill="#00e5a0" font-size="16" font-weight="bold" font-family="monospace" text-anchor="middle" dominant-baseline="middle" style="pointer-events:none; user-select:none;">{chr(65 + i)}</text>' for i in range(26))}
                    </g>
                    
                    <!-- Middle circle -->
                    <circle cx="200" cy="200" r="130" fill="none" stroke="#58a6ff" stroke-width="2" 
                            style="pointer-events:none;"/>
                    
                    <!-- Inner rotatable ring -->
                    <g id="inner-ring" transform="rotate({shift * 360 / 26} 200 200)" 
                       style="pointer-events:none; user-select:none;">
                        <!-- Inner circle -->
                        <circle cx="200" cy="200" r="80" fill="none" stroke="#8b949e" stroke-width="2"/>
                        
                        <!-- Radial lines -->
                        {"".join(f'<line x1="200" y1="200" x2="{200 + 130 * np.sin(i * 2 * np.pi / 26)}" y2="{200 - 130 * np.cos(i * 2 * np.pi / 26)}" stroke="#30363d" stroke-width="1.5"/>' for i in range(26))}
                        
                        <!-- Inner ring letters (rotatable ciphertext) -->
                        {"".join(f'<text x="{200 + 105 * np.sin(i * 2 * np.pi / 26)}" y="{200 - 105 * np.cos(i * 2 * np.pi / 26)}" fill="#58a6ff" font-size="14" font-family="monospace" text-anchor="middle" dominant-baseline="middle" style="pointer-events:none; user-select:none;">{chr(65 + i)}</text>' for i in range(26))}
                    </g>
                    
                    <!-- Center dot -->
                    <circle cx="200" cy="200" r="8" fill="#00e5a0" style="pointer-events:none;"/>
                </svg>
            </div>
            
            <div style="text-align:center; margin-top:15px; padding:10px; background:#0d1117; 
                        border-radius:8px; border:1px solid #30363d; user-select:none;">
                <span style="color:#8b949e; font-size:11px; font-family:'Space Mono',monospace;">
                    DRAG TO ROTATE &nbsp;|&nbsp; Current Shift: 
                    <span id="shift-display" style="color:#00e5a0; font-weight:bold; font-size:14px;">{shift}</span>
                </span>
            </div>
        </div>
        
        <script>
        (function() {{
            const wheel = document.getElementById('cipher-wheel');
            const innerRing = document.getElementById('inner-ring');
            const shiftDisplay = document.getElementById('shift-display');
            let isDragging = false;
            let currentRotation = {shift * 360 / 26};
            let startAngle = 0;
            
            // Prevent text selection during drag
            wheel.addEventListener('selectstart', (e) => e.preventDefault());
            wheel.addEventListener('dragstart', (e) => e.preventDefault());
            
            function getAngle(e, center) {{
                const rect = wheel.getBoundingClientRect();
                const x = (e.clientX || e.touches[0].clientX) - rect.left - center.x;
                const y = (e.clientY || e.touches[0].clientY) - rect.top - center.y;
                return Math.atan2(y, x) * 180 / Math.PI;
            }}
            
            function updateShift(rotation) {{
                const normalizedRotation = ((rotation % 360) + 360) % 360;
                const shift = Math.round(normalizedRotation / (360 / 26)) % 26;
                shiftDisplay.textContent = shift;
                return shift;
            }}
            
            wheel.addEventListener('mousedown', (e) => {{
                e.preventDefault();
                isDragging = true;
                wheel.style.cursor = 'grabbing';
                const rect = wheel.getBoundingClientRect();
                const center = {{ x: rect.width / 2, y: rect.height / 2 }};
                startAngle = getAngle(e, center) - currentRotation;
            }});
            
            wheel.addEventListener('touchstart', (e) => {{
                e.preventDefault();
                isDragging = true;
                const rect = wheel.getBoundingClientRect();
                const center = {{ x: rect.width / 2, y: rect.height / 2 }};
                startAngle = getAngle(e, center) - currentRotation;
            }}, {{ passive: false }});
            
            document.addEventListener('mousemove', (e) => {{
                if (!isDragging) return;
                e.preventDefault();
                const rect = wheel.getBoundingClientRect();
                const center = {{ x: rect.width / 2, y: rect.height / 2 }};
                currentRotation = getAngle(e, center) - startAngle;
                innerRing.setAttribute('transform', `rotate(${{currentRotation}} 200 200)`);
                updateShift(currentRotation);
            }});
            
            document.addEventListener('touchmove', (e) => {{
                if (!isDragging) return;
                e.preventDefault();
                const rect = wheel.getBoundingClientRect();
                const center = {{ x: rect.width / 2, y: rect.height / 2 }};
                currentRotation = getAngle(e, center) - startAngle;
                innerRing.setAttribute('transform', `rotate(${{currentRotation}} 200 200)`);
                updateShift(currentRotation);
            }}, {{ passive: false }});
            
            document.addEventListener('mouseup', () => {{
                if (isDragging) {{
                    isDragging = false;
                    wheel.style.cursor = 'grab';
                    // Snap to nearest position
                    const snapRotation = Math.round(currentRotation / (360 / 26)) * (360 / 26);
                    currentRotation = snapRotation;
                    innerRing.setAttribute('transform', `rotate(${{snapRotation}} 200 200)`);
                    updateShift(snapRotation);
                }}
            }});
            
            document.addEventListener('touchend', () => {{
                if (isDragging) {{
                    isDragging = false;
                    // Snap to nearest position
                    const snapRotation = Math.round(currentRotation / (360 / 26)) * (360 / 26);
                    currentRotation = snapRotation;
                    innerRing.setAttribute('transform', `rotate(${{snapRotation}} 200 200)`);
                    updateShift(snapRotation);
                }}
            }});
        }})();
        </script>
        """
        
        st.components.v1.html(wheel_html, height=580)

    # Explainer
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#161b22; border:1px solid #30363d;
                border-left:3px solid #00e5a0; border-radius:8px; padding:16px 20px;">
        <p style="font-family:'Space Mono',monospace; font-size:11px; color:#00e5a0;
                  letter-spacing:2px; margin:0 0 8px;">HOW CAESAR CIPHER WORKS</p>
        <p style="color:#8b949e; font-size:13px; margin:0; line-height:1.7;">
            Each letter is shifted forward by a fixed number of positions in the alphabet.
            With shift=3:
            <span style="color:#e6edf3; font-family:'Space Mono',monospace;">A→D, B→E, Z→C</span>.
            Decryption applies the reverse shift. Non-letter characters pass through unchanged.
            The key space is tiny — only 25 possibilities — making it trivially broken
            by brute force (see the next tab).
        </p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — Brute-Force
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#161b22; border:1px solid #ff6b6b; border-radius:10px;
                padding:16px 20px; margin-bottom:20px;">
        <p style="font-family:'Space Mono',monospace; font-size:11px; color:#ff6b6b;
                  letter-spacing:2px; margin:0 0 6px;">
            ⚠  ATTACK SIMULATION — EDUCATIONAL ONLY
        </p>
        <p style="color:#8b949e; font-size:13px; margin:0;">
            All 25 possible shifts are tried and scored against English letter frequency
            patterns to automatically identify the most likely plaintext.
        </p>
    </div>
    """, unsafe_allow_html=True)

    bf_input = st.text_area(
        "Paste ciphertext to crack:",
        placeholder="e.g.  Khoor Zruog  (that's 'Hello World' with shift 3)",
        height=120, key="bf_input"
    )
    run_bf = st.button("💥 Run Brute-Force Attack")

    if run_bf:
        if not bf_input.strip():
            st.warning("Please paste some ciphertext first.")
        else:
            with st.spinner("Trying all 25 shifts..."):
                results = brute_force(bf_input)

            top = results[0]
            confidence = min(round(((top['score'] + 300) / 400) * 100, 1), 99.9)
            top_text_display = top['text'][:250] + ('...' if len(top['text']) > 250 else '')

            # Header row: shift + confidence (no user text injected into HTML)
            st.markdown(f"""
            <div style="background:#0d2b1a; border:1px solid #00e5a0; border-radius:10px;
                        padding:20px 24px; margin:16px 0;">
                <p style="font-family:'Space Mono',monospace; font-size:11px; color:#00e5a0;
                          letter-spacing:2px; margin:0 0 14px;">&#10003;  MOST LIKELY RESULT</p>
                <div style="display:flex; align-items:center; gap:32px; flex-wrap:wrap;">
                    <div style="text-align:center; min-width:60px;">
                        <div style="color:#8b949e; font-size:10px;
                                    font-family:'Space Mono',monospace; margin-bottom:4px;">SHIFT</div>
                        <div style="color:#00e5a0; font-size:40px;
                                    font-family:'Space Mono',monospace;
                                    font-weight:700; line-height:1;">{top['shift']}</div>
                    </div>
                    <div style="text-align:center; min-width:80px;">
                        <div style="color:#8b949e; font-size:10px;
                                    font-family:'Space Mono',monospace; margin-bottom:4px;">CONFIDENCE</div>
                        <div style="color:#ffa94d; font-size:26px;
                                    font-family:'Space Mono',monospace; font-weight:700;">{confidence}%</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Decrypted text rendered by Streamlit — never injected into HTML
            st.markdown("""<p style="font-family:'Space Mono',monospace; font-size:11px;
                          color:#8b949e; letter-spacing:2px; margin:4px 0 6px;">
                          DECRYPTED TEXT</p>""", unsafe_allow_html=True)
            st.code(top_text_display, language=None)

            st.markdown("""
            <p style="font-family:'Space Mono',monospace; font-size:11px; color:#8b949e;
                      letter-spacing:2px; margin:20px 0 10px;">
                ALL 25 CANDIDATES — sorted by English frequency score
            </p>""", unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(11, 4))
            fig.patch.set_facecolor('#0d1117')
            ax.set_facecolor('#161b22')
            shifts_list = [r['shift'] for r in results]
            scores_list = [r['score'] for r in results]
            bar_colors  = ['#00e5a0' if r['likely'] else '#2d3748' for r in results]
            ax.barh([str(s) for s in shifts_list], scores_list,
                    color=bar_colors, edgecolor='none', height=0.65)
            ax.axvline(scores_list[0], color='#00e5a0', linewidth=1,
                       linestyle='--', alpha=0.4)
            ax.set_xlabel("English frequency score (higher = more likely)",
                          color='#8b949e', fontsize=10)
            ax.set_ylabel("Shift value", color='#8b949e', fontsize=10)
            ax.tick_params(colors='#8b949e', labelsize=9)
            ax.set_title(f"Brute-force results — best match: shift {top['shift']}",
                         color='#e6edf3', fontsize=11, pad=10)
            for spine in ax.spines.values():
                spine.set_edgecolor('#30363d')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

            with st.expander("📋 View all 25 attempts"):
                for r in results:
                    tag   = "✓ BEST" if r['likely'] else f"shift {r['shift']:2d}"
                    color = "#00e5a0" if r['likely'] else "#8b949e"
                    preview = r['text'][:100] + ('...' if len(r['text']) > 100 else '')
                    # Label row in HTML (no user text)
                    st.markdown(f"""
                    <div style="display:flex; gap:16px; padding:6px 0 2px;
                                border-bottom:1px solid #1c2128;
                                font-family:'Space Mono',monospace; font-size:12px;">
                        <span style="color:{color}; min-width:68px;">{tag}</span>
                        <span style="color:#555; min-width:80px;">score {r['score']:.1f}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    # Text rendered safely by Streamlit
                    st.text(preview)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — Frequency Analysis
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <p style="color:#8b949e; font-size:14px; margin-bottom:20px;">
        Compare the letter frequency distribution of any text against standard English.
        Encrypted text shows a flat or shifted pattern — the tell-tale sign
        of a simple substitution cipher.
    </p>
    """, unsafe_allow_html=True)

    fa_col1, fa_col2 = st.columns([1, 1], gap="large")

    with fa_col1:
        fa_text = st.text_area(
            "Text to analyse:",
            placeholder="Paste any text (plain or encrypted) here...",
            height=200, key="fa_text"
        )
        analyse_btn = st.button("📊 Run Frequency Analysis", use_container_width=True)

    with fa_col2:
        if analyse_btn:
            if not fa_text.strip():
                st.warning("Please enter some text first.")
            else:
                freq    = letter_frequency(fa_text)
                letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                x       = np.arange(26)

                fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
                fig.patch.set_facecolor('#0d1117')
                for ax in axes:
                    ax.set_facecolor('#161b22')
                    for spine in ax.spines.values():
                        spine.set_edgecolor('#30363d')
                    ax.tick_params(colors='#8b949e', labelsize=8)

                axes[0].bar(x, [freq[l] for l in letters],
                            color='#58a6ff', alpha=0.85, width=0.7)
                axes[0].set_title("Your text — letter frequency (%)",
                                  color='#e6edf3', fontsize=11, pad=8)
                axes[0].set_ylabel("%", color='#8b949e', fontsize=9)

                axes[1].bar(x, [ENGLISH_FREQ[l] for l in letters],
                            color='#00e5a0', alpha=0.75, width=0.7)
                axes[1].set_title("Standard English frequency (%)",
                                  color='#e6edf3', fontsize=11, pad=8)
                axes[1].set_ylabel("%", color='#8b949e', fontsize=9)
                axes[1].set_xticks(x)
                axes[1].set_xticklabels(letters, fontsize=8, color='#8b949e')

                plt.tight_layout(pad=2.0)
                st.pyplot(fig)
                plt.close()

                top5 = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:5]
                badges = "".join(
                    f'<span style="background:#0d2b1a; border:1px solid #00e5a0;'
                    f'border-radius:5px; padding:4px 12px; color:#00e5a0;'
                    f'font-size:14px; font-family:\'Space Mono\',monospace;">'
                    f'{l}: {v:.1f}%</span>'
                    for l, v in top5
                )
                st.markdown(f"""
                <div style="background:#161b22; border:1px solid #30363d;
                            border-radius:8px; padding:14px 16px; margin-top:14px;">
                    <p style="font-size:11px; color:#8b949e;
                              font-family:'Space Mono',monospace;
                              letter-spacing:2px; margin:0 0 10px;">
                        TOP 5 LETTERS IN YOUR TEXT
                    </p>
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">{badges}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background:#161b22; border:1px dashed #30363d;
                        border-radius:8px; padding:60px 20px; text-align:center;">
                <div style="font-size:40px; opacity:0.25;">📊</div>
                <div style="color:#30363d; font-family:'Space Mono',monospace;
                             font-size:12px; margin-top:12px;">
                    Charts appear here after analysis
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#161b22; border:1px solid #30363d;
                border-radius:10px; padding:20px 24px;">
        <p style="font-family:'Space Mono',monospace; font-size:11px; color:#58a6ff;
                  letter-spacing:2px; margin:0 0 14px;">WHY THIS BREAKS CAESAR CIPHER</p>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;">
            <div style="padding:14px; background:#0d1117; border-radius:8px;
                        border:1px solid #30363d;">
                <div style="font-size:18px; margin-bottom:8px;">📌</div>
                <div style="color:#e6edf3; font-size:13px; font-weight:500; margin-bottom:6px;">Pattern preserved</div>
                <div style="color:#8b949e; font-size:12px; line-height:1.6;">
                    Caesar shifts letters but keeps the same relative frequency
                    distribution — just rotated.
                </div>
            </div>
            <div style="padding:14px; background:#0d1117; border-radius:8px;
                        border:1px solid #30363d;">
                <div style="font-size:18px; margin-bottom:8px;">🔎</div>
                <div style="color:#e6edf3; font-size:13px; font-weight:500; margin-bottom:6px;">E is most common</div>
                <div style="color:#8b949e; font-size:12px; line-height:1.6;">
                    In English, 'E' appears ~12.7% of the time. The most frequent
                    ciphertext letter is the encrypted 'E'.
                </div>
            </div>
            <div style="padding:14px; background:#0d1117; border-radius:8px;
                        border:1px solid #30363d;">
                <div style="font-size:18px; margin-bottom:8px;">💥</div>
                <div style="color:#e6edf3; font-size:13px; font-weight:500; margin-bottom:6px;">Only 25 keys</div>
                <div style="color:#8b949e; font-size:12px; line-height:1.6;">
                    The entire key space is cracked in milliseconds — no frequency
                    analysis even required.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding-bottom:2rem;">
    <div style="color:#21262d; font-family:'Space Mono',monospace;
                font-size:11px; letter-spacing:2px;">
        SKILLCRAFT TECHNOLOGY &nbsp;·&nbsp; CYBERSECURITY INTERNSHIP &nbsp;·&nbsp; TASK 01
    </div>
    <div style="color:#21262d; font-size:11px; margin-top:4px;">
        Caesar Cipher · Educational · Non-malicious
    </div>
</div>
""", unsafe_allow_html=True)