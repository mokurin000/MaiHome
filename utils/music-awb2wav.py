import subprocess
from pathlib import Path
from multiprocessing import Pool, cpu_count
from os import listdir, path, rename, makedirs

CRIWARE_SRC = Path("C:/Software/CriTools/") / "src" / "index.js"


def process(arg: tuple[list[str], int]):
    files, chunk_no = arg
    if not files:
        return

    chunk_dir = Path(f"chunk{chunk_no:03}")
    makedirs(chunk_dir, exist_ok=True)

    for file in files:
        awb_file = file.replace(".acb", ".awb")

        rename(file, chunk_dir / file)
        rename(awb_file, chunk_dir / awb_file)

    args = [
        "node",
        CRIWARE_SRC,
        "awb2wavs",
        "-k",
        "9170825592834449000",
        "-d",
        chunk_dir,
    ]
    subprocess.run(args)

    for file in files:
        outdir = file.replace(".acb", "")
        rename(chunk_dir / outdir, outdir)


def main():
    acb_files = [
        file for file in listdir(".") if path.isfile(file) and file.endswith(".acb")
    ]

    chunk_size = (len(acb_files) + cpu_count() - 1) // cpu_count()
    chunks = (
        (acb_files[i : i + chunk_size], i // chunk_size)
        for i in range(0, len(acb_files) + chunk_size, chunk_size)
    )

    with Pool() as pool:
        pool.map(
            process,
            chunks,
        )


if __name__ == "__main__":
    main()

