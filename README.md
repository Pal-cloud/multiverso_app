# ✒️ MultiversoApp — Generador de Contenido con IA

> Convierte cualquier idea en contenido listo para publicar en segundos, impulsado por **Gemini AI** y **LangChain**.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-1.3-green)
![Gemini](https://img.shields.io/badge/Gemini-1.5_Flash-orange?logo=google)

---

## 🧠 ¿Qué es MultiversoApp?

MultiversoApp es una prueba de concepto (PoC) de generación automática de contenido creada para **Digital Content**. A partir de un tema y una audiencia objetivo, genera contenido listo para publicar adaptado al estilo y formato de cuatro plataformas:

| Plataforma | Estilo de salida |
|---|---|
| 📝 Blog | Post completo con título, secciones y conclusión |
| 🐦 Twitter/X | Hilo de 5 tweets (≤ 280 caracteres cada uno) |
| 📸 Instagram | Caption con gancho, cuerpo, CTA y hashtags |
| 💼 LinkedIn | Post profesional con apertura impactante y pregunta de engagement |

---

## 🗂️ Estructura del proyecto

```
multiverso_app/
├── app.py            # Interfaz web con Streamlit
├── generator.py      # Lógica LangChain + Gemini y plantillas de prompts
├── requirements.txt  # Dependencias Python
├── .env.example      # Plantilla de variables de entorno
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/Pal-cloud/multiverso_app.git
cd multiverso_app
```

### 2. Crear un entorno virtual con Python 3.13
```bash
py -3.13 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la API key

Copia `.env.example` a `.env` y añade tu clave de Gemini:
```bash
cp .env.example .env
```
```env
GEMINI_API_KEY=tu_clave_aqui
```
> Obtén una clave gratuita en [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Ejecutar la aplicación
```bash
# Activa el entorno virtual primero:
source venv/Scripts/activate   # Windows (Git Bash)
venv\Scripts\activate          # Windows (CMD/PowerShell)
source venv/bin/activate       # macOS/Linux

# Luego ejecuta:
streamlit run app.py
```

La app se abrirá automáticamente en `http://localhost:8501`

---

## 🔧 ¿Cómo funciona?

1. El usuario selecciona una **plataforma**, escribe un **tema** y define la **audiencia objetivo**.
2. `generator.py` construye un prompt usando un **`PromptTemplate` de LangChain**, inyectando instrucciones específicas de cada plataforma (tono, formato, longitud).
3. El prompt se envía a **Gemini 1.5 Flash** a través de `langchain-google-genai`.
4. El contenido generado se muestra en pantalla y se puede descargar como `.txt`.

```
Entrada del usuario ──► PromptTemplate ──► Gemini 1.5 Flash ──► Contenido listo para publicar
```

---

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|---|---|
| Lenguaje | Python 3.13 |
| Framework LLM | LangChain (LCEL) |
| Modelo LLM | Google Gemini 1.5 Flash (tier gratuito) |
| Frontend | Streamlit |
| Configuración | python-dotenv |

---

## 🌿 Ramas del repositorio

| Rama | Propósito |
|---|---|
| `main` | Código estable y revisado |
| `develop` | Integración de nuevas funcionalidades |
| `streamlit` | Desarrollo de la interfaz web y corrección de dependencias |

---

## 📋 Checklist de entrega (Nivel Esencial)

- [x] Generación de contenido de texto para múltiples plataformas y audiencias
- [x] Prompt Engineering con plantillas específicas por plataforma
- [x] Interfaz web (Streamlit) en español
- [x] Código documentado
- [x] README en GitHub
- [x] Repositorio Git con ramas organizadas y commits descriptivos
- [ ] Artículo en Medium

---

## 📄 Licencia

MIT
