# -*- coding: utf-8 -*-

"""
centi.summarise
~~~~~~~~~~~~~~~
This module returns a sentiment summary for an input string
"""
from .parser    import parse_text
from .tree      import get_polarity
from .constants import *
import collections

def summarise_text(text):
    sentence_trees = parse_text(text)
    
    sentiments = collections.Counter([get_polarity(tree).sentiment for tree in sentence_trees])
    
    return {
        'sentences' : len(sentence_trees),
        'positive'  : sentiments[POSITIVE_SENTIMENT],
        'negative'  : sentiments[NEGATIVE_SENTIMENT],
        'mixed'     : sentiments[MIXED_SENTIMENT],
        'neutral'   : sentiments[NEUTRAL_SENTIMENT]
    }
