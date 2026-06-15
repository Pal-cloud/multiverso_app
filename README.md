# MultiversoApp — Generador de Contenido con IA

> Convierte cualquier idea en contenido listo para publicar en cualquier plataforma e idioma, impulsado por **Groq** y **LangChain**.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-orange)
![License](https://img.shields.io/badge/Licencia-MIT-lightgrey)

---

## Que es MultiversoApp

MultiversoApp es una prueba de concepto (PoC) de generación automática de contenido creada para **Digital Content**. A partir de un tema, audiencia, tono e idioma, genera contenido listo para publicar adaptado al estilo y formato de cuatro plataformas:

| Plataforma | Estilo de salida |
|---|---|
| Blog | Post completo con título, secciones y conclusión (600-900 palabras) |
| Twitter/X | Hilo de 5 tweets numerados (menos de 280 caracteres cada uno) |
| Instagram | Caption con gancho, cuerpo, CTA y 10 hashtags |
| LinkedIn | Post profesional con apertura impactante y pregunta de engagement |

---

## Funcionalidades

- Selector de modelo: Llama 3.3 70B, Llama 3.1 8B o Gemma 2 9B (todos gratuitos via Groq)
- Multiidioma: Español, English, Français, Italiano
- Tono personalizable: sugerido automáticamente por plataforma y editable
- Descarga del contenido generado en .txt
- Arquitectura modular con separación de responsabilidades en src/

---

## Estructura del proyecto

```
multiverso_app/
├── app.py                          # Interfaz web con Streamlit
├── src/
│   ├── __init__.py
│   ├── config.py                   # Modelos disponibles y configuracion de plataformas
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

## Instalacion y ejecucion

### 1. Clonar el repositorio

Descarga el proyecto en tu máquina local:

```bash
git clone https://github.com/Pal-cloud/multiverso_app.git
cd multiverso_app
```

### 2. Crear el entorno virtual con Python 3.13

Es obligatorio usar Python 3.13. Crea un entorno virtual aislado para que
las dependencias no interfieran con otros proyectos:

```bash
py -3.13 -m venv venv
```

Esto genera una carpeta `venv/` en el directorio del proyecto con su propio
intérprete de Python.

### 3. Activar el entorno virtual

Activa el entorno antes de instalar nada ni ejecutar la app.
Si no lo activas, Python usará los paquetes del sistema y la app fallará:

```bash
source venv/Scripts/activate   # Windows (Git Bash)  <-- recomendado
venv\Scripts\activate          # Windows (CMD / PowerShell)
source venv/bin/activate       # macOS / Linux
```

Sabrás que está activo porque el prompt del terminal mostrará `(venv)` al inicio.

### 4. Instalar dependencias

Con el entorno virtual activo, instala todas las librerías necesarias:

```bash
pip install -r requirements.txt
```

Esto instalará: Streamlit, LangChain, langchain-groq y python-dotenv.
La instalación puede tardar 1-2 minutos la primera vez.

### 5. Configurar la API key de Groq

La app necesita una clave de Groq para acceder a los modelos LLM.
Es gratuita y se obtiene en menos de un minuto:

1. Ve a https://console.groq.com/keys
2. Crea una cuenta o inicia sesión
3. Pulsa "Create API Key" y copia la clave (empieza por `gsk_`)
4. Crea el archivo `.env` en la raíz del proyecto:

```bash
cp .env.example .env
```

5. Abre el `.env` y sustituye el valor:

```env
GROQ_API_KEY=gsk_tu_clave_aqui
```

El archivo `.env` está en `.gitignore`: nunca se sube a GitHub.

### 6. Ejecutar la aplicacion

Importante: usa siempre el ejecutable de Python del venv, no el del sistema,
para evitar conflictos con otros proyectos Streamlit que puedan estar corriendo:

```bash
venv/Scripts/python.exe -m streamlit run app.py --server.port 8503
```

La app se abrirá automáticamente en el navegador en:

```
http://localhost:8503
```

Si el puerto 8503 estuviese ocupado, cambia el número por cualquier otro libre
(8504, 8505, etc.).

---

## Como funciona

1. El usuario rellena el formulario: plataforma, modelo, audiencia, idioma, tono y tema.
2. `app.py` llama a `generar_contenido()` en `src/generators/content_generator.py`.
3. El generador construye la cadena LCEL: `PromptTemplate | ChatGroq | StrOutputParser`.
4. El prompt se envia al modelo Groq elegido con todas las variables inyectadas.
5. El contenido generado se muestra en pantalla y se puede descargar como `.txt`.

```
Formulario -> content_generator.py -> PromptTemplate -> Groq API -> Contenido listo
```

---

## Stack tecnologico

| Capa | Tecnologia |
|---|---|
| Lenguaje | Python 3.13 |
| Framework LLM | LangChain 0.3 (LCEL) |
| Modelos LLM | Llama 3.3 70B / Llama 3.1 8B / Gemma 2 9B (Groq, tier gratuito) |
| Frontend | Streamlit 1.58 |
| Configuracion | python-dotenv |

---

## Ramas del repositorio

| Rama | Proposito |
|---|---|
| `main` | Codigo estable y revisado |
| `develop` | Integracion de nuevas funcionalidades |
| `feature/streamlit` | Desarrollo de la interfaz web y correccion de dependencias |

---

## Checklist de entrega (Nivel Esencial)

- [x] Generacion de contenido de texto para multiples plataformas y audiencias
- [x] Prompt Engineering con plantillas especificas por plataforma
- [x] Selector de modelo de IA (3 modelos disponibles)
- [x] Generacion en varios idiomas (ES, EN, FR, IT)
- [x] Tono personalizable por el usuario
- [x] Interfaz web (Streamlit) en español
- [x] Codigo documentado y arquitectura modular
- [x] README en GitHub
- [x] Repositorio Git con ramas organizadas y commits descriptivos
- [x] Articulo en Medium: https://medium.com/p/2c30d555f49d

