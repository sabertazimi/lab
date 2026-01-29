import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

WORKDIR = Path.cwd()
MODEL = os.getenv("ANTHROPIC_MODEL", "glm-4.7")

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"), base_url=os.getenv("ANTHROPIC_BASE_URL")
)
