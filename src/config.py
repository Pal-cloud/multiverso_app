from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Modelos disponibles de Gemini (tier gratuito)
MODELOS_DISPONIBLES = {
    "Gemini 1.5 Flash": "gemini-1.5-flash-latest",
    "Gemini 2.0 Flash": "gemini-2.0-flash",
}

# Configuración por plataforma
PLATAFORMAS = {
    "Blog": {
        "tono_sugerido": "informativo y cercano",
        "formato": "post completo con título, introducción, 3 secciones con subtítulos y conclusión",
        "longitud": "600–900 palabras",
    },
    "Twitter/X": {
        "tono_sugerido": "directo y conversacional",
        "formato": "hilo de 5 tweets numerados (1/5 … 5/5), cada uno de menos de 280 caracteres",
        "longitud": "muy corta",
    },
    "Instagram": {
        "tono_sugerido": "visual, inspirador y emocional",
        "formato": "caption con frase gancho, mensaje principal, llamada a la acción y 10 hashtags relevantes",
        "longitud": "150–250 palabras",
    },
    "LinkedIn": {
        "tono_sugerido": "profesional y reflexivo",
        "formato": "post con apertura impactante, 3–4 párrafos cortos y pregunta final para fomentar debate",
        "longitud": "200–350 palabras",
    },
}


def obtener_modelo(nombre_modelo: str) -> ChatGoogleGenerativeAI:
    """Devuelve una instancia del LLM de Gemini."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY no encontrada. Revisa tu archivo .env.")
    modelo_real = MODELOS_DISPONIBLES[nombre_modelo]
    return ChatGoogleGenerativeAI(
        model=modelo_real,
        google_api_key=api_key,
        temperature=0.7,
    )
