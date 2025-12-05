from pathlib import Path
import requests
import pickle
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from recommender import (
    load_items, build_tfidf_matrix, build_embedding_matrix,
    resolve_title_to_index, recommend_content, recommend_content_embeddings
)

DATA_DIR = Path(__file__).parent / "data"
MEDIA_FILES = {"anime": "anime.csv", "manga": "manga.csv", "manhwa": "manhwa.csv"}

app = FastAPI(title="Anime Recommendation API", version="4.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ENGINE_STATE = {}

class Recommendation(BaseModel):
    item_id: int
    title: str
    genres: str
    image_url: str  # <--- NEW FIELD
    similarity_score: float

class RecommendResponse(BaseModel):
    media_type: str
    engine_used: str
    base_title: str
    topn: int
    recommendations: list[Recommendation]

@app.on_event("startup")
def startup_event():
    print("🚀 Starting up... Loading datasets and models...")
    for media, filename in MEDIA_FILES.items():
        path = DATA_DIR / filename
        if not path.exists(): continue
            
        print(f"   📂 Loading {media} dataset...")
        items = load_items(path)
        
        _, tfidf = build_tfidf_matrix(items)
        
        cache_path = DATA_DIR / f"{media}_embeddings.pkl"
        if cache_path.exists():
            print(f"      ⚡ Loading cached embeddings for {media}...")
            with open(cache_path, "rb") as f:
                data = pickle.load(f)
                model = data["model"]
                embeddings = data["embeddings"]
        else:
            print(f"      🧠 Building NEW embeddings for {media}...")
            model, embeddings = build_embedding_matrix(items)
            with open(cache_path, "wb") as f:
                pickle.dump({"model": model, "embeddings": embeddings}, f)
        
        ENGINE_STATE[media] = (items, tfidf, embeddings, model)
    print("✅ System Ready!")

@app.get("/health")
def health_check():
    return {"status": "ok"}

def fetch_anime_live(query: str, media_type: str):
    print(f"🌍 Searching internet for: {query}")
    try:
        api_type = "manga" if media_type in ["manga", "manhwa"] else "anime"
        url = f"https://api.jikan.moe/v4/{api_type}?q={query}&limit=1"
        response = requests.get(url, timeout=20) 
        data = response.json()

        if not data.get("data"): return None
        item = data["data"][0]
        
        try:
            img = item['images']['jpg']['image_url']
        except:
            img = "https://placehold.co/400x600?text=No+Image"

        genres = [g["name"] for g in item.get("genres", [])]
        genre_str = ", ".join(genres)
        description = item.get("synopsis", "") or ""
        content = f"{item['title']} {genre_str} {description}"
        
        return {"title": item["title"], "content": content, "genres": genre_str, "image_url": img}
    except Exception as e:
        print(f"API Error: {e}")
        return None

@app.get("/recommend", response_model=RecommendResponse)
def get_recommendations(media_type: str = Query("anime"), query: str = Query(...), topn: int = 5, use_smart_search: bool = True):
    media_type = media_type.lower()
    if media_type not in ENGINE_STATE: raise HTTPException(404, "Media type not loaded")

    items, tfidf, embeddings, model = ENGINE_STATE[media_type]
    idx, matched_title = resolve_title_to_index(items, query)

    if idx is None:
        live_data = fetch_anime_live(query, media_type)
        if not live_data: raise HTTPException(404, detail="Not found.")
        
        matched_title = f"{live_data['title']} (Web Search)"
        engine = "Sentence-BERT (Live Web Mode)"
        query_vector = model.encode([live_data["content"]])
        scores = (embeddings @ query_vector.T).flatten()
        top_indices = scores.argsort()[::-1][:topn]
        recs_df = items.iloc[top_indices].copy()
        recs_df["similarity_score"] = scores[top_indices]
    else:
        if use_smart_search:
            recs_df = recommend_content_embeddings(items, embeddings, item_index=idx, topn=topn)
            engine = "Sentence-BERT (Local)"
        else:
            recs_df = recommend_content(items, tfidf, item_index=idx, topn=topn)
            engine = "TF-IDF (Local)"

    return RecommendResponse(
        media_type=media_type, engine_used=engine, base_title=str(matched_title), topn=topn,
        recommendations=[
            Recommendation(
                item_id=int(row.item_id),
                title=str(row.title),
                genres=str(row.genres),
                image_url=str(row.image_url),
                similarity_score=float(row.similarity_score)
            ) for _, row in recs_df.iterrows()
        ]
    )