import subprocess
from multiprocessing import Pool
from os import listdir, path


def process(wav_file: str):
    if not path.isfile(wav_file) or not wav_file.endswith(".wav"):
        return
    out_file = f"{wav_file.removesuffix('.wav')}.mp3"
    if path.exists(out_file):
        return
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            wav_file,
            "-qscale:a",
            "2",
            "-b:a",
            "192k",
            out_file,
        ]
    )


def main():
    with Pool() as pool:
        pool.map(process, listdir("."))


if __name__ == "__main__":
    main()
