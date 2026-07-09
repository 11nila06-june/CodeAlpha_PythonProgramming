import os
import shutil

print("===== Task Automation =====")

source_folder = input("Enter Source Folder Path: ")
destination_folder = input("Enter Destination Folder Path: ")

if not os.path.exists(source_folder):
    print("Source folder does not exist!")
    exit()

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files_moved = 0

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        files_moved += 1
        print(f"Moved: {file}")

print("\nTask Completed Successfully!")
print("Total JPG files moved:", files_moved)
