import subprocess
from pathlib import Path
from multiprocessing import Pool, cpu_count
from os import listdir, path

exe = Path(__file__).parent / "vgmstream" / "vgmstream-cli.exe"


def process(files: list[str]):
    if not files:
        return

    for awb_file in files:
        args = [exe, awb_file, "-o", f"{awb_file.removesuffix(".awb")}.wav"]
        subprocess.run(args)


def main():
    awb_files = [
        file for file in listdir(".") if path.isfile(file) and file.endswith(".awb")
    ]

    chunk_size = (len(awb_files) + cpu_count() - 1) // cpu_count()
    chunks = (
        awb_files[i : i + chunk_size]
        for i in range(0, len(awb_files) + chunk_size, chunk_size)
    )

    with Pool() as pool:
        pool.map(
            process,
            chunks,
        )


if __name__ == "__main__":
    main()
