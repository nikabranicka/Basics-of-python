"""
    Implementation of Task 2 from module four
"""

import os
import re

FILE_PREFIX = 'spam'
FILE_EXTENSION = '.txt'
SPAM_PATH = './spam/'


def close_gaps():
    """
        Method responsible for detecting gaps between spam files and closing them
    """
    spam_files = os.listdir(SPAM_PATH)
    if not spam_files:
        raise FileNotFoundError("Given path is not working")

    list_of_file_names = []
    for file in spam_files:
        list_of_file_names.append(file)
    list_of_file_names.sort()

    for index, file_name in enumerate(list_of_file_names, start=1):
        number_as_string = str(index)
        number_as_string = number_as_string.zfill(3)
        new_file_name = FILE_PREFIX + number_as_string + FILE_EXTENSION
        os.rename(SPAM_PATH + file_name, SPAM_PATH + new_file_name)


if __name__ == "__main__":
    close_gaps()
