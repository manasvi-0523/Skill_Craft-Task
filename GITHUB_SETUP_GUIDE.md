# 📘 GitHub Reference — Skill_Craft-Task

> Repo is live at **https://github.com/manasvi-0523/Skill_Craft-Task**

---

## ✅ What's already done

| Step | Status |
|------|--------|
| Repo created on GitHub | ✅ |
| All 4 task folders pushed | ✅ |
| Root `README.md` (portfolio overview) | ✅ |
| Per-task `README.md` files | ✅ |
| `.gitignore` (excludes `__pycache__`, `node_modules`, `output/`) | ✅ |
| `.gitattributes` (line-ending normalization) | ✅ |
| `LICENSE` (MIT 2026) | ✅ |

---

## 🏷️ Recommended: add topics on GitHub

Go to **https://github.com/manasvi-0523/Skill_Craft-Task** → click the ⚙️ gear next to **About** → add:

```
cybersecurity  python  react  streamlit  tkinter
cryptography  password-security  keystroke-dynamics
image-encryption  internship  skillcraft
```

---

## 🔄 Everyday workflow

```bash
# After editing any file
git add .
git commit -m "Brief description of what changed"
git push
```

---

## 🗂️ Repo structure (for reference)

```
Skill_Craft-Task/
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md               ← portfolio overview
├── GITHUB_SETUP_GUIDE.md   ← this file
│
├── SCT_CS_01/              ← 🔐 Caesar Cipher (Python + Streamlit)
│   ├── app.py
│   ├── caesar.py
│   ├── requirements.txt
│   └── README.md
│
├── SCT_CS_02/              ← 🛡️ Password Checker (Python + HTML/JS)
│   ├── password_strength_checker.py
│   ├── index.html
│   └── README.md
│
├── SCT_CS_03/              ← ⌨️ Typing Behavior (React + Vite)
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
└── SCT_CS_04/              ← 🖼️ Image Encryption (Python + Tkinter)
    ├── app.py
    ├── encrypt.py
    ├── decrypt.py
    ├── gui.py
    ├── utils.py
    ├── requirements.txt
    └── README.md
```

---

## 🚀 Optional: deploy the web projects

| Task | Platform | Command / Steps |
|------|----------|-----------------|
| SCT_CS_01 (Streamlit) | [Streamlit Cloud](https://streamlit.io/cloud) | Connect repo → set main file to `SCT_CS_01/app.py` → Deploy |
| SCT_CS_02 (HTML) | GitHub Pages | Repo Settings → Pages → select `main` branch → `/SCT_CS_02` folder |
| SCT_CS_03 (React) | [Vercel](https://vercel.com) | Import repo → Root Directory: `SCT_CS_03` → Build: `npm run build` → Output: `dist` |

---

## 🆘 Troubleshooting

| Problem | Fix |
|---------|-----|
| `remote origin already exists` | `git remote set-url origin https://github.com/manasvi-0523/Skill_Craft-Task.git` |
| `failed to push — rejected` | `git pull origin main --rebase` then `git push` |
| Nested `.git` warning again | `Remove-Item -Recurse -Force <subfolder>\.git` then `git add .` |
