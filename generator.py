from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# --- Platform configurations ---
PLATFORM_CONFIG = {
    "Blog": {
        "tone": "informative and engaging",
        "format": "a full blog post with a title, introduction, 3 sections with subheadings, and a conclusion",
        "length": "600–900 words",
    },
    "Twitter/X": {
        "tone": "punchy, direct and conversational",
        "format": "a thread of 5 tweets, each under 280 characters, numbered 1/5 to 5/5",
        "length": "very short",
    },
    "Instagram": {
        "tone": "visual, inspiring and emotional",
        "format": "a caption with a hook sentence, the main message, a call to action, and 10 relevant hashtags",
        "length": "150–250 words",
    },
    "LinkedIn": {
        "tone": "professional, thoughtful and insightful",
        "format": "a post with a strong opening line, 3–4 short paragraphs, and a closing question to drive engagement",
        "length": "200–350 words",
    },
}

PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["platform", "topic", "audience", "tone", "format", "length"],
    template="""
You are PixelPen, an expert content creator specialized in social media and digital marketing.

Generate content for **{platform}** about the following topic:

Topic: {topic}
Target Audience: {audience}

Instructions:
- Tone: {tone}
- Format: {format}
- Approximate length: {length}
- Write ONLY the final content, ready to publish. No meta-commentary or explanations.

Go ahead:
""",
)


def get_llm():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        model_name="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.7,
    )



def generate_content(platform: str, topic: str, audience: str) -> str:
    config = PLATFORM_CONFIG[platform]
    llm = get_llm()
    chain = PROMPT_TEMPLATE | llm | StrOutputParser()
    return chain.invoke(
        {
            "platform": platform,
            "topic": topic,
            "audience": audience,
            "tone": config["tone"],
            "format": config["format"],
            "length": config["length"],
        }
    )
