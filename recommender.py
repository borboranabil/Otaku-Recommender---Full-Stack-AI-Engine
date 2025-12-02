import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from pathlib import Path

def load_items(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df["genres"] = df["genres"].fillna("")
    df["description"] = df["description"].fillna("")
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

def recommend_content(items, matrix, item_id, topn=5):
    idx = items.index[items["item_id"] == item_id][0]
    cosine_sim = linear_kernel(matrix[idx:idx+1], matrix).flatten()
    indices = cosine_sim.argsort()[::-1]
    indices = [i for i in indices if i != idx]
    return items.iloc[indices[:topn]][["item_id", "title", "genres"]]
