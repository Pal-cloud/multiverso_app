# 🌐 MultiversoApp — Generador de Contenido con IA

> Convierte cualquier idea en contenido listo para publicar en cualquier plataforma e idioma, impulsado por **Gemini AI** y **LangChain**.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-orange?logo=google)
![License](https://img.shields.io/badge/Licencia-MIT-lightgrey)

---

## 🧠 ¿Qué es MultiversoApp?

MultiversoApp es una prueba de concepto (PoC) de generación automática de contenido creada para **Digital Content**. A partir de un tema, audiencia, tono e idioma, genera contenido listo para publicar adaptado al estilo y formato de cuatro plataformas:

| Plataforma | Estilo de salida |
|---|---|
| 📝 Blog | Post completo con título, secciones y conclusión (600–900 palabras) |
| 🐦 Twitter/X | Hilo de 5 tweets numerados (≤ 280 caracteres cada uno) |
| 📸 Instagram | Caption con gancho, cuerpo, CTA y 10 hashtags |
| 💼 LinkedIn | Post profesional con apertura impactante y pregunta de engagement |

---

## ✨ Funcionalidades

- 🤖 **Selector de modelo**: Gemini 1.5 Flash o Gemini 2.0 Flash (ambos en tier gratuito)
- 🌍 **Multiidioma**: Español, English, Français, Italiano
- 🎨 **Tono personalizable**: sugerido automáticamente por plataforma y editable
- ⬇️ **Descarga del contenido** generado en `.txt`
- 🧩 **Arquitectura modular** con separación de responsabilidades en `src/`

---

## 🗂️ Estructura del proyecto

```
multiverso_app/
├── app.py                          # Interfaz web con Streamlit
├── src/
│   ├── __init__.py
│   ├── config.py                   # Modelos disponibles y configuración de plataformas
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── content_prompt.py       # PromptTemplate de LangChain
│   └── generators/
│       ├── __init__.py
│       └── content_generator.py    # Cadena LCEL: prompt | LLM | parser
├── requirements.txt
├── .env.example
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
```

### 3. Activar el entorno virtual
```bash
source venv/Scripts/activate   # Windows (Git Bash)
venv\Scripts\activate          # Windows (CMD/PowerShell)
source venv/bin/activate       # macOS/Linux
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar la API key

Copia `.env.example` a `.env` y añade tu clave de Gemini:
```bash
cp .env.example .env
```
```env
GEMINI_API_KEY=tu_clave_aqui
```
> Obtén una clave gratuita en [Google AI Studio](https://aistudio.google.com/app/apikey)

### 6. Ejecutar la aplicación
```bash
# Con el venv activado:
python -m streamlit run app.py
```

La app se abrirá automáticamente en `http://localhost:8501`

---

## 🔧 ¿Cómo funciona?

1. El usuario rellena el formulario: **plataforma**, **modelo**, **audiencia**, **idioma**, **tono** y **tema**.
2. `app.py` llama a `generar_contenido()` en `src/generators/content_generator.py`.
3. El generador construye la cadena LCEL: `PromptTemplate | ChatGoogleGenerativeAI | StrOutputParser`.
4. El prompt se envía al modelo Gemini elegido con todas las variables inyectadas.
5. El contenido generado se muestra en pantalla y se puede descargar como `.txt`.

```
Formulario ──► content_generator.py ──► PromptTemplate ──► Gemini API ──► Contenido listo
```

---

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|---|---|
| Lenguaje | Python 3.13 |
| Framework LLM | LangChain 0.3 (LCEL) |
| Modelos LLM | Gemini 1.5 Flash / Gemini 2.0 Flash (tier gratuito) |
| Frontend | Streamlit 1.58 |
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
- [x] Selector de modelo de IA
- [x] Generación en varios idiomas (ES, EN, FR, IT)
- [x] Tono personalizable por el usuario
- [x] Interfaz web (Streamlit) en español
- [x] Código documentado y arquitectura modular
- [x] README en GitHub
- [x] Repositorio Git con ramas organizadas y commits descriptivos
- [ ] Artículo en Medium

---

## 📄 Licencia

MIT

