'''
This little program should take as input some files and rename them according to user input.
User needs to choose the resprective folder and input the changes.
Göttingen, 9.9.20 Sarah Vanessa Schweighofer
'''


import os
from tkinter import filedialog
import shutil

##this is the only thing to be changed:
REPLACE = 'LI32_spl1_CRISPR4.1_U2OS-wt_g2clone2_Snap-OMP25_Snap-SiR600nM_Halo-Bax-oe_Halo-Atto590-new-250nM_'
WITH = ''

def main():
    root_path = filedialog.askdirectory()  #prompts user to choose directory. From tkinter
    file_format = ".msr"
    # file_format = input("Please enter the exact file ending, eg.: .tiff .obf .msr etc.  ")
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
        new_filename = filename.replace(REPLACE, WITH)
        output_file = os.path.join(result_path, new_filename)
        print(input_file)
        print(output_file)
        shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()