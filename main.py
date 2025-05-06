import os
import shutil

# Define folder where your files are
folder = "C:\Users\hp\Downloads"

# Create subfolders
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(target_folder, filename))
                break
