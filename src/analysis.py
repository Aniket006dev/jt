import pandas as pd
import os

INPUT_CSV = "data/processed/final_dataset.csv"
OUTPUT_FILE = "outputs/insights.txt"

os.makedirs("outputs", exist_ok=True)

def analyze():
    df = pd.read_csv(INPUT_CSV)

    total_samples = len(df)

    df["word_count"] = df["text"].apply(lambda x: len(str(x).split()))

    avg_words = df["word_count"].mean()

    
    try:
        meta = pd.read_csv("data/raw/metadata.csv")
        avg_duration = meta["duration"].mean()
        total_hours = meta["duration"].sum() / 3600
    except:
        avg_duration = 0
        total_hours = 0

    insights = f"""
Total Samples: {total_samples}

Average Words per Transcript: {avg_words:.2f}

Average Audio Duration (seconds): {avg_duration:.2f}

Total Audio Duration (hours): {total_hours:.2f}
"""

    with open(OUTPUT_FILE, "w") as f:
        f.write(insights)

    print(insights)


if __name__ == "__main__":
    analyze()