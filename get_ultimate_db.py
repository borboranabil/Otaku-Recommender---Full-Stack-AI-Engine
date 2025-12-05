import requests
import pandas as pd
import time
from pathlib import Path

# --- SETTINGS ---
TARGET_PER_CATEGORY = 3000
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def fetch_category(name, endpoint, file_name, params=None):
    base_url = f"https://api.jikan.moe/v4/{endpoint}"
    if params is None: params = {}
    
    collected = []
    page = 1
    
    print(f"\n🚀 Starting download for: {name.upper()} (With Images)")
    print(f"   Target: {TARGET_PER_CATEGORY} items")

    while len(collected) < TARGET_PER_CATEGORY:
        try:
            current_params = params.copy()
            current_params["page"] = page
            
            print(f"   📥 Fetching Page {page} (Total: {len(collected)})...")
            response = requests.get(base_url, params=current_params)
            
            if response.status_code == 429:
                print("   ⏳ Rate limited. Sleeping 5s...")
                time.sleep(5)
                continue
            
            if response.status_code != 200: break
            data = response.json().get('data', [])
            if not data: break

            for item in data:
                # 1. Get Image URL
                try:
                    img_url = item['images']['jpg']['image_url']
                except:
                    img_url = "https://placehold.co/400x600?text=No+Image"

                # 2. Get Genres
                genres = [g['name'] for g in item.get('genres', []) + item.get('themes', []) + item.get('demographics', [])]
                genre_str = "|".join(genres) if genres else "General"
                
                # 3. Description
                desc = item.get('synopsis', '')
                if desc:
                    desc = desc.replace('\n', ' ').replace('\r', '').strip()
                else:
                    desc = ""

                collected.append({
                    "item_id": item['mal_id'],
                    "title": item['title'],
                    "genres": genre_str,
                    "description": desc,
                    "image_url": img_url  # <--- NEW FIELD
                })

            page += 1
            time.sleep(1.5)

        except Exception as e:
            print(f"   ❌ Crash: {e}")
            break

    # Save to CSV
    df = pd.DataFrame(collected)
    df.drop_duplicates(subset=['item_id'], inplace=True)
    output_path = DATA_DIR / file_name
    df.to_csv(output_path, index=False)
    print(f"🎉 Saved {len(df)} {name} to {output_path}")

def main():
    fetch_category("Anime", "top/anime", "anime.csv", params={"filter": "bypopularity"})
    fetch_category("Manga", "top/manga", "manga.csv", params={"type": "manga", "filter": "bypopularity"})
    fetch_category("Manhwa", "top/manga", "manhwa.csv", params={"type": "manhwa", "filter": "bypopularity"})

if __name__ == "__main__":
    main()