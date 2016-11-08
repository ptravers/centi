import unittest
import centi

class TestTemplate(unittest.TestCase):

    def test_neutral_sentence(self):
        sentence = "This is a thing."
        parsed_tree = centi.parse_sentence(sentence)[0]
        actual_sentence_sentiment = centi.get_polarity(parsed_tree)

        expected_sentence_sentiment = (centi.NEUTRAL_SENTIMENT, centi.DEFAULT_MODIFIER)
        self.assertEqual(actual_sentence_sentiment.sentiment, expected_sentence_sentiment[0])

    def test_negative_sentence(self):
        negated_sentence = "I hate trees."
        parsed_tree = centi.parse_sentence(negated_sentence)[0]
        actual_sentence_sentiment = centi.get_polarity(parsed_tree)

        expected_sentence_sentiment = (centi.NEGATIVE_SENTIMENT,centi.REVERSE_MODIFIER )
        self.assertEqual(actual_sentence_sentiment.sentiment, expected_sentence_sentiment[0])

