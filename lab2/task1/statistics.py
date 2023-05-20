import re
from constants import (SENTENCE_TEMPLATE,
                       ABBREVIATIONS,
                       END_ABBREVIATIONS,
                       INITIALS_TEMPLATE,
                       NON_DECLARATIVE_TEMPLATE,
                       WORD_TEMPLATE,
                       NUMBER_TEMPLATE,
                       NEWLINE_TEMPLATE)


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


def get_word_length(text: str):
    words_len = 0
    words = re.findall(WORD_TEMPLATE, text)
    for word in words:
        words_len += len(word)
    nums = re.findall(NUMBER_TEMPLATE, text)
    for num in nums:
        words_len -= len(num)

    return words_len / (len(words) - len(nums))


def get_top_k_ngrams(text: str, k=10, n=4):
    text = text.lower()
    text = re.sub(NEWLINE_TEMPLATE, " ", text)
    ngrams = []
    for i in range(len(text) - n + 1):
        ngrams.append(text[i:i + n])
    frequency_dictionary = count_frequency(ngrams)
    sorted_frequencies = sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=True)
    return sorted_frequencies[:k]


def count_frequency(elements):
    frequencies = {}
    for el in elements:
        frequencies[el] = frequencies.get(el, 0) + 1
    return frequencies


def read_text(file_directory: str):
    with open(file_directory, "r") as file:
        return file.read()
