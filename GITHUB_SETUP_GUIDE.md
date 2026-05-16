# 📘 GitHub Setup Guide — Single Repo

> Push everything to **one** repository: `Skill_Craft-Task`

---

## Step 1 — Create the repository on GitHub

1. Go to **https://github.com/new**
2. Fill in:
   - **Repository name:** `Skill_Craft-Task`
   - **Description:** `🔐 SkillCraft Technology Cybersecurity Internship — Caesar Cipher, Password Checker, Typing Behavior Research, Image Encryption`
   - **Visibility:** Public
3. **Do NOT** tick "Add a README file" (we already have one)
4. Click **Create repository**

---

## Step 2 — Configure Git (one-time)

```bash
git config --global user.name "Manasvi"
git config --global user.email "your-email@example.com"
```

---

## Step 3 — Push from your local folder

Open a terminal, navigate to the `skill_craft` folder, and run:

```bash
cd "C:\Users\Lenovo\Desktop\skill_craft"

git init
git add .
git commit -m "Initial commit: SkillCraft Cybersecurity Internship — all 4 tasks"
git remote add origin https://github.com/manasvi-0523/Skill_Craft-Task.git
git branch -M main
git push -u origin main
```

That's it. All four task folders (`SCT_CS_01` through `SCT_CS_04`) plus the root `README.md` will be pushed together.

---

## Step 4 — Polish the repo on GitHub

### Add topics
Go to the repo page → click the ⚙️ gear next to **About** → add:

```
cybersecurity  python  react  streamlit  tkinter  cryptography
password-security  keystroke-dynamics  image-encryption  internship
```

### Pin it to your profile
Go to your GitHub profile → **Customize your pins** → select `Skill_Craft-Task`.

---

## Step 5 — Add a LICENSE (optional but recommended)

On GitHub: **Add file → Create new file** → name it `LICENSE` → click **Choose a license template** → select **MIT** → commit.

---

## Everyday Git workflow

```bash
# After making changes
git add .
git commit -m "Short description of what changed"
git push
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `remote origin already exists` | `git remote set-url origin https://github.com/manasvi-0523/Skill_Craft-Task.git` |
| `failed to push — rejected` | `git pull origin main --rebase` then `git push` |
| `Permission denied (publickey)` | Use HTTPS URL (above) or add an SSH key in GitHub Settings |

---

## What the repo will look like

```
Skill_Craft-Task/
├── SCT_CS_01/          # Caesar Cipher Tool
├── SCT_CS_02/          # Password Strength Checker
├── SCT_CS_03/          # Typing Behavior Research
├── SCT_CS_04/          # Image Encryption Tool
└── README.md
```

Each subfolder has its own `README.md` with full documentation for that task.
