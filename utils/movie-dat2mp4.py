import subprocess
from pathlib import Path
from os import listdir, makedirs, rename
from multiprocessing import Pool, cpu_count


def batched(iterable, n: int):
    from itertools import islice

    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def dat2ivf(i: int):
    path = f"split_{i}"
    subprocess.run(
        [
            # uv tool install --with python-json-logger git+https://github.com/donmai-me/WannaCRI
            "wannacri",
            "extractusm",
            path,
            "--key",
            "9170825592834449000",  # random key for unknown game
        ]
    )


def ivf2mp4(pair: tuple[str, str]):
    chart_id, video_dir = pair

    ivf_file = list(filter(lambda f: f.endswith(".ivf"), listdir(video_dir)))
    if len(ivf_file) == 1:
        ivf_file = ivf_file.pop()
    else:
        return
    ivf_path = Path(video_dir) / ivf_file
    output_file = f"{chart_id}.mp4"

    if Path(output_file).exists():
        return

    subprocess.run(
        [
            "ffmpeg",
            "-i",
            ivf_path,
            "-c",
            "copy",
            output_file,
        ]
    )


def main():
    N = cpu_count()

    for i in range(N):
        makedirs(f"split_{i}", exist_ok=True)
    for chunk in batched(
        (file for file in listdir(".") if file.endswith(".dat")),
        N,
    ):
        for i, file in enumerate(chunk):
            rename(file, f"split_{i}/{file}")

    with Pool() as pool:
        pool.map(dat2ivf, range(N))
        pool.map(
            ivf2mp4,
            (
                (
                    folder.removesuffix(".dat"),
                    Path("output") / folder / "videos",
                )
                for folder in listdir("output")
                if Path(folder).is_dir()
            ),
        )


if __name__ == "__main__":
    main()
