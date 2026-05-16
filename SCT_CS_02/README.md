# 🛡️ Password Strength Checker

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)](https://www.javascript.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **SkillCraft Technology Cybersecurity Internship - Task 02**

A comprehensive password strength assessment tool with both CLI (Python) and web-based (HTML/JS) interfaces. Evaluates passwords against 7 security criteria and provides actionable feedback.

![Password Strength Checker](https://img.shields.io/badge/Status-Production-success)

## 🌟 Features

### 🔍 Multi-Criteria Analysis
- **Length Check**: Minimum 8, recommended 12+, excellent 16+ characters
- **Character Variety**: Uppercase, lowercase, numbers, special characters
- **Pattern Detection**: Identifies sequential characters, repeated patterns, common words
- **Real-time Scoring**: 0-100% strength rating with color-coded feedback
- **Visual Feedback**: Progress bars, heatmaps, and interactive UI

### 💻 Dual Interface
- **Python CLI**: Terminal-based tool with detailed reports
- **Web App**: Modern, responsive HTML/CSS/JS interface with live validation

### 📊 Detailed Reporting
- ✅ Passed checks with green indicators
- ❌ Failed checks with specific recommendations
- 📈 Percentage score and strength classification
- 💡 Actionable improvement suggestions

## 🚀 Quick Start

### Python CLI Version

#### Prerequisites
```bash
Python 3.8 or higher
```

#### Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/manasvi-0523/SCT_CS_02.git
cd SCT_CS_02
```

2. **Run the CLI tool**
```bash
python password_strength_checker.py
```

3. **Enter passwords to test**
```
> MyP@ssw0rd123
```

### Web Version

1. **Open the HTML file**
```bash
# Simply open index.html in any modern browser
# Or use a local server:
python -m http.server 8000
# Then visit: http://localhost:8000
```

2. **Start typing**
   - Real-time feedback as you type
   - Visual strength meter
   - Instant recommendations

## 📖 Usage Examples

### Python CLI

```python
from password_strength_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker()
result = checker.assess_password("MyP@ssw0rd123")

print(f"Strength: {result['strength']}")
print(f"Score: {result['score']}/{result['max_score']}")
print(f"Percentage: {result['percentage']}%")
```

**Output:**
```
═══════════════════════════════════════════════════════════
PASSWORD STRENGTH ASSESSMENT
═══════════════════════════════════════════════════════════

Password: *************
Strength: 🟢 Strong
Score: 15/18 (83.3%)
[████████████████████████████████░░░░░░░░] 83.3%

────────────────────────────────────────────────────────────
DETAILED FEEDBACK
────────────────────────────────────────────────────────────

✓ Passed Checks:
  ✓ Length: Good length (13 characters)
  ✓ Uppercase: Contains 2 uppercase letters
  ✓ Lowercase: Contains 7 lowercase letters
  ✓ Numbers: Contains 3 numbers
  ✓ Special Characters: Contains 2 special characters
  ✓ Pattern Check: No common weak patterns
  ✓ Character Variety: Excellent variety (all character types)

═══════════════════════════════════════════════════════════
```

### Web Interface

The web version provides:
- **Live typing feedback** with instant strength updates
- **Visual criteria grid** showing pass/fail status
- **Interactive strength bar** with color transitions
- **Detailed recommendations** panel
- **Password visibility toggle**

## 🏗️ Project Structure

```
SCT_CS_02/
├── password_strength_checker.py   # Python CLI implementation
├── index.html                      # Web-based interface
├── .gitignore                      # Git ignore rules
└── README.md                       # Project documentation
```

## 🔒 Security Criteria

### 1. Length (Max 3 points)
- ❌ < 8 characters: Too short
- ⚠️ 8-11 characters: Acceptable
- ✅ 12-15 characters: Good
- 🌟 16+ characters: Excellent

### 2. Uppercase Letters (Max 2 points)
- ❌ None: 0 points
- ⚠️ 1 letter: 1 point
- ✅ 2+ letters: 2 points

### 3. Lowercase Letters (Max 2 points)
- ❌ None: 0 points
- ⚠️ 1 letter: 1 point
- ✅ 2+ letters: 2 points

### 4. Numbers (Max 2 points)
- ❌ None: 0 points
- ⚠️ 1 number: 1 point
- ✅ 2+ numbers: 2 points

### 5. Special Characters (Max 2 points)
- ❌ None: 0 points
- ⚠️ 1 character: 1 point
- ✅ 2+ characters: 2 points

### 6. Pattern Detection (Max 2 points)
- ❌ Weak patterns detected: 0 points
- ✅ No weak patterns: 2 points

Detects:
- Sequential letters (abc, xyz)
- Sequential numbers (123, 789)
- Repeated characters (aaa, 111)
- Common words (password, admin, qwerty)

### 7. Character Variety (Max 3 points)
- ❌ 1 type: 0 points
- ⚠️ 2 types: 1 point
- ✅ 3 types: 2 points
- 🌟 All 4 types: 3 points

## 📊 Strength Classification

| Score | Strength | Color | Description |
|-------|----------|-------|-------------|
| 90-100% | Very Strong | 🟢 Green | Excellent password |
| 70-89% | Strong | 🟢 Green | Good password |
| 50-69% | Moderate | 🟡 Yellow | Acceptable but improvable |
| 30-49% | Weak | 🟠 Orange | Needs improvement |
| 0-29% | Very Weak | 🔴 Red | Highly vulnerable |

## 🛠️ Technical Details

### Python Implementation
- **Object-Oriented Design**: Clean, maintainable `PasswordStrengthChecker` class
- **Type Hints**: Full type annotations for better code quality
- **Comprehensive Testing**: Handles edge cases and empty inputs
- **Extensible**: Easy to add new criteria or modify scoring

### Web Implementation
- **Pure JavaScript**: No external dependencies
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Validation**: Instant feedback as user types
- **Accessibility**: ARIA labels and semantic HTML
- **Modern CSS**: Flexbox, Grid, custom properties

## 🎨 Design Philosophy

- **User-Friendly**: Clear, actionable feedback
- **Educational**: Explains why passwords are weak
- **Visual**: Color-coded indicators and progress bars
- **Fast**: Real-time analysis with no lag
- **Secure**: All processing is client-side (web) or local (CLI)

## 🔐 Best Practices Promoted

✅ **DO:**
- Use 12+ characters (16+ is excellent)
- Mix all 4 character types
- Use unique passwords for each account
- Consider using a password manager
- Enable two-factor authentication

❌ **DON'T:**
- Use dictionary words
- Use personal information (birthdays, names)
- Reuse passwords across sites
- Use sequential or repeated characters
- Share passwords

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- [ ] Add dictionary attack simulation
- [ ] Implement entropy calculation
- [ ] Add password generation feature
- [ ] Support for multiple languages
- [ ] Integration with Have I Been Pwned API

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Manasvi**
- GitHub: [@manasvi-0523](https://github.com/manasvi-0523)
- Project: SkillCraft Technology Cybersecurity Internship

## 🙏 Acknowledgments

- NIST password guidelines
- OWASP security best practices
- SkillCraft Technology for the internship opportunity

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

<div align="center">
  <strong>🔒 Building stronger passwords, one check at a time</strong>
</div>
