from rich import print
from app.config import MONOLOGUE_PROMPT
from app.utils.llm import generate_inference_json


def generate_monologue(topic: str) -> dict:
    return generate_inference_json(
        query=topic, sysprompt=MONOLOGUE_PROMPT, required_prop="result"
    )["result"]
