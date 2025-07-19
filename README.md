# 📚 BookForge Pro

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**AI-powered book writer using Google Gemini API and ElevenLabs for audiobook generation. Includes GUI, CLI and Docker support.**

---

## 🚀 Features
- Generate full-length books using Google Gemini
- Automatic research and chapter writing
- Export to **PDF**, **EPUB**, and **Markdown**
- Optional audiobook generation with ElevenLabs
- GUI built with **Streamlit**
- CLI mode for automation
- Build as standalone **EXE / macOS App**
- Docker support

---

## 🖼 Preview
![BookForge Pro GUI](docs/screenshot.png)
*(Replace this with an actual screenshot from your GUI later)*

---

## 📦 Installation

### 1. Clone Repo
```bash
git clone https://github.com/Fr0stByt3s-21/bookforge-pro.git
cd bookforge-pro
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
export GEMINI_API_KEY=your_gemini_key
export ELEVENLABS_API_KEY=your_elevenlabs_key
```

### 4. Run GUI
```bash
python gui_app.py
```

### 5. Run CLI
```bash
python cli_app.py --topic "My Book" --words 30000 --export pdf,epub --audiobook yes
```

### 6. Docker
```bash
docker build -t bookforge-pro .
docker run -p 8501:8501 bookforge-pro
```

### 7. GitHub Actions Build
Tag a commit with `vX.Y.Z` to trigger the cross-platform build workflow.
