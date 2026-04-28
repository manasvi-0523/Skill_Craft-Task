# SecureText Studio

**SkillCraft Technology Cybersecurity Internship | Task 01**

A Streamlit web app for Caesar cipher encryption and decryption. Includes a brute-force attack simulator and letter frequency analysis to demonstrate why simple substitution ciphers are cryptographically weak.

---

## Features

**Encrypt / Decrypt tab**
- Shift value selector from 1 to 25
- Interactive cipher wheel that rotates to show the substitution mapping
- Output statistics: character count, letter count, symbol count
- Cipher alphabet map rendered below the output

**Brute-Force Attack tab**
- Tries all 25 possible shifts automatically
- Scores each candidate using English letter frequency (chi-squared) plus a common-word bonus
- Displays confidence percentage and a horizontal bar chart of all 25 scores

**Frequency Analysis tab**
- Plots letter frequency of any input text against the standard English baseline
- Useful for visually confirming whether text is encrypted or plaintext

---

## Setup

Requirements: Python 3.8 or higher.

```bash
git clone https://github.com/manasvi-0523/Skill_Craft-Task.git
cd Skill_Craft-Task
pip install -r SCT_CS_01/requirements.txt
streamlit run SCT_CS_01/app.py
```

The app opens at `http://localhost:8501`.

---

## Project structure

```
SCT_CS_01/
    app.py              main Streamlit application
    caesar.py           cipher logic, brute-force, frequency analysis
    requirements.txt    Python dependencies
    README.md
```

---

## How the scoring works

The brute-force ranker uses a hybrid score:

```
score = freq_score + word_match_bonus
```

`freq_score` is the negative chi-squared distance between the candidate's letter distribution and standard English frequencies. `word_match_bonus` adds 300 points per matched common English word. The shift with the highest score is marked as the most likely plaintext.

---

## Security note

The Caesar cipher has a key space of only 25. It is broken trivially by brute force or frequency analysis. This project exists to illustrate that weakness, not to provide real encryption. For actual data protection use AES-256 or similar.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| streamlit | web UI framework |
| matplotlib | frequency and brute-force charts |
| numpy | numerical operations |

---

## Author

Manasvi | [@manasvi-0523](https://github.com/manasvi-0523)
