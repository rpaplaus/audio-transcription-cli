from pathlib import Path
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

OUTPUT_DIR = Path("output")

PROMPT_TEMPLATE = """
You are an assistant specialized in analyzing audio transcripts.

From the transcript below, generate:
1. A concise executive summary (max 10 lines)
2. A list of main topics discussed
3. Key points, decisions, or action items (if any)

Be clear, objective, and avoid unnecessary verbosity.

Transcript:
---
{transcript}
---
"""

def analyze_transcript(transcript_text: str) -> str:
    prompt = PROMPT_TEMPLATE.format(transcript=transcript_text)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


def main():
    if not OUTPUT_DIR.exists():
        print("No output directory found.")
        return

    for project_dir in OUTPUT_DIR.iterdir():
        if not project_dir.is_dir():
            continue

        transcript_path = project_dir / "transcript.txt"
        summary_path = project_dir / "summary.md"

        if not transcript_path.exists():
            print(f"Skipping {project_dir.name}: no transcript.txt")
            continue

        print(f"Analyzing {project_dir.name}...")

        transcript = transcript_path.read_text(encoding="utf-8")
        summary = analyze_transcript(transcript)

        summary_path.write_text(summary, encoding="utf-8")

        print(f"Saved summary to {summary_path}")

    print("All done.")


if __name__ == "__main__":
    main()
