from collections import defaultdict
from pathlib import Path
import subprocess

from os import listdir, makedirs, rename

exe = Path(__file__).parent / "vgmstream" / "vgmstream-cli.exe"


def process_vo_folder(vo_folder: str | Path):
    if not str(vo_folder).startswith("Voice_"):
        return

    vo_folder = Path(vo_folder)
    if not vo_folder.is_dir():
        return

    args = [
        exe,
        f"{vo_folder}.awb",
        "-S",
        "0",
    ]

    print(f"Processing: {vo_folder}")

    captured = subprocess.run(
        args,
        cwd=vo_folder,
        stdout=subprocess.PIPE,
    )
    out = captured.stdout.decode("utf-8")

    vo_name_count: dict[str, int] = defaultdict(int)
    state: str = "idle"
    for line in out.split("\n"):
        # trim CR
        line = line.strip()

        if not line.startswith("stream ") or line.startswith("stream total samples"):
            continue
        match state:
            case "idle":
                if line.startswith("stream count: "):
                    state = "ready"
                else:
                    print(f"parse error: {line}")
                    break
            case "ready":
                try:
                    _, stream_index = line.split("stream index: ", maxsplit=1)
                    state = "wait_name"
                except:
                    print(f"parse error: {line}")
                    raise
            case "wait_name":
                try:
                    _, stream_name = line.split("stream name: ", maxsplit=1)

                    stream_name = stream_name.split(";")[0]

                    vo_name_count[stream_name] += 1
                    count = vo_name_count[stream_name]

                    file_path = vo_folder / f"{vo_folder}.awb#{stream_index}.wav"
                    normalized_name = f"{stream_name}_{count}.wav"
                    rename(file_path, file_path.with_name(normalized_name))

                    state = "idle"
                except:
                    print(f"parse error: {line}")
                    raise


def main():
    files = listdir(".")

    for acb_file in files:
        if not acb_file.startswith("Voice_"):
            continue
        if not Path(acb_file).is_file():
            continue
        if not acb_file.endswith(".acb"):
            continue
        awb_file = Path(acb_file.replace(".acb", ".awb"))
        if not awb_file.exists():
            continue

        folder = acb_file.split(".acb")[0]
        makedirs(folder, exist_ok=True)

        acb_file_path = Path(folder) / acb_file
        awb_file_path = Path(folder) / awb_file

        rename(acb_file, acb_file_path)
        rename(awb_file, awb_file_path)

    folders = listdir(".")
    for vo_folder in folders:
        process_vo_folder(vo_folder)


if __name__ == "__main__":
    main()
