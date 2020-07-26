import os
import shutil
import pyinputplus as pyip


def find_chosen_file_in_files_folder_location_and_copy_it_to_defined_location():
    """
    Method responsible for finding specifiied file in folder 'files' and coping it to provided destination
    """
    print("Please provide correct file name. Remember file must be inside repository in folder named 'files'")
    print("IMPORTANT! provide file name along with extension")

    file_to_copy = pyip.inputStr()
    if not os.path.exists(f'./files/{file_to_copy}'):
        raise FileNotFoundError("Provided file name does not exist")

    print("Please provide destination folder name.")
    print("Remember folder will be created inside repository under module/four/task_three if does not exist")

    destination = pyip.inputStr()
    if not os.path.exists(f'./{destination}'):
        os.mkdir(destination)

    shutil.copy2(f'files/{file_to_copy}', destination)


def main():
    find_chosen_file_in_files_folder_location_and_copy_it_to_defined_location()


if __name__ == "__main__":
    main()
