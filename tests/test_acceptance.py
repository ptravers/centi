import unittest
import centi

class TestTemplate(unittest.TestCase):

    def test_neutral_sentence(self):
        sentence = "This is a thing."
        parsed_tree = centi.parse_sentence(sentence)
        actual_sentence_sentiment = centi.get_polarity(parsed_tree)

        expected_sentence_sentiment = (centi.neutral, centi.modifier_default)
        self.assertEqual(actual_sentence_sentiment, expected_sentence_sentiment)

    def test_negated_sentence(self):
        negated_sentence = "This is not a thing."
        parsed_tree = centi.parse_sentence(negated_sentence)
        actual_sentence_sentiment = centi.get_polarity(parsed_tree)

        expected_sentence_sentiment = (centi.negative,centi.modifier_reverse )
        self.assertEqual(actual_sentence_sentiment, expected_sentence_sentiment)

