import os
import shutil
import subprocess
import zipfile
script_dir = os.path.dirname(os.path.abspath(__file__))
def get_game_name():
    # Function to get the game name from project.godot
    with open("project.godot", "r") as f:
        for line in f:
            if line.strip().startswith("config/name"):
                return line.split("=")[1].strip(' "\n')
def compress_files_to_zip():
    print_compression_info()
    # Directory containing the files you want to compress
    source_dir = os.path.join(script_dir, "exports/web")
    try:
        # Create a ZIP file in write mode
        with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the source directory and its subdirectories
            for foldername, subfolders, filenames in os.walk(source_dir):
                for filename in filenames:
                    # Get the full path of the file
                    file_path = os.path.join(foldername, filename)
                    # Add the file to the ZIP archive with its relative path
                    zipf.write(file_path, os.path.relpath(file_path, source_dir))
        
        print(f'Files compressed to "{zip_filepath}" successfully!')
    except Exception as e:
        print(f'Error: {e}')

def print_compression_info():
    # Print information about the source directory

    # Get the list of files to be compressed
    files_to_compress = []
    for foldername, _, filenames in os.walk(source_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            files_to_compress.append(file_path)

    # Print the list of files to be compressed
    print("\nFiles to be Compressed:")
    for file_path in files_to_compress:
        print(file_path)

    # Print the name of the ZIP file to be created
    print(f"\nZIP File to be Created: {get_game_name()}_{export_preset}.zip\n")

def get_current_branch():
    # Function to get the current Git branch
    try:
        result = subprocess.check_output(["git", "symbolic-ref", "--short", "HEAD"], universal_newlines=True).strip()
        return result
    except subprocess.CalledProcessError:
        return None

def export_to_itchio():
    # Main export function
    target_branch = "production"
    itchio_user = "mittomrum"

    current_branch = get_current_branch()

    if current_branch != target_branch:
        print(f"Not on the '{target_branch}' branch. Skipping build.")
        print(f"Current branch: '{current_branch}'")
        input("Press Enter to exit...")
        exit(1)
    else:
        print(f"Current branch: '{current_branch}'")

    game_name = get_game_name()

    if game_name is None:
        print("Failed to get the game name from project.godot.")
        input("Press Enter to exit...")
        exit(1)

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the project path based on the script directory
    itchio_credentials = f"{itchio_user}/{game_name}:html5"

    print("Exporting project to itch.io...")

    try:
        output_bytes = subprocess.check_output(["butler", "push", os.path.join(script_dir, "exports"), itchio_credentials])
        output_text = output_bytes.decode('utf-8')
        print(output_text)
        print("Export successful.")

        output_bytes = subprocess.check_output(["butler", "status", itchio_credentials])
        output_text = output_bytes.decode('utf-8')
        print(output_text)

    except subprocess.CalledProcessError as e:
        print(f"Export failed with error: {e}")
        print(f"Command output:\n{e.output.decode('utf-8')}")
        input("Press Enter to exit...")
        exit(1)

    input("Press Enter to exit...")

    # Compress files to ZIP
    print("Compressing files to ZIP...")
    compress_files_to_zip()



itchio_user = "mittomrum"
export_preset = "Web"  # Change this to your desired export preset
source_dir = os.path.join(script_dir, "exports\\web")
zip_dir = os.path.join(script_dir, "exports") # where the zip should be saved
zip_filepath = os.path.join(zip_dir, f"{get_game_name()}_{export_preset}.zip")

print(f"Game Name: {get_game_name()}")
print(f"itch.io User: {itchio_user}")
print(f"Export Preset: {export_preset}")
print(f"Zip Directory: {zip_dir}")

print("Compressing files to ZIP...")
compress_files_to_zip()
export_to_itchio()


# run the line `butler status mittomrum/Popington:html5` to check the status of the game on itch.io

input("Press Enter to exit...")


