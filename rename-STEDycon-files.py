'''
This little program should take as input the numbered files of a multiposition time-lapse experiment
performed at the STEDycon (mounted on a Nikon body in the life-cell imaging facility at the MPI-BPC Göttingen)
and rename them according to user input. The titel of the image should then contain position and timepoint.
User needs to choose the resprective folder and input the number of positions that were recorded.
Göttingen, 23.8.20 Sarah Vanessa Schweighofer
'''


import os
from tkinter import filedialog
import shutil


def main():
    root_path = filedialog.askdirectory()  #prompts user to choose directory. From tkinter
    file_format = ".obf"
    # file_format = input("Please enter the exact file ending, eg.: .tiff .obf .msr etc.  ")
    result_path = os.path.join(root_path, 'renamed')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    filenames = [filename for filename in sorted(os.listdir(root_path)) if filename.endswith(file_format)]
    if not filenames:  #pythonic for if a list is empty
        print("There are no files with this format.")
    print(filenames)
    positions = int(input("Please enter the number of positions (ROIs, cells, etc.) recorded:  "))
    copy_and_rename_them(filenames, positions, root_path, result_path, file_format)


def copy_and_rename_them(filenames, positions, root_path, result_path, file_format):
    counter = 0
    for timepoint in range(len(filenames)//positions):
        for position in range(positions):
            counter += 1  ##need the counter in the innermost loop so that it takes every file only once in an increasing manner.
            filename = filenames[counter-1]  # the counter is essential here. either filenames[timepoint] or filenames[position] would both only takea subset of the image files
            input_file = os.path.join(root_path, filename)
            output_file = os.path.join(result_path, filename[8:-4] + "_pos" + str(position+1) + "_t" + str(timepoint) + file_format)
            print(input_file)
            print(output_file)
            shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()