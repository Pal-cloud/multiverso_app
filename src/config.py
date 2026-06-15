from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

MODELOS_DISPONIBLES = {
    "Llama 3.3 70B": "llama-3.3-70b-versatile",
    "Llama 3.1 8B":  "llama-3.1-8b-instant",
    "Gemma 2 9B":    "gemma2-9b-it",
}

PLATAFORMAS = {
    "Blog": {
        "tono_sugerido": "informativo y cercano",
        "formato":  "post completo con titulo, introduccion, 3 secciones con subtitulos y conclusion",
        "longitud": "600-900 palabras",
    },
    "Twitter/X": {
        "tono_sugerido": "directo y conversacional",
        "formato":  "hilo de 5 tweets numerados (1/5 - 5/5), cada uno de menos de 280 caracteres",
        "longitud": "muy corta",
    },
    "Instagram": {
        "tono_sugerido": "visual, inspirador y emocional",
        "formato":  "caption con frase gancho, mensaje principal, llamada a la accion y 10 hashtags",
        "longitud": "150-250 palabras",
    },
    "LinkedIn": {
        "tono_sugerido": "profesional y reflexivo",
        "formato":  "post con apertura impactante, 3-4 parrafos cortos y pregunta final",
        "longitud": "200-350 palabras",
    },
}


def obtener_modelo(nombre_modelo: str) -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY no encontrada. Revisa tu archivo .env.")
    modelo_real = MODELOS_DISPONIBLES.get(nombre_modelo)
    if not modelo_real:
        raise ValueError(f"Modelo '{nombre_modelo}' no reconocido.")
    return ChatGroq(model=modelo_real, api_key=api_key)
