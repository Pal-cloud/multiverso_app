import streamlit as st
from generator import generate_content, PLATFORM_CONFIG

# --- Configuración de página ---
st.set_page_config(
    page_title="MultiversoApp 🌐",
    page_icon="🌐",
    layout="centered",
)

# --- Cabecera ---
st.title("🌐 MultiversoApp")
st.caption("Convierte cualquier idea en contenido listo para publicar — impulsado por Gemini AI")
st.divider()

# --- Entradas ---
col1, col2 = st.columns(2)

with col1:
    platform = st.selectbox(
        "📢 Plataforma",
        options=list(PLATFORM_CONFIG.keys()),
        help="Elige dónde quieres publicar el contenido",
    )

with col2:
    audience = st.text_input(
        "👥 Audiencia objetivo",
        placeholder="Ej: jóvenes emprendedores, padres, estudiantes…",
    )

topic = st.text_area(
    "💡 Tema / Idea",
    placeholder="Describe sobre qué quieres escribir…",
    height=120,
)

# --- Botón de generación ---
st.divider()
generate_btn = st.button("✨ Generar contenido", type="primary", use_container_width=True)

# --- Resultado ---
if generate_btn:
    if not topic.strip():
        st.warning("Por favor, introduce un tema antes de generar.")
    elif not audience.strip():
        st.warning("Por favor, especifica la audiencia objetivo.")
    else:
        with st.spinner("MultiversoApp está escribiendo tu contenido…"):
            try:
                content = generate_content(platform, topic, audience)
                st.success("¡Contenido listo!")
                st.divider()
                st.subheader(f"📄 Tu contenido para {platform}")
                st.markdown(content)
                st.divider()
                st.download_button(
                    label="⬇️ Descargar como .txt",
                    data=content,
                    file_name=f"multiversoapp_{platform.lower().replace('/', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            except ValueError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"Algo salió mal: {e}")
