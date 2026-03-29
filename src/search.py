import pandas as pd

DATASET = "data/processed/final_dataset.csv"


def search_word(query):
    df = pd.read_csv(DATASET)

    results = df[df["text"].str.contains(query, na=False)]

    if results.empty:
        print("No results found.")
        return

    print(f"\nFound {len(results)} results:\n")

    for i, row in results.head(5).iterrows():
        print(f"Audio File: {row['audio_path']}")
        print(f"Transcript: {row['text'][:150]}...")
        print("-" * 50)


if __name__ == "__main__":
    query = input("Enter word to search: ")
    search_word(query)