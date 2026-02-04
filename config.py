from pathlib import Path
import os

# Pastas base
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "audio_input"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

# Extensões permitidas
ALLOWED_EXTENSIONS = {".wav", ".mp3", ".aiff", ".m4a"}

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")