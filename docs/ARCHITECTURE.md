```markdown
# Architecture – Anime Recommendation System

## 1. Overview
This project is a **Content-Based Recommendation System** built using:
- Python  
- TF-IDF Vectorization  
- Cosine Similarity  

The system recommends anime based on similarities in:
- Title  
- Genres  
- Description  

## 2. Project Structure

Anime-Recommendation-System/
│
├── data/
│ └── items.csv → Anime dataset
│
├── recommender.py → ML logic (TF-IDF + similarity)
├── main.py → CLI interface
├── requirements.txt → Dependencies
└── README.md → Project overview

markdown
Copy code

## 3. Data Flow

1. **Load Dataset**  
   `load_items()` reads `data/items.csv` into a pandas DataFrame.

2. **Preprocess Text**  
   Title, genres, and description are combined into one column:  
content = title + " " + genres + " " + description

markdown
Copy code

3. **Normalize Missing Values**  
Uses `.fillna("")` to handle empty fields.

4. **Vectorization (TF-IDF)**  
Converts text into machine-readable vectors.  
Removes English stop words.

5. **Similarity Calculation**  
`linear_kernel()` computes cosine similarity between all anime.

6. **Recommendation Output**  
For a given anime ID, the closest matches are returned.

## 4. Important Functions

### `load_items()`
Loads and preprocesses the CSV dataset.

### `build_tfidf_matrix(items)`
Builds the TF-IDF matrix and computes similarity scores.

### `recommend_content(item_id, items, tfidf_matrix)`
Returns top similar anime titles.

## 5. Example Recommendation Logic

User selects Attack on Titan (item_id=1)
↓
System checks its TF-IDF vector
↓
Finds nearest anime based on cosine similarity
↓
Returns titles like:

Tokyo Ghoul

Jujutsu Kaisen

Demon Slayer

yaml
Copy code

## 6. Future Improvements

### 🔮 Planned Features:
- Use a larger dataset (AniList / MyAnimeList API)
- Add popularity or rating scores
- Build a web UI (Flask, FastAPI, or Streamlit)
- Add collaborative filtering (user-based recommendations)
- Implement a vector database (FAISS / Pinecone) for fast search

---

This architecture document helps future contributors and keeps the project maintainable.
