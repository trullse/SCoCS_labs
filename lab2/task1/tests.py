import unittest
from statistics import get_sentences_amount, get_non_declarative_amount, get_sentences_length, get_word_length, \
    get_top_k_ngrams


class StatisticsTests(unittest.TestCase):
    def test_sentences_amount(self):
        self.assertEqual(get_sentences_amount("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                              "What should I do?!"), 3)
        self.assertEqual(get_sentences_amount("I'd like to eat some oranges, apples, bananas, etc. But neither Dr. "
                                              "Martins, nor A.A. Brown have suggested me anything of these."), 2)
        self.assertEqual(get_sentences_amount("\"What should I do?\", - asked Ann. \"Think about it!\", - answered M. "
                                              "Jane. Ann was upset and took 2 lbs. of sweets with herself."), 5)

    def test_non_declarative_amount(self):
        self.assertEqual(get_non_declarative_amount("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                                    "What should I do?!"), 1)
        self.assertEqual(get_non_declarative_amount("It's not fair! Tell me the truth! Or you are not ready, don't "
                                                    "you?"), 3)
        self.assertEqual(get_non_declarative_amount("It's true... But it means nothing! It's a witness!"), 2)

    def test_sentence_length(self):
        self.assertAlmostEqual(get_sentences_length("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                                    "What should I do?!"), 19.66667, delta=1e-5)
        self.assertAlmostEqual(get_sentences_length("I'd like to eat some oranges, apples, bananas, etc. But neither "
                                                    "Dr. Martins, nor A.A. Brown have suggested me anything of these."),
                               49, delta=1e-5)
        self.assertAlmostEqual(get_sentences_length("\"What should I do?\", - asked Ann. \"Think about it!\", - "
                                                    "answered M. Jane. Ann was upset and took 2 lbs. of sweets with "
                                                    "herself."), 17.2, delta=1e-5)

    def test_word_length(self):
        self.assertAlmostEqual(get_word_length("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                               "What should I do?!"), 3.27778, delta=1e-5)
        self.assertAlmostEqual(get_word_length("I'd like to eat some oranges, apples, bananas, etc. But neither Dr. "
                                               "Martins, nor A.A. Brown have suggested me anything of these."), 4.26087,
                               delta=1e-5)
        self.assertAlmostEqual(get_word_length("\"What should I do?\", - asked Ann. \"Think about it!\", - "
                                               "answered M. Jane. Ann was upset and took 2 lbs. of sweets with "
                                               "herself."), 3.90909, delta=1e-5)

    def test_top_k_ngrams(self):
        self.assertEqual(get_top_k_ngrams("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                          "What should I do?!", 3, 4), [(" the", 2), ("ther", 2), ("here", 2)])
        self.assertEqual(get_top_k_ngrams("Once upon a time I was there. There were no Mr. and Mrs. Smith. "
                                          "What should I do?!", 3, 1), [(" ", 17), ("e", 8), ("o", 5)])
        self.assertEqual(get_top_k_ngrams("Sometimes somebody can tell anybody anything", 3, 4),
                         [("some", 2), ("body", 2), ("ody ", 2)])


if __name__ == '__main__':
    unittest.main()
