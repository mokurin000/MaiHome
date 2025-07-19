import json
from os import listdir, makedirs, path

for version in listdir("."):
    if not path.isdir(version) or not version.startswith("maimai"):
        continue
    song_ids = listdir(version)
    manifest = {"name": version, "url": None, "id": None, "levelIds": song_ids}

    output_dir = path.join("collections", version)
    output_file = path.join(output_dir, "manifest.json")

    makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False)
