# 🌐 MultiversoApp — Generador de Contenido con IA

> Convierte cualquier idea en contenido listo para publicar en segundos, impulsado por **Groq + LangChain**.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)
![React](https://img.shields.io/badge/React-18-61dafb?logo=react)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.42-red?logo=streamlit)

## 🚀 Demos en vivo

| Versión | Tecnología | Enlace |
|---------|-----------|--------|
| **v1 — Streamlit** | Python + Streamlit | [multiversoapp-pgs.streamlit.app](https://multiversoapp-pgs.streamlit.app/) |
| **v2 — React + FastAPI** | React + MUI + FastAPI + Groq | [multiverso-q1czvt74o-pals-projects-afd1b7ce.vercel.app](https://multiverso-q1czvt74o-pals-projects-afd1b7ce.vercel.app/) |

---

## 🧠 ¿Qué es MultiversoApp?

MultiversoApp es un generador de contenido con IA que, dado un tema y una audiencia objetivo, produce texto listo para publicar adaptado al estilo y formato de cuatro plataformas:

| Plataforma | Formato de salida |
|-----------|------------------|
| 📝 Blog | Post completo con título, secciones y conclusión |
| 🐦 Twitter/X | Hilo de 5 tweets (≤ 280 caracteres cada uno) |
| 📸 Instagram | Caption con gancho, cuerpo, CTA y hashtags |
| 💼 LinkedIn | Post profesional con apertura impactante y pregunta final |

---

## 🗂️ Ramas del proyecto

Este repositorio documenta una **migración progresiva** de una app Streamlit a una arquitectura moderna con React + FastAPI:

| Rama | Descripción |
|------|-------------|
| `feature/streamlit` | v1 — App completa en Streamlit + Groq. Desplegada en Streamlit Cloud |
| `feature/react` | v2 — Frontend React + MUI + SweetAlert2 con backend FastAPI serverless. Desplegada en Vercel |
| `main` | Documentación general y punto de entrada del proyecto |

---

## 🏗️ Cómo lo conseguimos — El proceso de migración

### v1: Streamlit + Gemini → Streamlit + Groq
El punto de partida fue una app Streamlit que usaba **Gemini 1.5 Flash** como LLM. El primer paso fue **migrar el proveedor LLM a Groq** (Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B), aprovechando la capa gratuita de Groq y su velocidad de inferencia. La lógica se refactorizó en módulos bajo `src/`:

```
src/
├── config.py                    # Modelos y configuración por plataforma
├── prompts/content_prompt.py    # Plantilla de prompt con LangChain
└── generators/content_generator.py  # Cadena LCEL: prompt | llm | parser
```

### v2: React + FastAPI + Vercel
Para la segunda versión se separaron completamente frontend y backend:

- **Backend**: `api/index.py` — FastAPI expuesto como función serverless en Vercel, reutilizando toda la lógica Python de `src/`
- **Frontend**: `frontend/` — React 18 con Material UI para el diseño, SweetAlert2 para notificaciones y Axios para las llamadas a la API
- **Despliegue**: todo en una sola plataforma (Vercel) gracias al `vercel.json` que enruta `/generar` al Python serverless y el resto al build estático de React

```
User (React UI)
     │
     ▼  POST /generar
FastAPI serverless (Vercel)
     │
     ▼
LangChain LCEL chain
     │
     ▼
Groq API (Llama 3.3 70B)
     │
     ▼
Contenido listo para publicar
```

---

## 🗂️ Estructura del proyecto

```
multiverso_app/
├── api/
│   └── index.py              # Backend FastAPI (serverless Vercel)
├── frontend/
│   ├── src/
│   │   ├── App.js            # UI React + MUI + SweetAlert2
│   │   └── index.js
│   └── package.json
├── src/
│   ├── config.py             # Modelos Groq + config por plataforma
│   ├── prompts/
│   │   └── content_prompt.py # Plantilla LangChain
│   └── generators/
│       └── content_generator.py  # Lógica LCEL
├── app.py                    # App Streamlit (rama feature/streamlit)
├── vercel.json               # Config despliegue Vercel
├── Procfile                  # Config Railway/Render (alternativa)
├── docker-compose.yml        # Orquestación Docker (opcional)
├── requirements.txt
└── .env.example
```

---

## ⚙️ Ejecución local

### Prerrequisitos
- Python 3.11+
- Node.js 18+
- API key de [Groq](https://console.groq.com) (gratuita)

### 1. Clonar y configurar entorno

```bash
git clone https://github.com/Pal-cloud/multiverso_app.git
cd multiverso_app
git checkout feature/react   # para la versión React
# o
git checkout feature/streamlit  # para la versión Streamlit

python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
cp .env.example .env
# Edita .env y añade tu GROQ_API_KEY
```

### 2a. Correr versión Streamlit

```bash
git checkout feature/streamlit
streamlit run app.py
# Abre http://localhost:8501
```

### 2b. Correr versión React + FastAPI

```bash
git checkout feature/react

# Terminal 1 — Backend
uvicorn api.index:app --port 8000 --reload

# Terminal 2 — Frontend
cd frontend && npm install && npm start
# Abre http://localhost:3000
```

---

## 🛠️ Stack tecnológico

| Capa | v1 Streamlit | v2 React + FastAPI |
|------|-------------|-------------------|
| LLM | Groq (Llama 3.3 70B) | Groq (Llama 3.3 70B) |
| LLM Framework | LangChain LCEL | LangChain LCEL |
| Backend | Streamlit | FastAPI (serverless) |
| Frontend | Streamlit | React 18 + MUI + SweetAlert2 |
| Despliegue | Streamlit Cloud | Vercel |
| Contenedores | — | Docker Compose (opcional) |

---

## 📋 Checklist del proyecto

- [x] Generación de contenido para múltiples plataformas y audiencias
- [x] Prompt Engineering con plantillas específicas por plataforma
- [x] Interfaz Streamlit (v1) — desplegada en Streamlit Cloud
- [x] Migración de Gemini a Groq
- [x] Refactorización modular en `src/`
- [x] Backend FastAPI con endpoint `/generar`
- [x] Frontend React con MUI y SweetAlert2 (v2)
- [x] Despliegue en Vercel (frontend + backend serverless)
- [x] Docker Compose para despliegue local contenedorizado
- [x] Ramas Git organizadas (`feature/streamlit`, `feature/react`)
- [x] README documentado
- [x] [Artículo en Medium](https://medium.com/p/2c30d555f49d/)

---

## 📄 Licencia

MIT
