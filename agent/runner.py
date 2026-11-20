import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from .tools import calculate_expression, get_project_note

load_dotenv()

MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
SYSTEM_INSTRUCTION = (
    "You are a concise, helpful personal AI agent. "
    "Use your available tools whenever math or saved project notes are needed. "
    "Be clear and direct."
)

AVAILABLE_TOOLS = [calculate_expression, get_project_note]


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in environment or .env")
    return genai.Client(api_key=api_key)


def run_agent(message: str) -> str:
    client = get_client()
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=message,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            tools=AVAILABLE_TOOLS,
            temperature=0.2,
        ),
    )
    return response.text or ""
