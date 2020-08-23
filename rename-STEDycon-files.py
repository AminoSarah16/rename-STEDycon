'''
This little program should - with a little user input - take the files of a multiposition STEDycon time-lapse
and rename them according to user input - position naming
'''


import os
from tkinter import filedialog
import shutil


def main():
    root_path = filedialog.askdirectory()  #prompts user to choose directory. From tkinter
    file_format = input("Please enter the exact file ending, eg.: .tiff .obf .msr etc.  ")
    result_path = os.path.join(root_path, 'renamed')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    filenames = [filename for filename in sorted(os.listdir(root_path)) if filename.endswith(file_format)]
    if not filenames:
        print("There are no files with this format.")
    print(filenames)
    positions = int(input("Please enter the number of positions (ROIs, cells, etc.) recorded:  "))

    counter = 0
    for timepoint in range(len(filenames)//positions):
        for position in range(positions):
            counter += 1  ##need the counter in the innermost loop so that it takes every file only once in an increasing manner.
            print(counter)
            filename = filenames[counter-1]  # the counter is essential here. either filenames[timepoint] or filenames[position] would both only takea subset of the image files
            input_file = os.path.join(root_path, filename)
            output_file = os.path.join(result_path, filename[8:-4] + "_pos" + str(position+1) + "_t" + str(timepoint) + file_format)
            print(input_file)
            print(output_file)
            shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()