import os

def remove_identifier_files(directory):
    removed_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.Identifier'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")
    
    print(f"Total files removed: {removed_count}")


remove_identifier_files(".")