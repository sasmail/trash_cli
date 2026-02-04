from pathlib import Path

def create_directory_structure():
    trash_dir = Path.home() / ".local/share/trash-cli/"
    trash_dir.mkdir(parents=True, exist_ok=True)

    files_path = Path(trash_dir) / "files"
    info_path = Path(trash_dir) / "info"

    files_path.mkdir(parents=True, exist_ok=True)
    info_path.mkdir(parents=True, exist_ok=True)

    return files_path, info_path