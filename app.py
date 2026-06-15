import streamlit as st
from src.config import MODELOS_DISPONIBLES, PLATAFORMAS
from src.generators.content_generator import generar_contenido
# v2 - Groq

# ── Configuración de página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="MultiversoApp",
    page_icon="🌐",
    layout="centered",
)

# ── Estilos ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%); }
    h1 { background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
         -webkit-background-clip: text; -webkit-text-fill-color: transparent;
         font-size: 2.8rem !important; font-weight: 700 !important; }
    .tagline { color: #94a3b8; font-size: 1rem; margin-top: -10px; margin-bottom: 20px; }
    .resultado-box {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(167,139,250,0.3);
        border-radius: 12px;
        padding: 24px;
        margin-top: 16px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #7c3aed, #2563eb);
        color: white; border: none; border-radius: 8px;
        font-weight: 600; font-size: 1rem;
        transition: opacity 0.2s;
    }
    .stButton > button:hover { opacity: 0.85; }
</style>
""", unsafe_allow_html=True)

# ── Cabecera ──────────────────────────────────────────────────────────────────
st.markdown("<h1>🌐 MultiversoApp</h1>", unsafe_allow_html=True)
st.markdown('<p class="tagline">Genera contenido listo para publicar en cualquier plataforma e idioma — impulsado por Groq + LangChain</p>', unsafe_allow_html=True)
st.divider()

# ── Formulario ────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    plataforma = st.selectbox(
        "📢 Plataforma",
        options=list(PLATAFORMAS.keys()),
        help="Elige dónde quieres publicar",
    )
with col2:
    modelo = st.selectbox(
        "🤖 Modelo de IA",
        options=list(MODELOS_DISPONIBLES.keys()),
    )

col3, col4 = st.columns(2)
with col3:
    audiencia = st.text_input(
        "👥 Audiencia objetivo",
        placeholder="Ej: jóvenes emprendedores, padres, estudiantes…",
    )
with col4:
    idioma = st.selectbox(
        "🌍 Idioma",
        options=["Español", "English", "Français", "Italiano"],
    )

tema = st.text_area(
    "💡 Tema / Idea",
    placeholder="Describe sobre qué quieres escribir…",
    height=110,
)

tono_sugerido = PLATAFORMAS[plataforma]["tono_sugerido"]
tono = st.text_input(
    "🎨 Tono",
    value=tono_sugerido,
    help="Se sugiere automáticamente según la plataforma, pero puedes cambiarlo",
)

# ── Generar ───────────────────────────────────────────────────────────────────
st.divider()
generar = st.button("✨ Generar contenido", type="primary", use_container_width=True)

if generar:
    if not tema.strip():
        st.warning("Por favor, introduce un tema.")
    elif not audiencia.strip():
        st.warning("Por favor, especifica la audiencia objetivo.")
    else:
        with st.spinner(f"Generando contenido para {plataforma}…"):
            try:
                resultado = generar_contenido(
                    tema=tema,
                    plataforma=plataforma,
                    audiencia=audiencia,
                    tono=tono,
                    nombre_modelo=modelo,
                    idioma=idioma,
                )
                st.success("¡Contenido generado!")
                st.markdown(f'<div class="resultado-box">{resultado}</div>', unsafe_allow_html=True)
                st.divider()
                st.download_button(
                    label="⬇️ Descargar como .txt",
                    data=resultado,
                    file_name=f"multiverso_{plataforma.lower().replace('/', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            except ValueError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"Error inesperado: {e}")
