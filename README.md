<p align="center"> <img src="docs/banner.png" alt="Anime Recommendation Engine Banner" width="100%"> </p> <p align="center"> <img src="https://img.shields.io/badge/Project-Anime%20%2F%20Manga%20%2F%20Manhwa%20Recommender-blue?style=for-the-badge"/> <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge"/> <img src="https://img.shields.io/badge/ML-Content--Based-orange?style=for-the-badge"/> <img src="https://img.shields.io/badge/Web-Streamlit-red?style=for-the-badge"/> <img src="https://img.shields.io/github/license/borboranabil/Anime-Multi-Recommendation-Engine?style=for-the-badge"/> </p>
🎌 Anime • Manga • Manhwa Multi-Recommendation Engine

A content-based AI recommendation system that can suggest similar titles from:

📺 Anime

📚 Manga

📙 Manhwa (Korean Webtoons)

Supports two recommendation engines:

⚡ TF-IDF (fast keyword-based)

🧠 Sentence-BERT (semantic meaning-based)

Also includes a fully interactive Streamlit Web App.

🧭 Table of Contents

Overview

Features

Supported Datasets

Tech Stack

Project Structure

How It Works

Web App (Streamlit UI)

How to Run

Example Session

Roadmap
---

## 📄 Documentation

- 📘 [Quickstart Guide](docs/QUICKSTART.md)
- 🧩 [System Architecture](docs/ARCHITECTURE.md)


License

Acknowledgements

📌 Overview

This project implements a multi-media recommendation engine supporting:

Anime

Manga

Manhwa

Recommendations are generated using:

title

genres

plot descriptions

The system works without user ratings — it is purely content-based.

⭐ Features
🔍 Recommendation Engines

TF-IDF + Cosine Similarity (fast, keyword-based)

Sentence-BERT semantic embeddings (understands meaning)

📚 Media Types Supported

Anime

Manga

Manhwa

🧠 Smart Text Processing

Cleans and merges description fields

Handles missing values automatically

🖥️ Two User Interfaces

Interactive CLI

Modern Streamlit Web App

🧩 Modular & Extensible

Add new datasets easily

Replace algorithms

Extend into collaborative filtering futures

📂 Supported Datasets

All datasets in /data/:

Type	File	Items
Anime	anime.csv	35+
Manga	manga.csv	35+
Manhwa	manhwa.csv	35+

Schema:

item_id, title, genres, description

🛠 Tech Stack
Language

Python 3.10+

Libraries

pandas

scikit-learn

Sentence-Transformers

Streamlit

numpy

Environment

VS Code

Git Bash / Terminal

📁 Project Structure
Anime-Multi-Recommendation-Engine/
│
├── data/
│   ├── anime.csv
│   ├── manga.csv
│   └── manhwa.csv
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── QUICKSTART.md
│   ├── webapp_screenshot.png
│   └── banner.png
│
├── app.py                # Streamlit Web UI
├── main.py               # CLI Interface
├── recommender.py        # TF-IDF + BERT logic
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

🔬 How It Works
1️⃣ Build the content field
df["content"] = df["title"] + " " + df["genres"] + " " + df["description"]

2️⃣ TF-IDF Vectorization
TfidfVectorizer(stop_words="english")

3️⃣ Semantic Embeddings (Sentence-BERT)
SentenceTransformer("all-MiniLM-L6-v2")

4️⃣ Cosine Similarity
linear_kernel(tfidf_matrix, tfidf_matrix)

🌐 Web App (Streamlit UI)

The project includes a fully interactive web app:

Features:

Dataset selector: Anime / Manga / Manhwa

Engine selector: TF-IDF or Sentence-BERT

Slider for number of recommendations

Search by item_id or title

Clean table view of items

Run the Web App:
streamlit run app.py


After running, open:

📌 http://localhost:8501

🔧 How to Run
1️⃣ Install requirements
pip install -r requirements.txt

2️⃣ Run CLI mode
python main.py

3️⃣ Run Web App
streamlit run app.py

🧪 Example Session (CLI)
=== Multi-Media Recommendation Engine ===
Select mode:
  1) Anime
  2) Manga
  3) Manhwa

Loaded dataset: anime.csv

Available titles:
1: Attack on Titan
2: Naruto
3: One Piece
...

Enter item_id: 1

Recommendations for: Attack on Titan
-----------------------------------------
9   Tokyo Ghoul
10  Tokyo Revengers
5   Demon Slayer
6   Jujutsu Kaisen
34  Idaten Deities

🚀 Roadmap
✅ Completed

✔ Streamlit Web App
✔ Sentence-BERT semantic engine
✔ Multi-dataset support
✔ Clean UI + Banner + Docs

🔧 Short-Term

⬜ Expand datasets to 150+ each
⬜ Add genre normalization
⬜ Add CSV import UI

⚙️ Medium-Term

⬜ Integrate AniList / MAL / Webtoon APIs
⬜ Add title-based global search

🧠 Long-Term

⬜ Build full website or mobile app
⬜ Deploy on cloud (Vercel / Railway)
⬜ Add collaborative filtering
⬜ Use GPT embeddings for similarity

📝 License

Distributed under the MIT License.

🙌 Acknowledgements

Built as an AI/ML learning project

Inspired by modern recommendation engines

Uses open-source Python libraries
