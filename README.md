<p align="center">
  <img src="docs/banner.png" alt="Otaku Recommender Banner" width="100%">
</p>

<h1 align="center">🎴 Otaku Recommender — Full-Stack AI Engine</h1>

<p align="center">
  AI-powered recommendations for Anime, Manga, and Manhwa  
  <br>
  Semantic Search • TF-IDF • Live Web Mode • FastAPI • React
</p>

<p align="center">

  <!-- Deployment Badges -->
  <a href="https://anime-multi-recommendation-engine.vercel.app">
    <img src="https://img.shields.io/badge/Frontend-Vercel-black?style=for-the-badge&logo=vercel" />
  </a>

  <a href="https://anime-recommender-i8w3.onrender.com">
    <img src="https://img.shields.io/badge/Backend-Render-0466C8?style=for-the-badge&logo=render" />
  </a>

  <!-- Tech Badges -->
  <img src="https://img.shields.io/badge/FastAPI-0.104.1-009485?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=white" />
  <img src="https://img.shields.io/badge/TF--IDF-ML%20Engine-F97316?style=for-the-badge" />

  <!-- Meta -->
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge" />

</p>

---

# 🌟 Overview

> A next-gen recommendation system for **Anime, Manga, and Manhwa**, powered by  
> **TF-IDF + Smart Semantic Search + Live Web Mode (Jikan API)**.

🔗 **Live Demo (Frontend – Vercel)**:  
https://anime-multi-recommendation-engine.vercel.app  

🔗 **Backend API (Render)**:  
https://anime-recommender-i8w3.onrender.com  

---

# ✨ What Makes This Special?

Unlike traditional recommenders, **Otaku Recommender is “alive.”**  
It understands **titles, descriptions, moods, themes, and even vague prompts.**

## 1️⃣ Smart TF-IDF Brain  
We vectorize:

- title  
- genres  
- description  

This lets the engine match anime by **tone, vibe, and theme**, not just keywords.

---

## 2️⃣ Semantic Text Mode (NEW)

If the user types a **descriptive natural-language query**, no API is needed.

Examples:

sad story about a pianist
dark psychological thriller
samurai revenge tragedy
wholesome romance with comedy

css
Copy code

The system treats the entire input as a **semantic description** → then performs TF-IDF similarity across all titles.

⚡ Works for ANY text  
⚡ Extremely fast  
⚡ No embeddings / GPU required  

Label used:
TF-IDF (Semantic Text Mode)

yaml
Copy code

---

## 3️⃣ Live Web Mode (Jikan API)

Triggered when:

- The query looks like a *title*,  
- It isn’t found in the CSV,  
- Semantic mode is ON.

Flow:

1. Fetch title + genres + synopsis from **Jikan**
2. Build text content
3. Run TF-IDF similarity on your local dataset

Label used:

TF-IDF (Live Web Mode)

yaml
Copy code

---

## 4️⃣ Multi-Media Support

Separate databases for:

- Anime  
- Manga  
- Manhwa  

---

## 5️⃣ Infinite Discovery UI

Click any recommendation card → immediately search based on that item.  
Creates a chain of *infinite recommendations*.

---

## 6️⃣ YouTube Trailer Button  
Instantly opens trailers based on the title.

---

# 🌟 Showcase — Smart Semantic Search in Action

## 🏠 Clean & Modern Homepage UI  
<p align="center">
  <img src="docs/screenshot-home.png" width="85%" />
</p>

---

## 🗡️ Semantic Query — *“samurai revenge tragedy”*
<p align="center">
  <img src="docs/screenshot-samurai.png" width="85%" />
</p>

The engine detects themes:

- Samurai  
- Revenge  
- Tragedy  
- Emotional conflict  

---

## 🧠 Semantic Query — *“dark psychological thriller”*
<p align="center">
  <img src="docs/screenshot-psychological.png" width="85%" />
</p>

Returns titles with:

- Psychological tension  
- Thriller pacing  
- Dark emotional tone  
- Mystery / mind games  

---

# 🧠 Tech Stack

### **Frontend**
- React (Vite)
- Tailwind CSS
- Framer Motion
- Lucide Icons
- Hosted on **Vercel**

### **Backend**
- Python + FastAPI
- TF-IDF vectorization
- Cosine similarity
- Jikan API for fallback search
- Hosted on **Render**

> ⚠️ No Sentence-BERT — this is tuned for **low-RAM free hosting**.

---

# 🚀 How to Run Locally

## 1️⃣ Backend Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt
uvicorn api:app --reload
Backend now runs at:

cpp
Copy code
http://127.0.0.1:8000
Useful Endpoints
Endpoint	Description
/health	Status check
/recommend	Recommendation engine
/docs	Swagger UI

Example:

bash
Copy code
curl "http://127.0.0.1:8000/recommend?media_type=anime&query=naruto&topn=5&use_smart_search=true"
2️⃣ Frontend Setup
bash
Copy code
cd frontend
npm install
npm run dev
Runs at:

arduino
Copy code
http://localhost:5173
To point frontend to local backend, edit:

js
Copy code
const BACKEND_URL = "http://127.0.0.1:8000";
🧬 Project Structure
css
Copy code
Otaku-Recommender/
├── api.py
├── recommender.py
├── data/
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── tailwind.config.js
├── docs/                  # Screenshots for README
└── README.md
🔍 Recommendation Logic Summary
✔ Local Title Match
Exact or substring match

TF-IDF similarity

Label: TF-IDF (Local Title Match)

✔ Semantic Text Mode (Descriptive Prompts)
If query is long / descriptive

Treat query as content

Label: TF-IDF (Semantic Text Mode)

✔ Live Web Mode (Unknown Titles)
Fetch from Jikan

Build synthetic content

TF-IDF similarity

Label: TF-IDF (Live Web Mode)

✔ Smart Mode OFF
Return friendly 404 if:

Title not found

Semantic mode disabled

🛣 Roadmap
User accounts + favorites

Collaborative filtering

Mood-based search

Tag-based clustering

Full anime detail pages

📜 License
MIT License — free for personal & commercial use.

🙌 Credits
Built with ❤️ by borboranabil
Powered by FastAPI, React, TF-IDF, and Jikan API
