from app.config import IMAGEGEN_PROMPT
from app.utils.llm import generate_inference_json


def generate_artprompt_from_monologue(topic: str) -> str:
    return generate_inference_json(
        query=topic, sysprompt=IMAGEGEN_PROMPT, required_prop="prompt"
    )["prompt"]
