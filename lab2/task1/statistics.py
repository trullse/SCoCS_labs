import re
from constants import SENTENCE_TEMPLATE


def get_statistics(file_directory: str):
    text = read_text(file_directory)
    statistics = {}
    result = re.findall(SENTENCE_TEMPLATE, text)
    statistics["Sentences amount: "] = len(result)
    return statistics


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
