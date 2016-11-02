# -*- coding: utf-8 -*-

"""
centi.sentiment
~~~~~~~~~~~~~~~
This module contains the methods for converting words into sentiment tuples
"""

import corpus

def get_sentiment(word):
    """Creates sentiment and modifier tuple for a word
    Sentiment can be positive (1), neutral (0) or negative (-1)
    Modifier can be pos (P), neg (N), invert (¬) or no modifier (=)
    """
    
    if word in corpus.positive:
        sentiment = 1
    elif word in corpus.negative:
        sentiment = -1
    else:
        sentiment = 0
    
    if word in corpus.reverse:
        modifier = '¬'
    else:
        modifier = '='
    
    return (sentiment, modifier)
