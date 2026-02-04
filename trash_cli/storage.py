from pathlib import Path
from datetime import datetime
import os

def generate_unique_filename(file):
    file_path = Path(file).resolve()

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    new_file_name = file_path.stem + "_" + time_stamp + file_path.suffix

    return new_file_name, file_path, time_stamp

def generate_info_file(new_filename):
    info_file_name = Path(new_filename).stem + ".trashinfo"

    return info_file_name

generate_unique_filename("/Users/sascha/PycharmProjects/LearningPython/03_Python_Basics/trash_cli/sample_file_1.txt")
