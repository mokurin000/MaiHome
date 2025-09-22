from os import listdir, path, makedirs, rename

for dir in listdir("."):
    if not path.isdir(dir):
        continue

    try:
        with open(f"{dir}/maidata.txt", "r", encoding="utf-8") as f:
            maidata = f.read()
    except FileNotFoundError:
        continue

    version = next(
        filter(lambda line: line.startswith("&version="), maidata.split("\n"))
    ).removeprefix("&version=")

    makedirs(version, exist_ok=True)
    rename(dir, f"{version}/{dir}")
