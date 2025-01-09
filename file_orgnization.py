import os
import shutil
path = input("Enter path: ")
if not os.path.exists(path):
    print(f"The directory '{path}' does not exist.")
else:
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            filename, extension = os.path.splitext(file)
            extension = extension[1:].lower()
            if not extension:
                continue
            extension_folder = os.path.join(path, extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
            shutil.move(file_path, os.path.join(extension_folder, file))
            print(f"Moved {file} to {extension_folder}")