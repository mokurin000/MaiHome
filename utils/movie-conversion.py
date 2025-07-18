import subprocess
from itertools import islice
from os import listdir, makedirs, rename
from multiprocessing import Pool


def process(i: int):
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


def batched(iterable, n: int):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def main():
    N = 20

    for i in range(N):
        makedirs(f"split_{i}", exist_ok=True)
    for chunk in batched(
        (file for file in listdir(".") if file.endswith(".dat")),
        N,
    ):
        for i, file in enumerate(chunk):
            rename(file, f"split_{i}/{file}")

    with Pool() as pool:
        pool.map(process, range(N))


if __name__ == "__main__":
    main()
