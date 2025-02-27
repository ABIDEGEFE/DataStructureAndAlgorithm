import os

# Directory containing your .txt and .py.txt files
directory = r'C:\Users\SolNet\DataStructureAndAlgorithm'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file has a .txt or .py.txt extension
    if filename.endswith('.txt') or filename.endswith('.py.txt'):
        # Create the new filename with a .py extension
        new_filename = filename.replace('.txt', '').replace('.py', '') + '.py'
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} to {new_filename}')
