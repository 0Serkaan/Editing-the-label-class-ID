import os
import argparse

def replace_first_value_in_files(folder_path, new_value):
    # Get all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Process each file
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        # Process only .txt files
        if file_name.endswith('.txt'):
            # Open and read the file contents
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Replace the first value in the first line with the new value
            if lines:
                first_line = lines[0].strip().split()
                if first_line:
                    first_line[0] = str(int(new_value))
                    lines[0] = ' '.join(first_line) + '\n'
                
                # Update the file with the modified content
                with open(file_path, 'w') as file:
                    file.writelines(lines)

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Replace the first value in each line of text files in a folder.")
    parser.add_argument("--source", required=True, help="Path to the folder containing text files.")
    parser.add_argument("--new_value", required=True, type=float, help="New value to replace the first value with.")
    args = parser.parse_args()
    
    # Perform the operation
    replace_first_value_in_files(args.source, args.new_value)
