import re
from constants import SENTENCE_TEMPLATE, ABBREVIATIONS


def get_statistics(file_directory: str):
    text = read_text(file_directory)
    statistics = {}
    result = re.findall(SENTENCE_TEMPLATE, text)
    res_count = len(result)
    for abbr in ABBREVIATIONS:
        res_count -= text.count(abbr)
    statistics["Sentences amount: "] = res_count
    return statistics


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
