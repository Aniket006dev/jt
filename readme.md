🎤 Hindi ASR Processing & Analysis System

🔗 Live Demo: https://jt-1.onrender.com/

🔗 GitHub: https://github.com/Aniket006dev/jt

📌 Overview

This project focuses on building a robust pipeline for Hindi ASR data processing, analysis, and improvement.

It includes:

Data preprocessing from raw audio + metadata
Transcript cleaning & normalization
Error analysis of ASR outputs
Web-based interface for search & exploration
🔹 Question 1: ASR Model Analysis
a) Data Preprocessing
Fixed broken dataset URLs by reconstructing valid GCP links
Downloaded audio and transcription JSON files
Parsed transcription (list → merged text)
Created structured dataset (final_dataset.csv)
b) Model Usage
Used Whisper (baseline) for transcription fallback
(If not fine-tuned — be honest)
c) Evaluation (WER)
| Model              | WER |
|-------------------|-----|
| Whisper-small     | TBD |
| Fine-tuned model  | TBD |

⚠️ (Note: Full fine-tuning not completed due to time constraints)

d) Error Sampling Strategy
Selected every Nth incorrect prediction
Ensured diverse error coverage
Avoided cherry-picking
e) Error Taxonomy
1. Number Errors
Example: "पच्चीस" → "25"
2. English Word Misinterpretation
Example: "इंटरव्यू" misrecognized
3. Phonetic Errors
Accent / pronunciation mismatch
f) Proposed Fixes
Number normalization
English word tagging
Better preprocessing pipeline
g) Fix Implementation

✔ Implemented:

Number normalization
Language tagging
🔹 Question 2: Cleanup Pipeline
a) Number Normalization
Examples:
दो सौ पचास → 250 ✅
पच्चीस → 25 ✅
दो-चार बातें → unchanged ❗
Edge Cases:
Idioms not converted to digits
b) English Word Detection
Input: मेरा इंटरव्यू अच्छा गया  
Output: मेरा [EN]इंटरव्यू[/EN] अच्छा गया
🔹 Question 3: Spelling Analysis
Approach:
Frequency-based filtering
Heuristic validation
Output:

📊 Google Sheet: (ADD LINK HERE)

Observations:
High-confidence words → correct
Low-confidence → ambiguous / mixed language
🔹 Question 4: Lattice-Based Evaluation
Approach:
Combine outputs from multiple models
Group alternatives into bins
Example:
["चौदह", "14"]
["किताबें", "पुस्तकें"]
Benefit:
Reduces unfair WER penalties
Captures valid variations
🔹 Web Application
Features:
Search transcripts
Audio playback
Pagination
🧠 Challenges
Broken dataset URLs
JSON parsing complexity
Audio handling in UI
🚀 Tech Stack
Python
Flask
Pandas
Whisper
▶️ How to Run
pip install -r requirements.txt
python src/preprocessing.py
python app/app.py
<<<<<<< HEAD
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Output

* Final dataset with:

  * Audio paths
  * Cleaned & processed transcripts
  * Metadata (duration, language)

* Interactive UI for searching and playing audio

---

## 🎯 Final Thoughts

This task helped me understand how messy real-world data can be and how important it is to build systems that can handle inconsistencies.

I tried to go beyond basic requirements by:

* Handling edge cases
* Adding fallback mechanisms
* Building a usable interface instead of just scripts

---

## Future Improvements

* Better search (semantic / embeddings)
* Improved UI/UX
* Faster transcription pipeline
=======
🎯 Key Highlights
Real-world data handling
End-to-end pipeline
Deployment + UI
🔮 Future Work
Whisper fine-tuning
Better WER evaluation
Semantic search
>>>>>>> aa0292290fc95524ddfcf6897f4e567b8b718d86
