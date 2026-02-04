import shutil
from datetime import datetime
from pathlib import Path
from config import INPUT_DIR, OUTPUT_DIR, LOG_DIR, ALLOWED_EXTENSIONS


def setup_directories():
    OUTPUT_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)


def log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = LOG_DIR / "pipeline.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def is_valid_audio(file_path: Path) -> bool:
    return file_path.suffix.lower() in ALLOWED_EXTENSIONS


def ingest_files():
    if not INPUT_DIR.exists():
        log("Input directory does not exist.")
        return

    files = list(INPUT_DIR.iterdir())

    if not files:
        log("No files found in input directory.")
        return

    for file in files:
        if not file.is_file():
            continue

        if not is_valid_audio(file):
            log(f"Skipped unsupported file: {file.name}")
            continue

        project_dir = OUTPUT_DIR / file.stem
        project_dir.mkdir(exist_ok=True)

        destination = project_dir / file.name
        shutil.copy(file, destination)

        log(f"Ingested file: {file.name} -> {project_dir}")


if __name__ == "__main__":
    setup_directories()
    log("Pipeline started.")
    ingest_files()
    log("Pipeline finished.")
