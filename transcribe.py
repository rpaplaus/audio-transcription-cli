from pathlib import Path
from datetime import datetime
from config import OUTPUT_DIR, LOG_DIR
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    raise RuntimeError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=openai_key)


def log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = LOG_DIR / "pipeline.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def transcribe_audio(audio_path: Path, output_dir: Path):
    transcript_path = output_dir / "transcript.txt"

    if transcript_path.exists():
        log(f"Transcript already exists for {audio_path.name}, skipping.")
        return

    try:
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="gpt-4o-transcribe"
            )

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcription.text)

        log(f"Transcription completed for {audio_path.name}")

    except Exception as e:
        log(f"Error transcribing {audio_path.name}: {str(e)}")


def run_transcription():
    for project_dir in OUTPUT_DIR.iterdir():
        if not project_dir.is_dir():
            continue

        audio_files = list(project_dir.glob("*.*"))
        for audio in audio_files:
            if audio.suffix.lower() in {".wav", ".mp3", ".aiff", ".m4a"}:
                transcribe_audio(audio, project_dir)


if __name__ == "__main__":
    log("Transcription phase started.")
    run_transcription()
    log("Transcription phase finished.")
