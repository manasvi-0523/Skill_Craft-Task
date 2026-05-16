# 🔐 Skill_Craft-Task — Cybersecurity Internship Portfolio

[![GitHub](https://img.shields.io/badge/GitHub-manasvi--0523-181717?logo=github)](https://github.com/manasvi-0523)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-19.2+-61DAFB?logo=react)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **All four cybersecurity tasks from the SkillCraft Technology Internship — in one place.**

This monorepo contains four production-ready projects covering classical cryptography, password security, behavioral analysis, and image encryption. Each task lives in its own subfolder with its own README and dependencies.

---

## 📁 Repository Structure

```
Skill_Craft-Task/
├── SCT_CS_01/          # 🔐 Caesar Cipher Tool (Python + Streamlit)
├── SCT_CS_02/          # 🛡️ Password Strength Checker (Python + HTML/JS)
├── SCT_CS_03/          # ⌨️ Typing Behavior Research (React + Vite)
├── SCT_CS_04/          # 🖼️ Image Encryption Tool (Python + Tkinter)
└── README.md           # This file
```

---

## 📚 Projects

### 🔐 Task 01 — SecureText Studio (Caesar Cipher)
**Path:** [`SCT_CS_01/`](./SCT_CS_01)

Modern Caesar Cipher implementation with cryptanalysis features.

| | |
|---|---|
| **Stack** | Python, Streamlit, Matplotlib, NumPy |
| **Run** | `streamlit run SCT_CS_01/app.py` |

**Highlights:**
- Encrypt/Decrypt with shift values 1–25
- Interactive drag-to-rotate cipher wheel
- Brute-force attack simulation with confidence scoring
- Letter frequency analysis vs. standard English

---

### 🛡️ Task 02 — Password Strength Checker
**Path:** [`SCT_CS_02/`](./SCT_CS_02)

Dual-interface password assessment tool — CLI and web.

| | |
|---|---|
| **Stack** | Python, HTML5, CSS3, Vanilla JavaScript |
| **Run (CLI)** | `python SCT_CS_02/password_strength_checker.py` |
| **Run (Web)** | Open `SCT_CS_02/index.html` in a browser |

**Highlights:**
- 7-criteria analysis: length, case, numbers, symbols, patterns, variety
- Real-time web UI with animated strength bar
- Actionable recommendations panel
- Zero dependencies for the web version

---

### ⌨️ Task 03 — Typing Behavior Research Tool
**Path:** [`SCT_CS_03/`](./SCT_CS_03)

Privacy-first keystroke dynamics analyzer — nothing leaves your browser.

| | |
|---|---|
| **Stack** | React 19, Vite 8, Recharts |
| **Run** | `cd SCT_CS_03 && npm install && npm run dev` |

**Highlights:**
- Live WPM, accuracy, and key-interval tracking
- Keyboard heatmap and WPM timeline chart
- Speed classification (Beginner → Professional)
- JSON export — all processing is 100% client-side

---

### 🖼️ Task 04 — PixelCrypt (Image Encryption)
**Path:** [`SCT_CS_04/`](./SCT_CS_04)

Multi-layer image encryption with a modern desktop GUI.

| | |
|---|---|
| **Stack** | Python, Tkinter, Pillow, NumPy |
| **Run** | `python SCT_CS_04/app.py` |

**Highlights:**
- Triple-layer encryption: XOR cipher → RGB channel shift → pixel shuffle
- Side-by-side live preview (Original / Encrypted / Decrypted)
- Password-based key derivation, lossless round-trip
- Save encrypted/decrypted images to `SCT_CS_04/output/`

---

## 🚀 Getting Started

### Clone the repo
```bash
git clone https://github.com/manasvi-0523/Skill_Craft-Task.git
cd Skill_Craft-Task
```

### Python projects (Tasks 01, 02, 04)
```bash
# Install dependencies for each task
pip install -r SCT_CS_01/requirements.txt
pip install -r SCT_CS_04/requirements.txt

# Task 02 web version has no dependencies — just open the HTML file
```

### React project (Task 03)
```bash
cd SCT_CS_03
npm install
npm run dev
```

---

## 🛠️ Tech Stack

| Language | Projects |
|----------|----------|
| Python | Task 01, 02, 04 |
| JavaScript (React) | Task 03 |
| HTML / CSS | Task 02, 03 |

| Library / Framework | Used In |
|---------------------|---------|
| Streamlit | Task 01 |
| Matplotlib, NumPy | Task 01, 04 |
| Pillow (PIL) | Task 04 |
| Tkinter | Task 04 |
| React + Vite | Task 03 |
| Recharts | Task 03 |

---

## 📊 Stats

| Task | Lines of Code | Status |
|------|--------------|--------|
| SCT_CS_01 | ~800 | ✅ Complete |
| SCT_CS_02 | ~1,200 | ✅ Complete |
| SCT_CS_03 | ~600 | ✅ Complete |
| SCT_CS_04 | ~500 | ✅ Complete |
| **Total** | **~3,100** | **✅ Complete** |

---

## 🎓 Concepts Covered

- Classical cryptography & cryptanalysis
- Password security (OWASP guidelines)
- Behavioral biometrics / keystroke dynamics
- Symmetric image encryption (XOR, RGB shift, pixel shuffle)
- Privacy-preserving client-side analytics
- GUI development (Tkinter, Streamlit, React)

---

## 👤 Author

**Manasvi**
- GitHub: [@manasvi-0523](https://github.com/manasvi-0523)

---

## 🙏 Acknowledgments

SkillCraft Technology for the internship opportunity and project briefs.

---

## 📝 License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <strong>🔐 Built during the SkillCraft Technology Cybersecurity Internship</strong>
</div>
