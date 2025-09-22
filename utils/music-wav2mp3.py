import subprocess
from multiprocessing import Pool
from os import listdir, path


def process(dir: str):
    if not path.isdir(dir):
        return
    subprocess.run(
        ["ffmpeg", "-i", f"{dir}/1.wav", "-qscale:a", "2", "-b:a", "192k", f"{dir}.mp3"]
    )


def main():
    with Pool() as pool:
        pool.map(process, listdir("."))


if __name__ == "__main__":
    main()
