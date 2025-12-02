<p align="center">
  <img src="docs/banner.png" alt="Anime Recommendation Engine Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Anime%20Recommender-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/github/license/borboranabil/Anime-Recommendation-Engine?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AI%2FML-Content--Based-orange?style=for-the-badge"/>
</p>

# Anime Recommendation Engine

A **content-based recommendation system** that can suggest similar titles across:

- 📺 **Anime**
- 📚 **Manga**
- 📙 **Manhwa (Korean webtoons)**

The engine uses **TF-IDF vectorization** over title, genres and description, and then applies **cosine similarity** to find the closest matches within the selected category.

---

## 🧭 Table of Contents

1. [Overview](#-1-overview)  
2. [Features](#-features)  
3. [Supported Datasets](#-supported-datasets)  
4. [Tech Stack](#-tech-stack)  
5. [Project Structure](#-project-structure)  
6. [How It Works](#-how-it-works)  
7. [How to Run](#-how-to-run)  
8. [Example Session](#-example-session)  
9. [Roadmap](#-roadmap)  
10. [License](#-license)

---

## 📌 1. Overview

This project implements a **multi-media content recommendation system** as part of an academic AI/ML project.

It supports three media types:

- Anime (TV / movie series)
- Manga (Japanese comics)
- Manhwa (Korean webtoons)

Given a title’s `item_id`, the system returns a list of **similar titles** from the same category based on:

- Title keywords  
- Genre tags  
- Short plot description  

The approach is purely **content-based** — it does **not** require user ratings or watch history.

---

## ⭐ Features

- 🔍 **Content-Based Recommendation**  
  Uses **TF-IDF vectorization** on combined text (`title + genres + description`) with **cosine similarity**.

- 📺 **Multi-Category Support**  
  Works with **Anime**, **Manga**, and **Manhwa** datasets using a single engine.

- 📂 **CSV-Based Datasets**  
  Simple and easy to edit: each dataset is just a `.csv` file.

- 🧠 **Text Preprocessing**  
  Handles missing values and merges relevant fields into a single content column.

- ⚡ **Fast Querying**  
  Pre-computes TF-IDF matrix once per dataset and reuses it for multiple queries.

- 🖥️ **CLI Interface**  
  Clean command-line menu where the user:
  1. Chooses the media type  
  2. Sees all available titles  
  3. Enters an `item_id` to get recommendations  

- 🧩 **Extensible Design**  
  You can easily:
  - Add more rows to existing datasets  
  - Add new dataset types (e.g., light novels)  
  - Replace the CLI with a web UI later

---

## 📂 Supported Datasets

All datasets are stored in the `data/` folder and share the same schema:

```text
item_id, title, genres, description
Current datasets:

Type	File	Entries (approx.)
Anime	data/anime.csv	35+
Manga	data/manga.csv	35+
Manhwa	data/manhwa.csv	35+

Each row contains:

item_id – numeric unique ID

title – name of the anime/manga/manhwa

genres – pipe-separated tags (e.g. Action|Fantasy)

description – short description used for similarity

🛠 Tech Stack
Language: Python 3.x

Libraries:

pandas – data handling

scikit-learn

TfidfVectorizer – text vectorization

linear_kernel – cosine similarity

Environment:

VS Code / any Python IDE

Command Line (Git Bash / PowerShell / Terminal)

📁 Project Structure
text
Copy code
Anime-Recommendation-Engine/
│
├── data/
│   ├── anime.csv
│   ├── manga.csv
│   └── manhwa.csv
│
├── docs/
│   ├── QUICKSTART.md
│   ├── ARCHITECTURE.md
│   └── banner.png
│
├── main.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
🔬 How It Works
Mode selection (in main.py)
User chooses one of:

1 → Anime

2 → Manga

3 → Manhwa

Dataset loading (recommender.load_items)

Reads the appropriate CSV file.

Fills missing genres / description with empty strings.

Creates a new text field content:

python
Copy code
df["content"] = df["title"] + " " + df["genres"] + " " + df["description"]
Vectorization (build_tfidf_matrix)

Uses TfidfVectorizer(stop_words="english") on content.

Returns the TF-IDF matrix for all titles.

Similarity computation (recommend_content)

For a given item_id, locate its index.

Compute cosine similarity with all other rows using linear_kernel.

Sort scores from highest to lowest and return the top N matches (excluding itself).

CLI Display

Prints all titles with item_id.

When user enters an item_id, shows the recommended titles and genres in a table.

🔧 How to Run
1️⃣ Install Requirements
First, make sure you are in the project folder:

bash
Copy code
cd Anime-Recommendation-Engine
Install dependencies:

bash
Copy code
python -m pip install -r requirements.txt
2️⃣ Run the Engine
bash
Copy code
python main.py
You will see:

text
Copy code
=== Multi-Media Recommendation Engine ===
Select mode:
  1) Anime
  2) Manga
  3) Manhwa
Enter 1 for Anime, 2 for Manga, or 3 for Manhwa.

After selection, all titles with their item_id are printed.

3️⃣ Get Recommendations
Enter an item_id from the list (e.g. 12), and the engine will print the top 5 similar titles in that same category.

Type b to go back to the mode menu.

Type q to exit.

🧪 Example Session
text
Copy code
=== Multi-Media Recommendation Engine ===
Select mode:
  1) Anime
  2) Manga
  3) Manhwa
Enter choice (1/2/3 or q to quit): 1

Loaded dataset: anime.csv
Available titles:

  1: Attack on Titan
  2: Naruto
  3: One Piece
  ...
  35: Blue Lock

Enter item_id (or 'b' to go back, 'q' to quit): 1

Recommendations for: Attack on Titan

 item_id                 title              genres
      9           Tokyo Ghoul       Action|Horror
     10       Tokyo Revengers        Action|Drama
      5            Demon Slayer Action|Dark Fantasy
      6          Jujutsu Kaisen Action|Supernatural
     34 The Idaten Deities Know Only Peace Action|Fantasy
🚀 Roadmap
Planned and possible improvements:

🔧 Short-Term
 Expand each dataset to 100+ titles

 Clean and normalize genre tags

 Add parameter to change number of recommendations (top-N)

⚙️ Medium-Term
 Integrate AniList / MyAnimeList / Webtoon APIs

 Add rating and popularity weighting to ranking

 Add command-line search by title name (not only item_id)

🧠 Long-Term
 Build a Streamlit or web UI for easier usage

 Add collaborative filtering (user-based recommendations)

 Use embedding-based similarity (e.g., Sentence Transformers)

 Deploy online (Railway / Vercel / Render)

📝 License
This project is licensed under the MIT License.
See the LICENSE file for details.

🙌 Acknowledgements
Built as a learning project for AI & ML applications.

Inspired by common recommendation system techniques used in streaming platforms.

Uses open-source Python libraries from the scientific ecosystem.


