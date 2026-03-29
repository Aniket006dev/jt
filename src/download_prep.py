import pandas as pd
import requests
import os
import json
from tqdm import tqdm

INPUT_CSV = "data/raw/metadata.csv"
OUTPUT_CSV = "data/processed/final_dataset.csv"

AUDIO_DIR = "data/audio"
TRANSCRIPT_DIR = "data/transcripts"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def download_file(url, path):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
            return True
    except:
        return False
    return False


def get_transcription(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None


def process():
    df = pd.read_csv(INPUT_CSV)
    results = []

    for _, row in tqdm(df.iterrows(), total=len(df)):

        audio_url = row["audio_url"]
        trans_url = row["transcription_url"]

        filename = audio_url.split("/")[-1]
        base_name = filename.replace(".wav", "")

        audio_path = os.path.join(AUDIO_DIR, filename)
        transcript_path = os.path.join(TRANSCRIPT_DIR, base_name + ".json")

        if not os.path.exists(audio_path):
            success = download_file(audio_url, audio_path)
            if not success:
                continue

       
        data = get_transcription(trans_url)
        if not data:
            continue

        with open(transcript_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        text = " ".join([seg.get("text", "") for seg in data])

        if not text.strip():
            continue

        results.append({
            "audio_path": audio_path,
            "transcript_path": transcript_path,
            "text": text
        })

    final_df = pd.DataFrame(results)
    final_df.to_csv(OUTPUT_CSV, index=False)

    print("\nSaved:", OUTPUT_CSV)
    print("Total usable samples:", len(final_df))


if __name__ == "__main__":
    process()