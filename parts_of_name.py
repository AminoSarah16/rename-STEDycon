'''
This little program should take as input some files and rename them according to user input.
User needs to choose the resprective folder and input the changes.
Göttingen, May 2021, Sarah Vanessa Schweighofer
'''


import os
#from tkinter import filedialog
import shutil

##these are the things to be changed:
part1_start = 0
part1_end = 5

part2_start = 15
part2_end = 17

file_format = ".fastq"
########################################


def main():
    root_path = "C:/Users/sschwei/Documents/HPC/Illumina_FH1_new-indices/data"  #prompts user to choose directory. From tkinter
    result_path = os.path.join(root_path, 'renamed')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    filenames = [filename for filename in sorted(os.listdir(root_path)) if filename.endswith(file_format)]
    if not filenames:  #pythonic for if a list is empty
        print("There are no files with this format.")
    print(filenames)
    copy_and_rename_them(filenames, root_path, result_path)


def copy_and_rename_them(filenames, root_path, result_path):
    for filename in filenames:
        input_file = os.path.join(root_path, filename)
        part1=filename[part1_start:part1_end]
        part2=filename[part2_start:part2_end]
        new_filename = part1 + '-' + part2 + file_format
        output_file = os.path.join(result_path, new_filename)
        print(input_file)
        print(output_file)
        shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()