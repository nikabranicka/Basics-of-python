from datetime import datetime
import pyinputplus as pyip

ADJECTIVE = 'ADJECTIVE'
NOUN = 'NOUN'
ADVERB = 'ADVERB'
VERB = 'VERB'

part_of_speech = [ADJECTIVE, NOUN, ADVERB, VERB]


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
    file_text = open("Sentences.txt", "r").read()
    for word in file_text.split():
        for key in part_of_speech:
            if key in word:
                file_text = replace_given_part_of_speech(key, file_text)
    return file_text


def save_new_text_to_new_file(new_text: str):
    """
        Method responsible for generating new txt file and saving given text to it.
    """
    print("New sentence is: " + new_text)
    file_name = str(datetime.now().hour) + '.txt'
    new_file = open(file_name, "w+")
    new_file.write(new_text)
    new_file.close()


def main():
    new_text = replace_parts_of_speech_in_text()
    save_new_text_to_new_file(new_text)


main()
