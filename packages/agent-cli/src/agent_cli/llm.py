import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"), base_url=os.getenv("ANTHROPIC_BASE_URL")
)

MODEL = os.getenv("ANTHROPIC_MODEL", "glm-4.7")
