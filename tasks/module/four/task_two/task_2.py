"""
    Implementation of Task 2 from module four
"""

import os
import re

FILE_PREFIX = 'spam'
FILE_EXTENSION = '.txt'
SPAM_PATH = './spam'


def get_and_sort_list_of_numbers_from_gathered_files(files):
    """
        Method responsible for extracting and sorting numbers gathered from provided list of files.
    """
    list_of_numbers = []
    for file in files:
        list_of_numbers.append(int(re.search(r'\d+', file).group(0)))
    list_of_numbers.sort()
    return list_of_numbers


def detect_missing_files(list_of_numbers):
    """
        Method responsible for dececting missing numbers in provided list
    """
    first = list_of_numbers[0]
    last = list_of_numbers[len(list_of_numbers) - 1]
    files_to_add = []
    while first + 1 < last:
        first += 1
        files_to_add.append(first)
    return files_to_add


def create_missing_files(files_to_create):
    """
        Method responsible for creating missing files and adding them to location precised by SPAM_PATH
    """
    for file_number in files_to_create:
        number_as_string = str(file_number)
        if len(number_as_string) < 3:
            number_as_string = number_as_string.zfill(3)
        full_file_name = FILE_PREFIX + number_as_string + FILE_EXTENSION
        if not os.path.isfile(SPAM_PATH + full_file_name):
            open(os.path.join(SPAM_PATH, full_file_name), 'wb')


def add_missing_files():
    """
        Method responsible populating list of spam with missing files
        IMPORTANT path is defined by default as SPAM_PATH.
    """
    spam_files = os.listdir(SPAM_PATH)
    if not spam_files:
        raise FileNotFoundError("Given path is not working")

    list_of_numbers = get_and_sort_list_of_numbers_from_gathered_files(spam_files)
    files_to_create = detect_missing_files(list_of_numbers)
    create_missing_files(files_to_create)


def main():
    """
        Main function which results with filling gaps between files basing on numeration
    """
    add_missing_files()


if __name__ == "__main__":
    main()
