from langchain_core.prompts import PromptTemplate

plantilla_contenido = PromptTemplate(
    input_variables=["tema", "plataforma", "audiencia", "tono", "formato", "longitud", "idioma"],
    template="""Eres MultiversoApp, un asistente experto en creación de contenido digital para redes sociales y medios digitales.

Genera contenido sobre el siguiente tema:

- Tema: {tema}
- Plataforma: {plataforma}
- Audiencia objetivo: {audiencia}
- Tono: {tono}
- Idioma: {idioma}

Instrucciones de formato:
- Formato esperado: {formato}
- Longitud aproximada: {longitud}

Genera ÚNICAMENTE el contenido final, listo para publicar. Sin explicaciones, sin comentarios adicionales.
""",
)
