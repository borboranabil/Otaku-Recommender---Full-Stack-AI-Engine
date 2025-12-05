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

  <!-- Tech -->
  <img src="https://img.shields.io/badge/FastAPI-0.104.1-009485?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=white" />
  <img src="https://img.shields.io/badge/TF--IDF-ML%20Engine-F97316?style=for-the-badge" />

  <!-- License (Dual Licensing) -->
  <img src="https://img.shields.io/badge/License-Dual--Licensed-orange?style=for-the-badge" />

</p>

---

# 🌟 Overview

A next-gen recommendation system for **Anime, Manga, and Manhwa**, powered by:

- **TF-IDF semantic matching**
- **Natural language understanding**
- **Live Web Search Mode (Jikan API)**
- **Full-stack React + FastAPI**

🔗 **Frontend (Vercel):**  
https://anime-multi-recommendation-engine.vercel.app  

🔗 **Backend API (Render):**  
https://anime-recommender-i8w3.onrender.com  

---

# ✨ What Makes This Special?

Unlike most recommenders, **Otaku Recommender can interpret moods, themes, and descriptive prompts — not just titles.**

---

## 1️⃣ Smart TF-IDF Brain  
Every item is vectorized by:

- Title  
- Genres  
- Description  

This allows similarity based on **tone**, **vibe**, and **theme**, not keywords.

---

## 2️⃣ Semantic Text Mode (NEW)

If the input looks like natural language, the system treats it as a **semantic description**.

Example prompts:

sad story about a pianist
dark psychological thriller
samurai revenge tragedy
wholesome romance with comedy

yaml
Copy code

✔ No API required  
✔ Works for any text  
✔ Very fast  
✔ No embeddings needed  

**Label in API:**  
`TF-IDF (Semantic Text Mode)`

---

## 3️⃣ Live Web Mode (Jikan API)

Activated when:

- Query looks like a title  
- Not found in CSV  
- Smart mode ON  

Flow:

1. Fetch synopsis & genres from Jikan  
2. Build synthetic description  
3. Run TF-IDF similarity  

**Label:**  
`TF-IDF (Live Web Mode)`

---

## 4️⃣ Multi-Media Support

- Anime  
- Manga  
- Manhwa  

Each uses its own dataset.

---

## 5️⃣ Infinite Discovery UI

Clicking any card → instantly searches that item again.  
A smooth chain of endless recommendations.

---

## 6️⃣ YouTube Trailer Button  
Every card includes a link to search for the trailer instantly.

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

Finds themes like:

- Samurai  
- Revenge  
- Tragedy  
- Dark emotional conflict  

---

## 🧠 Semantic Query — *“dark psychological thriller”*
<p align="center">
  <img src="docs/screenshot-psychological.png" width="85%" />
</p>

Matches titles involving:

- Psychological tension  
- Thriller pacing  
- Mystery / horror  
- Emotional darkness  

---

# 🧠 Tech Stack

### **Frontend**
- React (Vite)
- Tailwind CSS
- Framer Motion
- Lucide Icons
- Hosted on Vercel

### **Backend**
- Python + FastAPI
- TF-IDF vectorization
- Cosine similarity
- Jikan API (Live Web Mode)
- Hosted on Render

> No Sentence-BERT — optimized for low-RAM free hosting.

---

# 🚀 How to Run Locally

## 1️⃣ Backend

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
uvicorn api:app --reload
Backend runs at:

cpp
Copy code
http://127.0.0.1:8000
Endpoints
Path	Description
/health	Status
/recommend	Recommendation engine
/docs	Swagger UI

Example:

bash
Copy code
curl "http://127.0.0.1:8000/recommend?media_type=anime&query=naruto&topn=5&use_smart_search=true"
2️⃣ Frontend
bash
Copy code
cd frontend
npm install
npm run dev
Runs at:

arduino
Copy code
http://localhost:5173
To use local backend:

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
├── docs/
└── README.md
🔍 Recommendation Logic Summary
✔ Local Title Match
Exact/substring match

Label: TF-IDF (Local Title Match)

✔ Semantic Text Mode
For descriptive prompts

Label: TF-IDF (Semantic Text Mode)

✔ Live Web Mode
Fetch from Jikan

Label: TF-IDF (Live Web Mode)

✔ Smart Mode OFF
Friendly 404 if title not found.

🛣 Roadmap
User accounts + favorites

Collaborative filtering

Mood-based search

Tag clustering

Anime detail pages

📜 License — Dual Licensing (IMPORTANT)
This project uses a Dual License Model:

🔓 GPLv3 (Free)
Use is free only if your entire project is also open-source under GPLv3.

💼 Commercial License (Paid)
Required for:

Closed-source apps

Commercial products

SaaS usage

Business integrations

Contact for commercial licensing:

your-email-here

🙌 Credits
Built with ❤️ by borboranabil
Powered by FastAPI, React, TF-IDF, and Jikan API
