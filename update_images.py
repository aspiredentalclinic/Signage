import os
import json

BASE_URL = "https://aspiredentalclinic.github.io/Signage/assets/img/"
EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
JSON_FILE = os.path.join(os.path.dirname(__file__), "images.json")
SCAN_DIR = os.path.join(os.path.dirname(__file__), "assets", "img")

images = [
    BASE_URL + f
    for f in sorted(os.listdir(SCAN_DIR))
    if os.path.splitext(f)[1].lower() in EXTENSIONS
]

with open(JSON_FILE, "w") as f:
    json.dump(images, f, indent=2)

print(f"Updated images.json with {len(images)} image(s):")
for img in images:
    print(f"  {img}")
