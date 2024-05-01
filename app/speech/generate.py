import os
from rich import print

from app.speech.vendor.xtts_api_server.tts_funcs import TTSWrapper

# defaults
DEVICE = "cpu"
OUTPUT_FOLDER = ""
SPEAKER_FOLDER = f"{ os.path.dirname(__file__)}/vendor/xtts_api_server/speakers"
MODEL_FOLDER = f"{ os.path.dirname(__file__)}/vendor/xtts_api_server/xtts_models"
MODEL_SOURCE = os.getenv("MODEL_SOURCE", "local")
MODEL_VERSION = os.getenv("MODEL_VERSION", "v2.0.2")
LOWVRAM_MODE = False  # os.getenv("LOWVRAM_MODE") == "true"
DEEPSPEED = False
USE_CACHE = os.getenv("USE_CACHE") == "true"

XTTS: TTSWrapper = TTSWrapper(
    OUTPUT_FOLDER,
    SPEAKER_FOLDER,
    MODEL_FOLDER,
    LOWVRAM_MODE,
    MODEL_SOURCE,
    MODEL_VERSION,
    DEVICE,
    DEEPSPEED,
    USE_CACHE,
)


def initTTS():
    """
    Initialize the plugin.
    """
    global XTTS, MODEL_VERSION

    print("[bold green]- Initializing XTTS...[/bold green]")

    XTTS.model_version = XTTS.check_model_version_old_format(MODEL_VERSION)
    MODEL_VERSION = XTTS.model_version

    XTTS.load_model()


def generate_speech(prompt: str, output_path: str):
    initTTS()
    print(f"[green]Generating speech...[/green]")
    output_file_path = XTTS.process_tts_to_file(
        text=prompt,
        speaker_name_or_path="max",
        language="en",
        file_name_or_path=output_path,
    )
