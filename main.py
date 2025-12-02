from pathlib import Path
from recommender import load_items, build_tfidf_matrix, recommend_content

DATA_DIR = Path(__file__).parent / "data"

def choose_mode():
    print("=== Multi-Media Recommendation Engine ===")
    print("Select mode:")
    print("  1) Anime")
    print("  2) Manga")
    print("  3) Manhwa")

    while True:
        choice = input("Enter choice (1/2/3 or q to quit): ").strip().lower()
        if choice in ("q", "quit", "exit"):
            return None
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice, try again.")

def get_csv_for_mode(choice: str) -> Path:
    if choice == "1":
        return DATA_DIR / "anime.csv"
    elif choice == "2":
        return DATA_DIR / "manga.csv"
    elif choice == "3":
        return DATA_DIR / "manhwa.csv"

def run_recommender(csv_path: Path):
    items = load_items(csv_path)
    _, matrix = build_tfidf_matrix(items)

    print(f"\nLoaded dataset: {csv_path.name}")
    print("Available titles:\n")
    for _, row in items[["item_id", "title"]].iterrows():
        print(f"  {row['item_id']}: {row['title']}")

    while True:
        raw = input("\nEnter item_id (or 'b' to go back, 'q' to quit): ").strip().lower()
        if raw in ("q", "quit"):
            return "quit"
        if raw in ("b", "back"):
            return "back"

        try:
            item_id = int(raw)
            recs = recommend_content(items, matrix, item_id=item_id, topn=5)
            title = items.loc[items["item_id"] == item_id, "title"].values[0]
            print(f"\nRecommendations for: {title}\n")
            print(recs.to_string(index=False))
        except:
            print("Invalid item_id. Try again.")

def main():
    while True:
        choice = choose_mode()
        if choice is None:
            break

        csv_path = get_csv_for_mode(choice)
        action = run_recommender(csv_path)
        if action == "quit":
            break

if __name__ == "__main__":
    main()
