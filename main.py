import os
import shutil
from tkinter import Tk, filedialog

# Open a folder selection dialog
root = Tk()
root.withdraw()  # Hide the main window
folder = filedialog.askdirectory(title="Select the folder to organize")

if not folder:
    print("No folder selected. Exiting.")
    exit()

# Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

# Loop through files and move them to corresponding folders
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

print("Files organized successfully!")
