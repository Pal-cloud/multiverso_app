import streamlit as st
from generator import generate_content, PLATFORM_CONFIG

# --- Page config ---
st.set_page_config(
    page_title="PixelPen ✒️",
    page_icon="✒️",
    layout="centered",
)

# --- Header ---
st.title("✒️ PixelPen")
st.caption("Turn any idea into platform-ready content — powered by Gemini AI")
st.divider()

# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    platform = st.selectbox(
        "📢 Platform",
        options=list(PLATFORM_CONFIG.keys()),
        help="Choose where you want to publish",
    )

with col2:
    audience = st.text_input(
        "👥 Target Audience",
        placeholder="e.g. tech enthusiasts, parents, students…",
    )

topic = st.text_area(
    "💡 Topic / Idea",
    placeholder="Describe what you want to write about…",
    height=120,
)

# --- Generate button ---
st.divider()
generate_btn = st.button("✨ Generate Content", type="primary", use_container_width=True)

# --- Output ---
if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic before generating.")
    elif not audience.strip():
        st.warning("Please specify a target audience.")
    else:
        with st.spinner("PixelPen is writing your content…"):
            try:
                content = generate_content(platform, topic, audience)
                st.success("Content ready!")
                st.divider()
                st.subheader(f"📄 Your {platform} content")
                st.markdown(content)
                st.divider()
                st.download_button(
                    label="⬇️ Download as .txt",
                    data=content,
                    file_name=f"pixelpen_{platform.lower().replace('/', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            except ValueError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"Something went wrong: {e}")
