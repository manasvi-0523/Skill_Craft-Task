# Typing Behavior Research Tool

**SkillCraft Technology Cybersecurity Internship | Task 03**

A browser-based tool that records and analyzes typing behavior: words per minute, accuracy, keystroke timing intervals, and key frequency. All processing happens in the browser. No data is sent anywhere.

---

## Features

**During a session**
- Live WPM counter updated every 3 seconds
- Accuracy percentage based on backspace rate vs total keystrokes
- Average key interval in milliseconds
- Color-coded live key stream showing each keystroke type

**After stopping**
- Session summary with final WPM, accuracy, keystroke count, and key interval
- Speed classification: Beginner (below 30), Intermediate (30-60), Advanced (60-90), Professional (above 90)
- WPM timeline chart (SVG line graph, no library needed)
- Keyboard heatmap showing which keys were used most
- Bar chart of the top 8 most-pressed keys
- JSON export with full session data

**Privacy**
- Zero network requests
- No cookies, no localStorage, no analytics
- Data lives only in React state and is cleared on page refresh

---

## Setup

Requirements: Node.js 18 or higher.

```bash
git clone https://github.com/manasvi-0523/Skill_Craft-Task.git
cd Skill_Craft-Task/SCT_CS_03
npm install
npm run dev
```

Open `http://localhost:5173`.

**Production build:**

```bash
npm run build
```

Output goes to `SCT_CS_03/dist/`. Verified build size: 202 kB JS, 63 kB gzipped.

---

## Exported JSON format

```json
{
  "timestamp": "2026-05-16T10:30:00.000Z",
  "session_duration_s": 120,
  "total_keystrokes": 450,
  "backspaces": 23,
  "accuracy_pct": 95,
  "avg_wpm": 65,
  "avg_key_interval_ms": 185,
  "key_frequency": { "E": 45, "T": 38 },
  "wpm_timeline": [
    { "t": 3, "wpm": 58 },
    { "t": 6, "wpm": 62 }
  ]
}
```

---

## Project structure

```
SCT_CS_03/
    src/
        App.jsx                     entry component
        TypingBehaviorResearch.jsx  all session logic and UI
        index.css
        App.css
        main.jsx
    public/
    index.html
    vite.config.js
    package.json
    README.md
```

---

## Build verification

```
vite v8.0.12 building for production
17 modules transformed
dist/assets/index.js    202.47 kB | gzip: 63.99 kB
built in 471ms
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| react | 19.2 | UI framework |
| react-dom | 19.2 | DOM rendering |
| recharts | 3.8 | data charts |
| vite | 8.0 | build tool |

---

## Author

Manasvi | [@manasvi-0523](https://github.com/manasvi-0523)
