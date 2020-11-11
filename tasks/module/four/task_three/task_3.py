import os
import shutil
import pyinputplus as pyip

"""
Code responsible for finding specified files in folder 'files' and coping them to provided destination
"""

INPUT_FOLDER = "./files"
print("Please provide extension of files which would you like to copy")

file_extension_to_copy = pyip.inputStr()

print("Please provide destination folder name.")
print("Remember folder will be created inside repository under module/four/task_three if does not exist")
destination = pyip.inputStr()
if not os.path.exists(f'./{destination}'):
    os.mkdir(destination)

for dirpath, dirnames, files in os.walk(INPUT_FOLDER):
    for file in files:
        if file.endswith(file_extension_to_copy):
            shutil.copy2(os.path.join(dirpath, file), destination)
