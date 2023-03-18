import re
from constants import SENTENCE_TEMPLATE, ABBREVIATIONS, END_ABBREVIATIONS


def get_statistics(file_directory: str):
    text = read_text(file_directory)
    statistics = {"Sentences amount: ": get_sentences_amount(text)}
    return statistics


def get_sentences_amount(text: str):
    result = len(re.findall(SENTENCE_TEMPLATE, text))
    for abbr in ABBREVIATIONS:
        result -= text.count(abbr)
    for abbr in END_ABBREVIATIONS:
        abbr += r"\s+[^A-Z]"
        result -= len(re.findall(abbr, text))

    return result


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
