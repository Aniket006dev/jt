import pandas as pd
import requests
import os
import re
import json
from tqdm import tqdm
import whisper


INPUT_CSV = "data/raw/metadata.csv"
OUTPUT_CSV = "data/processed/final_dataset.csv"
AUDIO_DIR = "data/audio"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs("data/processed", exist_ok=True)


HEADERS = {"User-Agent": "Mozilla/5.0"}


print("Loading Whisper model...")
model = whisper.load_model("base")  

def download_file(url, path):
    try:
        if os.path.exists(path):
            return True

        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
            return True
    except Exception as e:
        print(f"Download failed: {url}")
    return False




def get_transcription(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            data = r.json()

          
            if isinstance(data, list):
                return " ".join([seg.get("text", "") for seg in data])

    except Exception as e:
        print(f"Transcription failed: {url}")

    return ""



def get_whisper_text(audio_path):
    try:
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"Whisper failed: {audio_path}")
        return ""



def detect_lang(word):
    for ch in word:
        if '\u0900' <= ch <= '\u097F':
            return "hi"
    return "en"


def tag_text(text):
    words = text.split()
    tagged = []

    for word in words:
        lang = detect_lang(word)
        tagged.append(f"{word}\\{lang}\\")

    return " ".join(tagged)



def num_to_words(num):
    mapping = {
        "0": "zero", "1": "one", "2": "two", "3": "three",
        "4": "four", "5": "five", "6": "six", "7": "seven",
        "8": "eight", "9": "nine", "10": "ten"
    }
    return mapping.get(num, num)


def normalize_numbers(text):
    return re.sub(r'\d+', lambda x: num_to_words(x.group()), text)



def process():
    df = pd.read_csv(INPUT_CSV)
    results = []

    print("Processing started...\n")

    for i, row in tqdm(df.iterrows(), total=len(df)):
        if i > 20:
            break
        audio_url = row["audio_url"]
        trans_url = row["transcription_url"]

        filename = audio_url.split("/")[-1]
        audio_path = os.path.join(AUDIO_DIR, filename)

        if not download_file(audio_url, audio_path):
            continue

   
        text = get_transcription(trans_url)

        if not text:
            text = get_whisper_text(audio_path)

        if not text:
            continue

   
        text = normalize_numbers(text)

        
        text = tag_text(text)

        results.append({
            "audio_path": audio_path,
            "text": text,
            "duration": row.get("duration", 0),
            "language": row.get("language", "unknown")
        })

    final_df = pd.DataFrame(results)
    final_df.to_csv(OUTPUT_CSV, index=False)

    print("\nSaved:", OUTPUT_CSV)
    print("Total usable samples:", len(final_df))



if __name__ == "__main__":
    process()