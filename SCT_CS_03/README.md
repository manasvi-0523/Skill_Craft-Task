# ⌨️ Typing Behavior Research Tool

[![React](https://img.shields.io/badge/React-19.2+-61DAFB?logo=react)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-8.0+-646CFF?logo=vite)](https://vitejs.dev/)
[![Recharts](https://img.shields.io/badge/Recharts-3.8+-8884d8)](https://recharts.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **SkillCraft Technology Cybersecurity Internship - Task 03**

A privacy-focused, client-side web application that analyzes typing behavior patterns including WPM (Words Per Minute), accuracy, keystroke timing, and key frequency. All data processing happens locally in your browser—zero network requests.

![Typing Behavior Research](https://img.shields.io/badge/Status-Production-success)

## 🌟 Features

### 📊 Real-Time Metrics
- **WPM Tracking**: Live words-per-minute calculation
- **Accuracy Score**: Backspace rate vs total keystrokes
- **Key Interval**: Average time between keystrokes (milliseconds)
- **Live Key Stream**: Visual feed of typed keys with color coding

### 🔥 Advanced Analytics
- **Keyboard Heatmap**: Visual representation of most-used keys
- **Frequency Analysis**: Bar chart of top 8 most-pressed keys
- **WPM Timeline**: Line graph showing typing speed over time
- **Speed Classification**: Beginner → Intermediate → Advanced → Professional

### 🔒 Privacy-First Design
- ✅ **100% Client-Side**: All processing in browser
- ✅ **Zero Network Requests**: No data transmission
- ✅ **Local Storage Only**: Data stays in memory
- ✅ **Export Control**: JSON export on user request only
- ✅ **No Tracking**: No analytics, cookies, or third-party scripts

### 📈 Data Export
Export comprehensive JSON reports including:
- Session duration and timestamp
- Total keystrokes and backspace count
- Accuracy percentage
- Average WPM and key intervals
- Complete key frequency map
- WPM timeline data

## 🚀 Quick Start

### Prerequisites
```bash
Node.js 18+ and npm/yarn
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/manasvi-0523/SCT_CS_03.git
cd SCT_CS_03
```

2. **Install dependencies**
```bash
npm install
# or
yarn install
```

3. **Start development server**
```bash
npm run dev
# or
yarn dev
```

4. **Open your browser**
```
Visit: http://localhost:5173
```

### Production Build

```bash
npm run build
npm run preview
```

## 📖 Usage Guide

### Starting a Session

1. Click **"Start Session"** button
2. Type naturally in the text area
3. Watch real-time metrics update
4. Click **"Stop & Review"** when finished

### Understanding Metrics

#### WPM (Words Per Minute)
- **Beginner**: < 30 WPM
- **Intermediate**: 30-60 WPM
- **Advanced**: 60-90 WPM
- **Professional**: > 90 WPM

#### Accuracy
- **Excellent**: 95-100%
- **Good**: 80-94%
- **Needs Improvement**: < 80%

#### Key Interval
- Average time between keystrokes
- Lower = faster typing
- Typical range: 100-300ms

### Exporting Data

Click **"Export JSON"** to download a comprehensive report:

```json
{
  "timestamp": "2026-05-16T10:30:00.000Z",
  "session_duration_s": 120,
  "total_keystrokes": 450,
  "backspaces": 23,
  "accuracy_pct": 95,
  "avg_wpm": 65,
  "avg_key_interval_ms": 185,
  "key_frequency": {
    "E": 45,
    "T": 38,
    "A": 35,
    ...
  },
  "wpm_timeline": [
    { "t": 3, "wpm": 58 },
    { "t": 6, "wpm": 62 },
    ...
  ]
}
```

## 🏗️ Project Structure

```
SCT_CS_03/
├── src/
│   ├── App.jsx                      # Main app component
│   ├── TypingBehaviorResearch.jsx   # Core typing analysis component
│   ├── App.css                      # Global styles
│   ├── index.css                    # Base styles
│   ├── main.jsx                     # React entry point
│   └── assets/                      # Images and icons
├── public/
│   ├── favicon.svg                  # App icon
│   └── icons.svg                    # Icon sprites
├── index.html                       # HTML template
├── vite.config.js                   # Vite configuration
├── eslint.config.js                 # ESLint rules
├── package.json                     # Dependencies
└── README.md                        # Documentation
```

## 🛠️ Technical Details

### Technologies Used

- **React 19.2**: Modern UI framework with hooks
- **Vite 8.0**: Lightning-fast build tool
- **Recharts 3.8**: Data visualization library
- **Pure JavaScript**: No TypeScript overhead
- **CSS-in-JS**: Inline styles for component isolation

### Key Features Implementation

#### Real-Time WPM Calculation
```javascript
function calcWPM(chars, ms) {
  if (ms < 1000) return 0;
  return Math.round((chars / 5) / (ms / 60000));
}
```

#### Keyboard Heatmap
- 3-row QWERTY layout visualization
- Color-coded by frequency (low → mid → high)
- Real-time updates during typing

#### Key Interval Tracking
- Measures time between consecutive keystrokes
- Filters outliers (> 2 seconds)
- Calculates average for session

### Performance Optimizations

- **useCallback**: Memoized event handlers
- **useRef**: Direct DOM access without re-renders
- **Efficient State Updates**: Batched updates for metrics
- **Sliding Window**: Last 50 keys/intervals stored
- **Throttled Updates**: WPM calculated every 3 seconds

## 🎨 Design System

### Color Palette
```css
--bg:      #0d1117  /* Dark background */
--surface: #161b22  /* Card background */
--border:  #21262d  /* Subtle borders */
--text:    #e6edf3  /* Primary text */
--muted:   #7d8590  /* Secondary text */
--accent:  #58a6ff  /* Blue accent */
--ok:      #3fb950  /* Success green */
--warn:    #d29922  /* Warning yellow */
--danger:  #f85149  /* Error red */
```

### Typography
- **Sans-serif**: system-ui, -apple-system
- **Monospace**: 'Courier New', monospace

## 📊 Use Cases

### Research Applications
- **Biometric Authentication**: Keystroke dynamics analysis
- **User Behavior Studies**: Typing pattern research
- **Ergonomics Research**: Keyboard usage patterns
- **Educational Tools**: Typing skill assessment

### Personal Use
- **Skill Tracking**: Monitor typing improvement over time
- **Habit Analysis**: Identify most-used keys
- **Speed Training**: Track WPM progress
- **Accuracy Goals**: Reduce backspace rate

## 🔐 Privacy & Security

### What We DON'T Collect
- ❌ Actual text content
- ❌ Personal information
- ❌ IP addresses
- ❌ Browser fingerprints
- ❌ Usage analytics

### What We DO Track (Locally)
- ✅ Key types (letter, space, backspace, enter)
- ✅ Timing intervals between keys
- ✅ Key frequency counts
- ✅ WPM calculations

### Data Handling
- All data stored in browser memory (React state)
- Cleared on page refresh
- Export only on explicit user action
- No cookies or localStorage used

## 🤝 Contributing

Contributions are welcome! Ideas for enhancement:

- [ ] Add typing test mode with sample texts
- [ ] Implement typing games for practice
- [ ] Add multi-session comparison
- [ ] Support for different keyboard layouts
- [ ] Dark/light theme toggle
- [ ] Mobile touch typing support

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Manasvi**
- GitHub: [@manasvi-0523](https://github.com/manasvi-0523)
- Project: SkillCraft Technology Cybersecurity Internship

## 🙏 Acknowledgments

- SkillCraft Technology for the internship opportunity
- React and Vite communities for excellent tooling
- Recharts for beautiful data visualization

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

<div align="center">
  <strong>⌨️ Understanding typing behavior, one keystroke at a time</strong>
</div>
