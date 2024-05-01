import ollama
import json
from rich import print
from app.config import OLLAMA_MODEL

MAX_INFERENCE_RETRIES = 15  # realistically we'll never need THIS many


def generate_inference(query: str, sysprompt: str) -> str:
    resp = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": query},
        ],
        options={
            "temperature": 1.0,
        },
    )

    return resp.get("message").get("content")


def generate_inference_json(*, query: str, sysprompt: str, required_prop=None) -> dict:
    response_object = None
    fail = True

    # Since LLMs are rebels that don't always follow instructions properly,
    # we'll try several times to get a valid response. It usually gets it right
    # the first time, but we can't rely on that.

    for _ in range(MAX_INFERENCE_RETRIES):
        try:
            json_resp = generate_inference(query, sysprompt)

            response_object = json.loads(json_resp)

            if required_prop and required_prop not in response_object:
                raise ValueError(
                    f"[yellow]Response object does not contain required property:[/yellow] {required_prop}"
                )
            fail = False
        except Exception as e:
            print("\n[yellow]Failed to parse JSON response. Retrying...[/yellow]\n")
        else:
            break

    if fail:
        # critical failure
        raise ValueError(
            "[red]LLM failed to generate response after repeated tries.[/red]"
        )

    return response_object
