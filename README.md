# ✒️ PixelPen — AI Content Generator

> Turn any idea into platform-ready content in seconds, powered by **Gemini AI** and **LangChain**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.2-green)
![Gemini](https://img.shields.io/badge/Gemini-1.5_Flash-orange?logo=google)

---

## 🧠 What is PixelPen?

PixelPen is a proof-of-concept content generation system built for **Digital Content**. Given a topic and a target audience, it automatically generates publication-ready content tailored to the style and format of four major platforms:

| Platform | Output style |
|---|---|
| 📝 Blog | Full post with title, sections and conclusion |
| 🐦 Twitter/X | Thread of 5 tweets (≤ 280 chars each) |
| 📸 Instagram | Caption with hook, body, CTA and hashtags |
| 💼 LinkedIn | Professional post with opening hook and engagement question |

---

## 🗂️ Project Structure

```
pixelpen/
├── app.py            # Streamlit web interface
├── generator.py      # LangChain + Gemini logic & prompt templates
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pixelpen.git
cd pixelpen
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Copy `.env.example` to `.env` and add your Gemini API key:
```bash
cp .env.example .env
```
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
> Get a free API key at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 🔧 How it works

1. The user selects a **platform**, enters a **topic** and a **target audience**.
2. `generator.py` builds a prompt using a **LangChain `PromptTemplate`**, injecting platform-specific instructions (tone, format, length).
3. The prompt is sent to **Gemini 1.5 Flash** via `langchain-google-genai`.
4. The generated content is displayed in the UI and can be downloaded as a `.txt` file.

```
User Input ──► PromptTemplate ──► Gemini 1.5 Flash ──► Ready-to-publish content
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM Framework | LangChain |
| LLM Model | Google Gemini 1.5 Flash (free tier) |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## 📋 Delivery Checklist (Nivel Esencial)

- [x] Text content generation for multiple platforms and audiences
- [x] Prompt Engineering with platform-specific templates
- [x] Web interface (Streamlit)
- [x] Documented code
- [x] README
- [ ] Git repository with clean branches and commits
- [ ] Medium article

---

## 📄 License

MIT
