import re
from datetime import datetime
import pyinputplus as pyip


EXTENSION = 'txt'
BASIC_FILE = 'Sentences.txt'
PART_OF_SPEECH = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


def replace_given_part_of_speech(part: str, sentence: str):
    """
        Method responsible for replacing first occurrence of specific part of speech with proposed word.
    """
    print(f"Enter a {part.lower()}: ")
    new_word = pyip.inputStr()
    return sentence.replace(part, new_word, 1)


def replace_parts_of_speech_in_text():
    """
        Method responsible for replacing parts of speech from "Sentence.txt" file with words proposed by user.
    """
    file_text = open(BASIC_FILE, 'r').read()

    for word in re.findall(r'[A-Za-z]+|\S', file_text):
        if word in PART_OF_SPEECH:
            file_text = replace_given_part_of_speech(word, file_text)
    return file_text


def save_new_text_to_new_file(text: str):
    """
        Method responsible for generating new txt file and saving given text to it.
    """
    print("New sentence is: " + text)
    current_time = datetime.now()
    file_name = str(f'{current_time.hour}{current_time.minute}{current_time.second}.{EXTENSION}')
    new_file = open(file_name, "w+")
    new_file.write(text)
    new_file.close()


if __name__ == "__main__":
    new_text = replace_parts_of_speech_in_text()
    save_new_text_to_new_file(new_text)
