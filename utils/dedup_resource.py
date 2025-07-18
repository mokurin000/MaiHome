import os
import hashlib
from multiprocessing import Pool
from functools import reduce
from sys import stderr


DIR_A = "/path/to/A000/MovieData"
DIR_B = "/path/to/A000/MovieData"


def calculate_sha1_of_file(filepath):
    """
    Calculates the SHA-1 hash of a given file.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The hexadecimal representation of the SHA-1 hash, or None if the file is not found.
    """
    sha1_hash = hashlib.sha1()
    try:
        with open(filepath, "rb") as file:
            # Read the file in chunks to handle large files efficiently
            while True:
                chunk = file.read(4096)  # Read 4KB at a time
                if not chunk:
                    break
                sha1_hash.update(chunk)
        return sha1_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def dedup_check(filename: str):
    path_a = os.path.join(DIR_A, filename)
    path_b = os.path.join(DIR_B, filename)

    sha1_a = calculate_sha1_of_file(path_a)
    sha1_b = calculate_sha1_of_file(path_b)

    if sha1_a != sha1_b:
        print(f"[WARN] {filename}: mismatch!", file=stderr)
        return
    else:
        print(filename)

    os.remove(path_b)
    os.link(path_a, path_b)


def main():
    insecs = reduce(
        lambda a, b: a & b,
        map(set, map(os.listdir, [DIR_A, DIR_B])),
    )
    with Pool() as pool:
        pool.map(dedup_check, insecs)


if __name__ == "__main__":
    main()
