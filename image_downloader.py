import os
import requests
from bs4 import BeautifulSoup

# a href links
HTML_FILE = "index.html"   

# saved folder
SAVE_DIR = "downloads"
os.makedirs(SAVE_DIR, exist_ok=True)

# read HTML file
with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# find <img> elements
images = [img["src"] for img in soup.find_all("img") if img.get("src")]

print(f"{len(images)} images found. downloading...")

for i, img_url in enumerate(images, 1):
    try:
        # download image
        response = requests.get(img_url, timeout=10)
        if response.status_code == 200:
            # file extension (jpg/png)
            ext = img_url.split(".")[-1].split("?")[0]
            filename = os.path.join(SAVE_DIR, f"img_{i}.{ext}")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"[✓] {filename}")
        else:
            print(f"[X] {img_url} could not download...")
    except Exception as e:
        print(f"[!] Hata: {img_url} - {e}")
