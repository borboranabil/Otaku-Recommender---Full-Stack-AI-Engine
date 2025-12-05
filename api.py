from pathlib import Path
import requests
import pickle  # you can remove this import if you stop using any cache files
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from recommender import (
    load_items,
    build_tfidf_matrix,
    resolve_title_to_index,
    recommend_content,
)

DATA_DIR = Path(__file__).parent / "data"
MEDIA_FILES = {
    "anime": "anime.csv",
    "manga": "manga.csv",
    "manhwa": "manhwa.csv",
}

app = FastAPI(title="Anime Recommendation API", version="4.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# For each media_type we'll store: (items_df, tfidf_matrix)
ENGINE_STATE: dict[str, tuple] = {}


class Recommendation(BaseModel):
    item_id: int
    title: str
    genres: str
    image_url: str
    similarity_score: float


class RecommendResponse(BaseModel):
    media_type: str
    engine_used: str
    base_title: str
    topn: int
    recommendations: list[Recommendation]


@app.on_event("startup")
def startup_event():
    print("🚀 Starting up... Loading datasets and TF-IDF matrices...")
    for media, filename in MEDIA_FILES.items():
        path = DATA_DIR / filename
        if not path.exists():
            print(f"   ⚠ Skipping {media}, file not found: {path}")
            continue

        print(f"   📂 Loading {media} dataset from {path}...")
        items = load_items(path)

        # Build TF-IDF matrix (no embeddings anymore)
        _, tfidf_matrix = build_tfidf_matrix(items)

        ENGINE_STATE[media] = (items, tfidf_matrix)

    print("✅ System Ready!")


@app.get("/health")
def health_check():
    return {"status": "ok"}


def fetch_anime_live(query: str, media_type: str):
    """
    Still here if you want to use it later, but currently unused
    in the recommender (since we removed Sentence-BERT).
    """
    print(f"🌍 Searching internet for: {query}")
    try:
        api_type = "manga" if media_type in ["manga", "manhwa"] else "anime"
        url = f"https://api.jikan.moe/v4/{api_type}?q={query}&limit=1"
        response = requests.get(url, timeout=20)
        data = response.json()

        if not data.get("data"):
            return None
        item = data["data"][0]

        try:
            img = item["images"]["jpg"]["image_url"]
        except Exception:
            img = "https://placehold.co/400x600?text=No+Image"

        genres = [g["name"] for g in item.get("genres", [])]
        genre_str = ", ".join(genres)
        description = item.get("synopsis", "") or ""
        content = f"{item['title']} {genre_str} {description}"

        return {
            "title": item["title"],
            "content": content,
            "genres": genre_str,
            "image_url": img,
        }
    except Exception as e:
        print(f"API Error: {e}")
        return None


@app.get("/recommend", response_model=RecommendResponse)
def get_recommendations(
    media_type: str = Query("anime"),
    query: str = Query(...),
    topn: int = 5,
):
    media_type = media_type.lower()
    if media_type not in ENGINE_STATE:
        raise HTTPException(status_code=404, detail="Media type not loaded")

    items, tfidf_matrix = ENGINE_STATE[media_type]

    # Try to match the query to an existing title in the dataset
    idx, matched_title = resolve_title_to_index(items, query)

    if idx is None:
        # For now, if the title isn't in our dataset, we return 404.
        # (Smart web + embeddings mode was removed to fit Render free tier.)
        raise HTTPException(status_code=404, detail="Title not found in local dataset.")

    # Use TF-IDF similarity only
    recs_df = recommend_content(items, tfidf_matrix, item_index=idx, topn=topn)
    engine = "TF-IDF (Local)"

    return RecommendResponse(
        media_type=media_type,
        engine_used=engine,
        base_title=str(matched_title),
        topn=topn,
        recommendations=[
            Recommendation(
                item_id=int(row.item_id),
                title=str(row.title),
                genres=str(row.genres),
                image_url=str(row.image_url),
                similarity_score=float(row.similarity_score),
            )
            for _, row in recs_df.iterrows()
        ],
    )
