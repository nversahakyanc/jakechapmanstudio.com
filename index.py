import os

def rename_jpg_files(directory):
    """
    Renames all jpg files in the specified directory by removing '#-' prefix if present.
    
    Args:
        directory (str): Path to the directory containing jpg files
    """
    # Get all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an jpg file
        if filename.lower().endswith('.jpg'):
            # Check if the filename starts with '#-'
            if filename.startswith('# '):
                # Create new filename by removing the first 2 characters (#-)
                new_filename = filename[2:]
                
                # Construct full paths
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')
            else:
                print(f'Skipped: {filename} (does not start with "#-")')

# Example usage:
if __name__ == "__main__":
    # Use raw string for Windows paths or double backslashes
    directory_path = r"C:\Users\Lenovo\OneDrive\Desktop\laspalmas88.com\jakechapmanstudio.com"
    
    # Verify directory exists
    if os.path.isdir(directory_path):
        rename_jpg_files(directory_path)
        print("File renaming complete!")
    else:
        print(f"Error: Directory not found - {directory_path}")