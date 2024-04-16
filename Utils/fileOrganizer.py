import os
import shutil

def take_input():
    directory = input("Enter the directory to organize: ")
    return directory

def organize_files_by_suffix(directory):
    # Iterate over all the files in the directory
    for filename in os.listdir(directory):
        # Get the file suffix (assuming it's the part after the last underscore)
        suffix = filename.rsplit('.',2)[-2]
        
        # If the subdirectory doesn't exist, create it
        if not os.path.exists(os.path.join(directory, suffix)):
            os.makedirs(os.path.join(directory, suffix))
        
        # Move the file to the subdirectory
        shutil.move(os.path.join(directory, filename), os.path.join(directory, suffix, filename))

def main():
    directory = take_input()
    directory = directory.replace("\\", f"\\")
    organize_files_by_suffix(directory)

if __name__ == "__main__":
    main()
    

