import re
from constants import SENTENCE_TEMPLATE, ABBREVIATIONS, END_ABBREVIATIONS, INITIALS_TEMPLATE


def get_statistics(file_directory: str):
    text = read_text(file_directory)
    statistics = {"Sentences amount: ": get_sentences_amount(text)}
    return statistics


def get_sentences_amount(text: str):
    result = len(re.findall(SENTENCE_TEMPLATE, text))
    for abbr in ABBREVIATIONS:
        result -= text.count(abbr)
    result -= len(re.findall(END_ABBREVIATIONS, text))
    result -= len(re.findall(INITIALS_TEMPLATE, text))
    return result


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
