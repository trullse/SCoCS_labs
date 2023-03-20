from statistics import get_sentences_amount, get_non_declarative_amount, get_sentences_length, get_word_length, \
    get_top_k_ngrams, read_text
from constants import FILE_DIRECTORY


def main():
    continue_request = True
    while continue_request:
        if input("Do you want to write a text or to read it from test_text.txt? w/r ") == "w":
            text = input("Print your text below: \n")
        else:
            print("You've chosen to read test_text.txt")
            text = read_text(FILE_DIRECTORY)
        correct_input = False
        if input("Do you want to enter K, N to find top-K repeated N-grams? y/n ") == "y":
            while not correct_input:
                try:
                    k = int(input("Enter K to find top-K repeated N-grams: "))
                    n = int(input("Enter N to find top-K repeated N-grams: "))
                    correct_input = True
                except ValueError:
                    print("Incorrect input! Try again.")
        else:
            k = 10
            n = 4
            print("Variables were set to default settings: K = 10, N = 4")
        print("\nSTATISTICS OF THE TEXT\n"
              "Sentences amount: {}\n"
              "Non-declarative sentences amount: {}\n"
              "Average length of the sentence (in characters): {}\n"
              "Average length of the word (in characters): {}".format(get_sentences_amount(text),
                                                                      get_non_declarative_amount(text),
                                                                      get_sentences_length(text),
                                                                      get_word_length(text)))
        top_ngrams = get_top_k_ngrams(text, k, n)
        not_repeated = 0
        for ngram in top_ngrams:
            if ngram[1] == 1:
                not_repeated += 1
        if not_repeated > 0 or len(top_ngrams) == 0:
            print("There are no {} repeated {}-grams in the text.".format(k, n))
            top_ngrams = top_ngrams[:k - not_repeated]
        if not_repeated != k and len(top_ngrams) != 0:
            print("Here are top-{} repeated {}-grams:".format(k - not_repeated, n))
            for ngram in top_ngrams:
                print("{}: {:5d} times".format(ngram[0], ngram[1]))
        if input("Do you want to continue? y/n: ") == "n":
            continue_request = False


if __name__ == '__main__':
    main()
