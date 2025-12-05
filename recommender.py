from pathlib import Path  # <--- THIS LINE WAS MISSING OR BROKEN
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sentence_transformers import SentenceTransformer

def load_items(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df["genres"] = df["genres"].fillna("")
    df["description"] = df["description"].fillna("")
    df["title"] = df["title"].fillna("")
    
    # Ensure image_url exists if missing
    if "image_url" not in df.columns:
        df["image_url"] = "https://placehold.co/400x600?text=No+Image"

    df["content"] = (
        df["title"].astype(str) + " " +
        df["genres"].astype(str) + " " +
        df["description"].astype(str)
    )
    return df

def build_tfidf_matrix(items: pd.DataFrame):
    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(items["content"])
    return tfidf, matrix

def build_embedding_matrix(items: pd.DataFrame, model_name: str = "all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(
        items["content"].tolist(),
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return model, embeddings

def resolve_title_to_index(items: pd.DataFrame, query: str):
    query = query.lower().strip()
    titles = items['title'].str.lower().tolist()
    
    # 1. Exact Match
    if query in titles:
        idx = titles.index(query)
        return idx, items.iloc[idx]['title']
    
    # 2. Substring Match
    for idx, title in enumerate(titles):
        if query in title: 
            return idx, items.iloc[idx]['title']
            
    return None, None

def recommend_content(items: pd.DataFrame, matrix, *, item_index: int, topn: int = 5) -> pd.DataFrame:
    cosine_sim = linear_kernel(matrix[item_index:item_index + 1], matrix).flatten()
    indices = cosine_sim.argsort()[::-1]
    indices = [i for i in indices if i != item_index][:topn]
    
    result = items.iloc[indices].copy()
    result["similarity_score"] = [round(float(cosine_sim[i]), 3) for i in indices]
    # RETURN IMAGE URL
    return result[["item_id", "title", "genres", "image_url", "similarity_score"]]

def recommend_content_embeddings(items: pd.DataFrame, embeddings: np.ndarray, *, item_index: int, topn: int = 5) -> pd.DataFrame:
    query_vec = embeddings[item_index]
    scores = embeddings @ query_vec
    indices = scores.argsort()[::-1]
    indices = [i for i in indices if i != item_index][:topn]
    
    result = items.iloc[indices].copy()
    result["similarity_score"] = [round(float(scores[i]), 3) for i in indices]
    # RETURN IMAGE URL
    return result[["item_id", "title", "genres", "image_url", "similarity_score"]]