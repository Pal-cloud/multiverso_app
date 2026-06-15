from langchain_core.prompts import ChatPromptTemplate

plantilla_contenido = ChatPromptTemplate.from_messages([
    (
        "system",
        "Eres un experto en marketing de contenidos y copywriting digital. "
        "Generas contenido auténtico, atractivo y optimizado para cada plataforma.",
    ),
    (
        "human",
        """Crea contenido para {plataforma} sobre el tema: {tema}

Audiencia objetivo : {audiencia}
Tono               : {tono}
Formato requerido  : {formato}
Longitud esperada  : {longitud}
Idioma             : {idioma}

Sigue exactamente el formato indicado y adapta el tono a la plataforma.
Responde SOLO con el contenido listo para publicar, sin explicaciones adicionales.""",
    ),
])
