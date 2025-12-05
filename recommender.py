from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def load_items(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    # Fill missing values
    df["genres"] = df.get("genres", "").fillna("")
    df["description"] = df.get("description", "").fillna("")
    df["title"] = df.get("title", "").fillna("")

    # Ensure image_url exists if missing
    if "image_url" not in df.columns:
        df["image_url"] = "https://placehold.co/400x600?text=No+Image"

    # Text used for similarity
    df["content"] = (
        df["title"].astype(str)
        + " "
        + df["genres"].astype(str)
        + " "
        + df["description"].astype(str)
    )
    return df


def build_tfidf_matrix(items: pd.DataFrame):
    """
    Build a TF-IDF matrix over the 'content' column.
    Returns both the vectorizer and the matrix.
    """
    tfidf = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=50000,
    )
    matrix = tfidf.fit_transform(items["content"])
    return tfidf, matrix


def resolve_title_to_index(items: pd.DataFrame, query: str):
    """
    Try to match a user query to a title in the dataset
    using exact and then substring matching (case-insensitive).
    """
    query = query.lower().strip()
    titles = items["title"].str.lower().tolist()

    # 1. Exact match
    if query in titles:
        idx = titles.index(query)
        return idx, items.iloc[idx]["title"]

    # 2. Substring match
    for idx, title in enumerate(titles):
        if query in title:
            return idx, items.iloc[idx]["title"]

    return None, None


def recommend_content(
    items: pd.DataFrame,
    matrix,
    *,
    item_index: int,
    topn: int = 5,
) -> pd.DataFrame:
    """
    TF-IDF cosine similarity recommendation based on an EXISTING item.
    """
    cosine_sim = linear_kernel(matrix[item_index : item_index + 1], matrix).flatten()

    indices = cosine_sim.argsort()[::-1]
    indices = [i for i in indices if i != item_index][:topn]

    result = items.iloc[indices].copy()
    result["similarity_score"] = [round(float(cosine_sim[i]), 3) for i in indices]

    return result[["item_id", "title", "genres", "image_url", "similarity_score"]]


def recommend_from_text(
    items: pd.DataFrame,
    tfidf,
    matrix,
    *,
    text: str,
    topn: int = 5,
) -> pd.DataFrame:
    """
    TF-IDF similarity using arbitrary text (used for live web search content).
    """
    query_vec = tfidf.transform([text])
    cosine_sim = linear_kernel(query_vec, matrix).flatten()

    indices = cosine_sim.argsort()[::-1][:topn]

    result = items.iloc[indices].copy()
    result["similarity_score"] = [round(float(cosine_sim[i]), 3) for i in indices]

    return result[["item_id", "title", "genres", "image_url", "similarity_score"]]
