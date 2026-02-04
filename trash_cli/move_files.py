import os
import shutil
from pathlib import Path
from config import create_directory_structure
from storage import generate_unique_filename
from datetime import datetime



def move_file_to_trash(file):
    files_path, info_path = create_directory_structure()
    new_file_name, new_file_path, time_stamp = generate_unique_filename(file)

    # renaming file to bear time_stamp
    file_parent = new_file_path.parent
    time_stamped_file_path = file_parent / new_file_name
    new_file_path.rename(time_stamped_file_path)

    # moving file to be deleted to trash folder
    shutil.move(time_stamped_file_path, files_path)

    # setting up info_file
    formatted_time = datetime.strptime(time_stamp, "%Y%m%d%H%M%S%f")
    info_time = formatted_time.strftime('%Y-%m-%dT%H:%M:%S')
    new_file_name_no_suffix = os.path.splitext(new_file_name)[0]

    # writing info file
    info_file = open(f"{new_file_name_no_suffix}.trashinfo", "w")
    info_file.write(f"[Trash Info]\nPath={new_file_path}\nDeletionDate={info_time}")
    info_file.close()
    temp_info_file_path = Path(info_file.name).resolve()
    shutil.move(temp_info_file_path, info_path)

# move_file_to_trash("/Users/sascha/PycharmProjects/LearningPython/03_Python_Basics/trash_cli/sample_file_1.txt")
move_file_to_trash("/Users/sascha/PycharmProjects/LearningPython/03_Python_Basics/trash_cli/sample_file_2.txt")
move_file_to_trash("/Users/sascha/PycharmProjects/LearningPython/03_Python_Basics/trash_cli/sample_file_3.txt")

# Call generate_unique_filename ONCE
# Get: new_name, original_path, timestamp

# Move original file to: files_path / new_name

# Create .trashinfo at: info_path / (new_name + ".trashinfo")
# Write: original path and timestamp to .trashinfo


