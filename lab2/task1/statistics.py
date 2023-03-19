import re
from constants import SENTENCE_TEMPLATE, ABBREVIATIONS, END_ABBREVIATIONS, INITIALS_TEMPLATE, NON_DECLARATIVE_TEMPLATE,\
    WORD_TEMPLATE, NUMBER_TEMPLATE


def get_statistics(file_directory: str):
    text = read_text(file_directory)
    statistics = {"Sentences amount: ": get_sentences_amount(text),
                  "Non-declarative sentences amount: ": get_non_declarative_amount(text),
                  "Average length of the sentence: ": get_sentences_length(text)}
    return statistics


def get_sentences_amount(text: str):
    result = len(re.findall(SENTENCE_TEMPLATE, text))
    for abbr in ABBREVIATIONS:
        result -= text.count(abbr)
    result -= len(re.findall(END_ABBREVIATIONS, text))
    result -= len(re.findall(INITIALS_TEMPLATE, text))
    return result


def get_non_declarative_amount(text: str):
    return len(re.findall(NON_DECLARATIVE_TEMPLATE, text))


def get_sentences_length(text: str):
    words_len = 0
    for word in re.findall(WORD_TEMPLATE, text):
        words_len += len(word)
    for num in re.findall(NUMBER_TEMPLATE, text):
        words_len -= len(num)
    return words_len / get_sentences_amount(text)


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
