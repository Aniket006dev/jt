# 🎤 Audio Dataset Processing & Search System

## 📌 Overview

This project focuses on building a complete pipeline for processing an audio dataset — starting from raw metadata to a usable dataset and an interactive search interface.

The goal was not just to clean and organize the data, but also to handle real-world issues like broken links, inconsistent formats, and missing information, and then make the data easily searchable through a simple UI.

---

## ⚙️ What I Built

The project is divided into three main parts:

### 1. Data Extraction & Fixing

* Loaded the provided dataset (CSV)
* Identified that the given URLs were not working as expected
* Correctly reconstructed the working URLs by extracting relevant parts from the original links

---

### 2. Data Preprocessing

* Downloaded audio files from the dataset
* Parsed transcription JSON files (handled list-based structure properly)
* Combined everything into a structured dataset (`final_dataset.csv`)
* Added fallback using Whisper for cases where transcription was missing
* Applied basic NLP preprocessing:

  * Language tagging (`word\hi\`, `word\en\`)
  * Number normalization

---

### 3. Data Analysis

* Calculated:

  * Total number of samples
  * Average words per transcript
  * Total and average audio duration

---

### 4. Search Interface (UI)

* Built a Flask-based web app
* Features:

  * Search using words or full sentences
  * Displays matching transcripts
  * Audio playback support
  * Pagination for results

---

## 🧠 Challenges Faced

Some real-world issues made this task interesting:

* **Broken URLs**
  The provided links didn’t work directly. I had to analyze and reconstruct them using patterns from the dataset.

* **Transcription format issue**
  The JSON files were lists of segments, not a single text field. This required proper parsing and merging.

* **Audio handling in UI**
  Initially, audio files were not playing due to incorrect paths and routing issues.

* **Multiple audio playback issue**
  Fixed by controlling playback so only one audio plays at a time.

---

## 🚀 Tech Stack

* Python
* Pandas
* Flask
* Requests
* Whisper (for speech-to-text fallback)

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run preprocessing:

```bash
python src/preprocessing.py
```

3. Start the web app:

```bash
python app/app.py
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
