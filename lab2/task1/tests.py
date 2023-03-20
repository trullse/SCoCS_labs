import unittest
from statistics import get_sentences_amount, get_non_declarative_amount, get_sentences_length, get_word_length, \
    get_top_k_ngrams


class StatisticsTests(unittest.TestCase):
    def test_sentences_count(self):
        self.assertEqual(get_sentences_amount("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                              "What should I do?!"), 3)
        self.assertEqual(get_sentences_amount("I'd like to eat some oranges, apples, bananas, etc. But neither Dr. "
                                              "Martins, nor A.A. Brown have suggested me anything of these."), 2)
        self.assertEqual(get_sentences_amount("\"What should I do?\", - asked Ann. \"Think about it!\", - answered M. "
                                              "Jane. Ann was upset and took 2 lbs. of sweets with herself."), 5)


if __name__ == '__main__':
    unittest.main()
