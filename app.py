from pathlib import Path

import pandas as pd
import streamlit as st

from recommender import (
    load_items,
    build_tfidf_matrix,
    build_embedding_matrix,
    resolve_title_to_index,
    recommend_content,
    recommend_content_embeddings,
)

DATA_DIR = Path(__file__).parent / "data"


# ----------------------------
# Cached helpers
# ----------------------------

@st.cache_data
def get_items(kind: str) -> pd.DataFrame:
    if kind == "Anime":
        path = DATA_DIR / "anime.csv"
    elif kind == "Manga":
        path = DATA_DIR / "Manga.csv" if (DATA_DIR / "Manga.csv").exists() else DATA_DIR / "manga.csv"
    else:
        path = DATA_DIR / "manhwa.csv"
    return load_items(path)


@st.cache_resource
def get_tfidf_matrix(kind: str):
    items = get_items(kind)
    _, matrix = build_tfidf_matrix(items)
    return matrix


@st.cache_resource
def get_embedding_matrix(kind: str):
    items = get_items(kind)
    _, embeddings = build_embedding_matrix(items)
    return embeddings


# ----------------------------
# Streamlit UI
# ----------------------------

def main():
    st.set_page_config(
        page_title="Anime / Manga / Manhwa Recommender",
        page_icon="🍥",
        layout="wide",
    )

    st.title("🎌 Anime • Manga • Manhwa Recommendation Engine")

    st.markdown(
        "Content-based recommendation system supporting **TF-IDF** and "
        "**Sentence-BERT (semantic)** similarity."
    )

    with st.sidebar:
        st.header("⚙️ Settings")

        dataset_kind = st.selectbox(
            "Choose dataset:",
            ["Anime", "Manga", "Manhwa"],
            index=0,
        )

        engine = st.radio(
            "Recommendation Engine:",
            ["TF-IDF (fast)", "Semantic (Sentence-BERT)"],
            index=0,
        )

        topn = st.slider(
            "Number of recommendations",
            min_value=1,
            max_value=15,
            value=5,
            step=1,
        )

    # Load data
    items = get_items(dataset_kind)

    st.subheader(f"Dataset: {dataset_kind} ({len(items)} items)")
    st.dataframe(items[["item_id", "title", "genres"]].head(10), use_container_width=True)

    query = st.text_input(
        "Enter an **item_id** or a **title**:",
        placeholder="e.g., 1 or Attack on Titan",
    )

    if st.button("🔍 Get Recommendations"):

        if not query.strip():
            st.warning("Please enter an item_id or title.")
            return

        # Resolve query -> item_index
        raw = query.strip()
        idx = None
        base_title = None
        item_id = None

        if raw.isdigit():
            item_id = int(raw)
            matches = items.index[items["item_id"] == item_id].tolist()
            if not matches:
                st.error("No item with that item_id found in this dataset.")
                return
            idx = matches[0]
            base_title = items.loc[idx, "title"]
        else:
            idx, matched_title = resolve_title_to_index(items, raw)
            if idx is None:
                st.error("Could not match that title to anything in the dataset.")
                return
            item_id = int(items.loc[idx, "item_id"])
            base_title = matched_title
            st.info(f"Using best match: **{matched_title}** (item_id={item_id})")

        # Choose engine
        if engine.startswith("TF-IDF"):
            matrix = get_tfidf_matrix(dataset_kind)
            recs = recommend_content(items, matrix, item_index=idx, topn=topn)
            engine_label = "TF-IDF"
        else:
            embeddings = get_embedding_matrix(dataset_kind)
            recs = recommend_content_embeddings(items, embeddings, item_index=idx, topn=topn)
            engine_label = "Sentence-BERT"

        st.subheader(f"Recommendations for: {base_title} (item_id={item_id})")
        st.caption(f"Engine: {engine_label}")

        st.dataframe(recs, use_container_width=True)


if __name__ == "__main__":
    main()
