from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import os
import math
import re

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, "../data/processed/final_dataset.csv")
AUDIO_FOLDER = os.path.join(BASE_DIR, "../data/audio")

df = pd.read_csv(DATASET_PATH)


df["audio_path"] = df["audio_path"].apply(lambda x: x.replace("\\", "/"))

RESULTS_PER_PAGE = 5


def smart_search(df, query):
    words = query.lower().split()

    def match_score(text):
        text = str(text).lower()
        score = 0
        for word in words:
           
            if re.search(rf"\b{re.escape(word)}\b", text):
                score += 1
        return score

    df_copy = df.copy()
    df_copy["score"] = df_copy["text"].apply(match_score)

   
    filtered = df_copy[df_copy["score"] > 0]

    filtered = filtered.sort_values(by="score", ascending=False)

    return filtered



def highlight(text, query):
    words = query.split()

    for word in words:
        pattern = re.compile(rf"({re.escape(word)})", re.IGNORECASE)
        text = pattern.sub(r"<mark>\1</mark>", text)

    return text


@app.route("/", methods=["GET", "POST"])
def home():
    results = []

   
    query = request.form.get("query") or request.args.get("query", "")
    page = int(request.args.get("page", 1))

    total_pages = 0

    if query:
        filtered = smart_search(df, query)

        total_results = len(filtered)
        total_pages = math.ceil(total_results / RESULTS_PER_PAGE)

        start = (page - 1) * RESULTS_PER_PAGE
        end = start + RESULTS_PER_PAGE

        for _, row in filtered.iloc[start:end].iterrows():
            filename = os.path.basename(row["audio_path"])

            results.append({
                "audio": f"/audio/{filename}",
                "text": highlight(str(row["text"]), query)
            })

    return render_template(
        "index.html",
        results=results,
        query=query,
        page=page,
        total_pages=total_pages
    )



@app.route("/audio/<path:filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)