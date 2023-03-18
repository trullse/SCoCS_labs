import re
from constants import SENTENCE_TEMPLATE, ABBREVIATIONS


def get_statistics(file_directory: str):
    text = read_text(file_directory)
    statistics = {"Sentences amount: ": get_sentences_amount(text)}
    return statistics


def get_sentences_amount(text: str):
    result = re.findall(SENTENCE_TEMPLATE, text)
    res_count = len(result)
    for abbr in ABBREVIATIONS:
        res_count -= text.count(abbr)
    return res_count


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
