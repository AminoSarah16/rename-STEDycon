'''
This little program should - with a little user input - take the files of a multiposition STEDycon time-lapse
and rename them according to user input - position naming
'''


import os
from tkinter import filedialog
import shutil


def main():
    root_path = filedialog.askdirectory()  #prompts user to choose directory. From tkinter
    positions = int(input("Number of positions recorded: "))
    result_path = os.path.join(root_path, 'renamed')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    filenames = [filename for filename in sorted(os.listdir(root_path)) if filename.endswith(".obf")]
    print(filenames)

    for timepoint in range(1, len(filenames)//positions+1):
        for position in range(positions):
            filename = filenames[position*timepoint]
            input_file = os.path.join(root_path, filename)
            output_file = os.path.join(result_path, filename[8:-4] + "_pos" + str(position+1) + "_t" + str(timepoint) + '.obf')
            print(input_file)
            print(output_file)
            # shutil.copyfile(input_file, output_file)


if __name__ == '__main__':
    main()