import os
import shutil
import subprocess

def prepare_source_files(src_folders, dst_folder="src"):
    """
    Copies files from each directory in src_folders to dst_folder.

    :param src_folders: List of source directories.
    :param dst_folder: Destination directory.

    """
    # Create destination directory if it doesn't exist
    os.makedirs(dst_folder, exist_ok=True)

    for src_folder in src_folders:
        # Obtain the list of filenames in source directory
        filenames = os.listdir(src_folder)

        # Copy each file except .gitignore and poetry.lock
        for filename in filenames:
            if filename not in [".gitignore", "dist", "poetry.lock"]:
                src_filepath = os.path.join(src_folder, filename)
                if os.path.isfile(src_filepath):
                    shutil.copy2(src_filepath, dst_folder)

def build_project():
    """
    Executes 'poetry build' in a subprocess.

    """
    subprocess.check_call(["poetry", "build"])

# Define your source folders here.
# For example: ["folder1", "folder2"]
SOURCE_FOLDERS = ["."]

prepare_source_files(SOURCE_FOLDERS)
build_project()

# After build, remove the src folder
shutil.rmtree("src")