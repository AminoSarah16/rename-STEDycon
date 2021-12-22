'''
This little program should take as input .obf files and rename them with pos+num according to acquisition time.
User needs to choose the respective folder and input the changes.
Göttingen, July 2021, Sarah Vanessa Schweighofer
'''


import os
from tkinter import filedialog
import shutil

# prompts user to say what to replace (the number at the beginning is removed automatically, just if yuo also want to remove stuff at the end):
REPLACE = str(input('Please enter the part (loop-pos or similar) you want to have replaced exactly as it appears in the filename (best copy-paste!): '))
WITH = ''

def main():
    # prompts user to choose directory. From tkinter
    root_path = filedialog.askdirectory()
    file_format = ".obf"
    # file_format = input("Please enter the exact file ending, eg.: .tiff .obf .msr etc.  ")
    result_path = os.path.join(root_path, 'renamed')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)

    # now filter for and sort the wanted files:
    # you can give the sorted function a key value which lets you choose what to sort for
    # in my case this is the
    # !!!!date of modification (i.e. acquiisition)!!!!
    # to make sure the loop files are in the correct order
    # the lambda function is needed to pass the reuslt of the getmtime function as an object to the sorted function
    # Jan-Niklas says in most cases when you have a function within brackets, it's a lambda function
    filenames = [filename for filename in sorted(os.listdir(root_path), key=lambda x: os.path.getmtime(os.path.join(root_path, x))) if filename.endswith(file_format)]
    if not filenames:  #pythonic for if a list is empty
        print("There are no files with this format.")
    print(filenames)
    copy_and_rename_them(filenames, root_path, result_path)


def copy_and_rename_them(filenames, root_path, result_path):
    pos_num = 0
    for filename in filenames:
        pos_num += 1
        input_file = os.path.join(root_path, filename)
        # cuts out the automatic number in front (78 characters) and the .obf in the back
        new_filename = filename[8:-4].replace(REPLACE, WITH)
        output_file = os.path.join(result_path, new_filename + "pos" + str(pos_num).zfill(2)+ ".obf") #zfill fills up zeros
        print(input_file)
        print(output_file)
        shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()