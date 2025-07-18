from multiprocessing import Pool
import subprocess
from os import listdir, path


def process(pair: tuple[str, str]):
    chart_id, video_dir = pair

    ivf_file = list(filter(lambda f: f.endswith(".ivf"), listdir(video_dir)))
    if len(ivf_file) == 1:
        ivf_file = ivf_file.pop()
    else:
        return
    ivf_path = path.join(video_dir, ivf_file)
    output_file = f"{chart_id}.mp4"

    if path.exists(output_file):
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
    with Pool() as pool:
        pool.map(
            process,
            (
                (
                    folder.removesuffix(".dat"),
                    path.join(folder, "videos"),
                )
                for folder in listdir(".")
                if path.isdir(folder)
            ),
        )


if __name__ == "__main__":
    main()
