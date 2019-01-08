"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    #os.mkdir('temp')
    #os.mkdirs('doc', 'docx', 'png', 'gif', 'txt', 'xls', 'xlsx', 'jpg')


    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)
    for filename in os.chdir("/Desktop/JCU Folder/March 2018/CP1404/CP1404 Practicals/prac_09/FilesToSort"):
        if filename.endswith('.doc'):
            shutil.move(filename, 'doc/' + new_name)
        if filename.endswith('.docx'):
            shutil.move(filename, 'docx/' + new_name)
        if filename.endswith('.png'):
            shutil.move(filename, 'png/' + new_name)
        if filename.endswith('.gif'):
            shutil.move(filename, 'gif/' + new_name)
        if filename.endswith('.txt'):
            shutil.move(filename, 'txt/' + new_name)
        if filename.endswith('.xls'):
            shutil.move(filename, 'xls/' + new_name)
        if filename.endswith('.xlsx'):
            shutil.move(filename, 'xlsx/' + new_name)
        if filename.endswith('.jpg'):
            shutil.move(filename, 'jpg/' + new_name)
    # Process all subdirectories using os.walk()
    os.chdir('..')  # '..' means to go 'up' one directory
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: change into the directory and print the current working directory
        # then change back to the lyrics_path
        # Note: if you get this wrong, walk will stop short,
        # so you need to check it still walks through all subdirectories

        # TODO: add a loop (in between directory changes) to rename the files


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()