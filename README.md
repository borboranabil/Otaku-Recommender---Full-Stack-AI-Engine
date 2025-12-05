# Otaku Recommender - Full-Stack AI Engine

> A next-gen recommendation system for **Anime, Manga, and Manhwa**.  
> Powered by **TF-IDF + Live Web Search (Jikan API)**, **FastAPI**, and **React**.

[Live Demo (Frontend - Vercel)](https://anime-multi-recommendation-engine.vercel.app)  
[Backend API (Render)](https://anime-recommender-i8w3.onrender.com)

---

## ✨ What makes this special?

Unlike standard recommendation engines that only suggest items from a fixed list, **Otaku Recommender is “alive”**:

1. **Smart TF-IDF Brain**  
   Uses `scikit-learn` TF-IDF over titles + genres + descriptions to find anime with similar *vibes*, not just exact words.

2. **Live Internet Fallback (Jikan API)**  
   If you search for something that isn’t in the local CSVs (e.g. “sad samurai revenge” or a brand-new anime),
   the backend:
   - queries the **Jikan API** (MyAnimeList),
   - builds a rich text description from the result,
   - and runs TF-IDF similarity against your local universe.

   This gives you “semantic-ish” recommendations without heavy GPU models.

3. **Multi-Media Support**  
   Works for **Anime**, **Manga**, and **Manhwa** – each with its own dataset.

4. **“Infinite Discovery” UI**  
   Click any recommendation card to pivot the search to that title instantly and keep jumping around the universe.

5. **Trailer Integration**  
   Every card comes with a **“Watch Trailer”** button that jumps straight to YouTube search for that title.

---

## 🖼 Screenshots

Dark Mode UI – Natural Language Search  
*(AI can handle queries like “sad story about a pianist” or “best samurai revenge” via web fallback.)*

> (Screenshots live in `/docs` – Vercel preview shows them nicely.)

---

## 🧠 Tech Stack

### Frontend (The Face)

- **Framework:** React (Vite)
- **Styling:** Tailwind CSS (Dark Mode)
- **Animations:** Framer Motion
- **Icons:** Lucide React
- **Hosting:** Vercel

### Backend (The Brain)

- **API Framework:** FastAPI (Python)
- **Modeling:** `scikit-learn` TF-IDF + cosine similarity
- **Data Handling:** Pandas, NumPy
- **Live Data:** Jikan API (MyAnimeList) for unknown / natural-language queries
- **Hosting:** Render (Free Web Service)

> ⚠️ Note: The current deployed version **does NOT use Sentence-BERT** anymore.  
> It’s optimized for lightweight TF-IDF + web descriptions so it can run in low-RAM environments like free Render.

---

## 🚀 How to Run Locally

### 1. Backend Setup (Python)

The backend handles the AI logic and data processing.

```bash
# 1. Create venv (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Download larger “universe” CSVs
#    You can use the smaller sample CSVs in /data or run:
# python get_ultimate_db.py

# 4. Start the API
uvicorn api:app --reload
# Backend will be at: http://127.0.0.1:8000
Useful endpoints:

GET /health – quick status check

GET /recommend – main recommendation endpoint

Example:

bash
Copy code
curl "http://127.0.0.1:8000/recommend?media_type=anime&query=naruto&topn=5&use_smart_search=true"
2. Frontend Setup (React)
bash
Copy code
cd frontend

# 1. Install libraries
npm install

# 2. Start dev server
npm run dev
# App runs at: http://localhost:5173
If you’re running the backend locally, you can point the frontend to http://127.0.0.1:8000.
For production, it’s already wired to your Render URL.

🧬 Project Structure
text
Copy code
Anime-Multi-Recommendation-Engine/
├── api.py                 # FastAPI server (TF-IDF + web search)
├── recommender.py         # Core ML logic (TF-IDF + helpers)
├── get_ultimate_db.py     # (Optional) data downloader script
├── data/                  # Anime/Manga/Manhwa CSVs
├── frontend/              # React application
│   ├── src/
│   │   ├── App.jsx        # Main UI code
│   │   └── main.jsx       # Entry point
│   └── tailwind.config.js # Styling config
└── README.md              # You are here 🙂
🔍 Recommendation Logic (Current Version)
Local Title Search

Try to match the query to an existing title in the CSV (exact or substring, case-insensitive).

If found → compute TF-IDF cosine similarity vs all items in that media type.

Response label:
engine_used = "TF-IDF (Local Title Match)"

Semantic-ish Search (toggle ON)

If title isn’t in the CSV and use_smart_search=true:

Call Jikan API for q=<your query>.

Build a “content” string from title + genres + synopsis.

Use that text as a query vector against the local TF-IDF matrix.

Response label:
engine_used = "TF-IDF (Live Web Mode)"
base_title = "<your original query> (Web Search)"

Smart Toggle OFF

If title isn’t found and use_smart_search=false:

Return 404 with a friendly message:
“Title not found in local dataset. Enable Semantic Search for web lookup.”

🛣 Future Roadmap
 User accounts + “Watch List”

 Simple rating system and collaborative filtering

 Better intent detection for natural-language queries

 Tag-based and mood-based recommendation modes

📜 License
Distributed under the MIT License – feel free to fork, hack, and build your own otaku brain.

yaml
Copy code

---

## 2️⃣ `requirements.txt` (replace whole file)

```txt
pandas
numpy
scikit-learn
fastapi==0.104.1
uvicorn==0.24.0
requests
