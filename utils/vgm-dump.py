from pathlib import Path
import subprocess

from os import listdir, makedirs, rename

exe = Path(__file__).parent / "vgmstream" / "vgmstream-cli.exe"


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
        if not vo_folder.startswith("Voice_"):
            continue

        vo_folder = Path(vo_folder)
        if not vo_folder.is_dir():
            continue

        args = [
            exe,
            f"{vo_folder}.awb",
            "-S",
            "0",
        ]

        subprocess.run(
            args,
            cwd=vo_folder,
        )


if __name__ == "__main__":
    main()
