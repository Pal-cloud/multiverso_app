from langchain_core.output_parsers import StrOutputParser
from src.prompts.content_prompt import plantilla_contenido
from src.config import obtener_modelo, PLATAFORMAS
from dotenv import load_dotenv

load_dotenv()


def generar_contenido(
    tema: str,
    plataforma: str,
    audiencia: str,
    tono: str,
    nombre_modelo: str,
    idioma: str,
) -> str:
    """Genera contenido listo para publicar usando Gemini + LangChain LCEL."""
    config = PLATAFORMAS[plataforma]
    llm = obtener_modelo(nombre_modelo)
    chain = plantilla_contenido | llm | StrOutputParser()
    return chain.invoke(
        {
            "tema": tema,
            "plataforma": plataforma,
            "audiencia": audiencia,
            "tono": tono,
            "formato": config["formato"],
            "longitud": config["longitud"],
            "idioma": idioma,
        }
    )
