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

        expected_sentence_sentiment = (centi.NEGATIVE_SENTIMENT,centi.DEFAULT_MODIFIER )
        self.assertEqual(actual_sentence_sentiment.sentiment, expected_sentence_sentiment[0])

    def test_positive_sentence(self):
        negated_sentence = "I love trees."
        parsed_tree = centi.parse_sentence(negated_sentence)[0]
        actual_sentence_sentiment = centi.get_polarity(parsed_tree)

        expected_sentence_sentiment = (centi.POSITIVE_SENTIMENT,centi.DEFAULT_MODIFIER )
        self.assertEqual(actual_sentence_sentiment.sentiment, expected_sentence_sentiment[0])

    def test_negation_sentence(self):
        negated_sentence = "I do not love trees."
        parsed_tree = centi.parse_sentence(negated_sentence)[0]
        actual_sentence_sentiment = centi.get_polarity(parsed_tree)

        expected_sentence_sentiment = (centi.NEGATIVE_SENTIMENT,centi.NEUTRAL_MODIFIER )
        self.assertEqual(actual_sentence_sentiment.sentiment, expected_sentence_sentiment[0])

