# Password Strength Checker

**SkillCraft Technology Cybersecurity Internship | Task 02**

A password assessment tool available in two forms: a Python CLI and a standalone HTML/JS web page. Both evaluate the same seven security criteria and return a strength rating with specific feedback.

---

## Features

Seven criteria are checked on every password:

| Criterion | Max points | What is checked |
|-----------|-----------|-----------------|
| Length | 3 | below 8 fails, 12+ is good, 16+ is excellent |
| Uppercase letters | 2 | presence and count |
| Lowercase letters | 2 | presence and count |
| Numbers | 2 | presence and count |
| Special characters | 2 | presence and count |
| Pattern check | 2 | sequential chars, repeated chars, common words |
| Character variety | 3 | how many of the four types are present |

Score is converted to a percentage. Thresholds: Very Weak below 30, Weak 30-49, Moderate 50-69, Strong 70-89, Very Strong 90 and above.

---

## Setup

**CLI version** (Python 3.8+):

```bash
git clone https://github.com/manasvi-0523/Skill_Craft-Task.git
cd Skill_Craft-Task
python SCT_CS_02/password_strength_checker.py
```

**Web version** (no dependencies):

Open `SCT_CS_02/index.html` directly in any modern browser. All logic runs in the browser with no server required.

---

## CLI usage

```
python SCT_CS_02/password_strength_checker.py

Enter a password to check (or 'quit' to exit):
> MyP@ssw0rd12

PASSWORD STRENGTH ASSESSMENT
Score: 14/16 (87.5%)
Strength: Strong
```

---

## Using the module in your own code

```python
from SCT_CS_02.password_strength_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker()
result = checker.assess_password('MyP@ssw0rd12')

print(result['strength'])     # Strong
print(result['percentage'])   # 87.5
print(result['passed_checks'])
print(result['failed_checks'])

recs = checker.get_recommendations(result)
for r in recs:
    print(r)
```

---

## Project structure

```
SCT_CS_02/
    password_strength_checker.py    CLI tool and importable module
    index.html                      self-contained web interface
    README.md
```

---

## Test results

Verified against these cases:

| Password | Expected | Result |
|----------|---------|--------|
| `abc` | Very Weak | Very Weak (12.5%) |
| `password123` | Weak | Weak (37.5%) |
| `MyP@ssw0rd12` | Strong | Strong (87.5%) |
| `X9#mK2@pLqR7!vNz` | Very Strong | Very Strong (100%) |
| `` (empty) | Invalid | Invalid |

---

## Author

Manasvi | [@manasvi-0523](https://github.com/manasvi-0523)
