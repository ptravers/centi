import unittest
from centi import rules,snode, constants

class TestTemplate(unittest.TestCase):

    def setUp(self):
        generic_det = snode.Snode(label = "Det", sentiment = constants.NEUTRAL_SENTIMENT, modifier = constants.DEFAULT_MODIFIER)
        generic_noun = snode.Snode(label = "NN", sentiment = constants.NEUTRAL_SENTIMENT, modifier = constants.DEFAULT_MODIFIER)
        self.test_noun_phrase = [generic_det, generic_noun]

    def test_noun_phrase_head(self):
        rules.calculate_head(self.test_noun_phrase, "NP")
        self.assertTrue(self.test_noun_phrase[1].head)
