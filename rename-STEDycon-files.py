'''
This little program should - with a little user input - take the files of a multiposition STEDycon time-lapse
and rename them according to user input - position naming
'''


import os
from tkinter import filedialog
import shutil


def main():
    positions = int(input("Number of positions recorded: "))
    root_path = filedialog.askdirectory()  #prompts user to choose directory. From tkinter
    result_path = os.path.join(root_path, 'renamed')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    filenames = [filename for filename in sorted(os.listdir(root_path)) if filename.endswith(".obf")]
    print(filenames)

    for timepoint in range(len(filenames)//positions):
        for position in range(positions):
            filename = filenames[timepoint]
            input_file = os.path.join(root_path, filename)
            output_file = os.path.join(result_path, filename[8:-4] + "_pos" + str(position+1) + "_t" + str(timepoint) + '.obf')
            print(output_file)
            shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()