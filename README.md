# Otaku Recommender - Full-Stack AI Engine

> A next-gen recommendation system for **Anime, Manga, and Manhwa**.  
> Powered by **TF-IDF + Live Web Search (Jikan API)**, **FastAPI**, and **React**.

[Live Demo (Frontend - Vercel)](https://anime-multi-recommendation-engine.vercel.app)  
[Backend API (Render)](https://anime-recommender-i8w3.onrender.com)

---

## ✨ What makes this special?

Unlike standard recommendation engines that only suggest items from a fixed list, **Otaku Recommender is “alive”**:

### 1️⃣ Smart TF-IDF Brain  
Uses `scikit-learn` TF-IDF over titles + genres + descriptions to find anime with similar *vibes*, not just exact words.

### 2️⃣ Live Internet Fallback (Jikan API)  
If you search for something that isn’t in the local CSVs (e.g., **“sad samurai revenge”**, **“dark psychological thriller”**, etc.), the backend:

- queries the **Jikan API** (MyAnimeList),
- builds a rich text description,
- runs TF-IDF similarity against your local universe.

This gives “semantic-like” recommendations **without heavy GPU models**.

### 3️⃣ Multi-Media Support  
Works for **Anime**, **Manga**, and **Manhwa**, each with separate datasets.

### 4️⃣ Infinite Discovery UI  
Click any recommendation card → instantly start a new search based on that title.

### 5️⃣ Trailer Integration  
Each card has a **YouTube trailer** button.

---

# 🌟 Showcase — Smart Semantic Search in Action

The engine supports natural language queries, title-based search, and live web fallback.  
Here are real examples:

---

## 🏠 1. Clean & Modern Homepage UI

<p align="center">
  <img src="docs/screenshot-home.png" width="85%" />
</p>

Features:

- Anime / Manga / Manhwa media switch  
- Keyword vs Semantic mode  
- Vibe-based searching  
- Fully responsive dark UI  

---

## 🗡️ 2. Example Query — *“samurai revenge tragedy”* (Semantic Mode)

<p align="center">
  <img src="docs/screenshot-samurai.png" width="85%" />
</p>

The system identifies themes like:

- Samurai  
- Revenge  
- Tragedy  
- Historical conflict  

Even though the dataset does NOT contain these exact words, it finds conceptual matches using enhanced TF-IDF.

---

## 🧠 3. Example Query — *“dark psychological thriller”* (Semantic Mode)

<p align="center">
  <img src="docs/screenshot-psychological.png" width="85%" />
</p>

Matches:

- Psychological tension  
- Thriller pacing  
- Dark emotional tone  
- Mature themes  

This is the strongest demonstration of the “semantic-like” mode without BERT.

---

## 🧠 Tech Stack

### Frontend (The Face)
- **React (Vite)**
- **Tailwind CSS** (dark mode aesthetic)
- **Framer Motion** for smooth animations
- **Lucide Icons**
- **Vercel Hosting**

### Backend (The Brain)
- **FastAPI (Python)**
- **TF-IDF vectorization** (scikit-learn)
- **Cosine similarity engine**
- **Pandas + NumPy**
- **Jikan API** for live fallback search
- **Render Hosting**

> ⚠️ This deployed version **does NOT use Sentence-BERT**  
> It is optimized for **lightweight TF-IDF + external descriptions** to run reliably on Render free tier.

---

# 🚀 How to Run Locally

## 1️⃣ Backend Setup (Python)

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start API
uvicorn api:app --reload
Backend will be available at:

cpp
Copy code
http://127.0.0.1:8000
Useful Endpoints
Endpoint	Description
/health	Health check
/recommend	Main recommendation endpoint
/docs	Swagger UI

Example:

bash
Copy code
curl "http://127.0.0.1:8000/recommend?media_type=anime&query=naruto&topn=5&use_smart_search=true"
2️⃣ Frontend Setup (React)
bash
Copy code
cd frontend

npm install
npm run dev
Frontend runs at:

arduino
Copy code
http://localhost:5173
To use local backend, update App.jsx:

js
Copy code
const BACKEND_URL = "http://127.0.0.1:8000";
🧬 Project Structure
powershell
Copy code
Anime-Multi-Recommendation-Engine/
├── api.py                 # FastAPI server
├── recommender.py         # TF-IDF logic + helpers
├── data/                  # Anime/Manga/Manhwa CSV files
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # UI logic
│   │   └── main.jsx
│   └── tailwind.config.js
├── docs/                  # Screenshots for README
└── README.md              # You are here
🔍 Recommendation Logic (Current Version)
✔ Local Title Search
Try exact or substring match in CSV

If found → TF-IDF similarity

Label: TF-IDF (Local Title Match)

✔ Semantic Query Mode
If title NOT found and use_smart_search=true:

Query Jikan for the term

Build synthetic “content” string

Run TF-IDF similarity

Label:

scss
Copy code
TF-IDF (Live Web Mode)
✔ Smart Mode OFF
If title not found and semantic mode is off → return 404 message.

🛣 Roadmap
User accounts + watchlists

Rating system + collaborative filtering

Better intent detection

Mood-based recommendation mode

Full anime detail pages per title

📜 License
MIT License — Free for personal and commercial use.

🙌 Credits
Built with ❤️ by borboranabil
Powered by FastAPI, React, TF-IDF, and Jikan API
