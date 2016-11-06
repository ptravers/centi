# -*- coding: utf-8 -*-

"""
centi.sentiment
~~~~~~~~~~~~~~~
This module contains the methods for converting words into sentiment tuples
"""

import corpus
from .constants import modifier_reverse, modifier_default, neutral, positive, negative

def get_sentiment(word):
    """Creates sentiment and modifier tuple for a word
    Sentiment can be positive (1), neutral (0) or negative (-1)
    Modifier can be pos (P), neg (N), invert (¬) or no modifier (=)
    """

    if word in corpus.positive:
        sentiment = positive
    elif word in corpus.negative:
        sentiment = negative
    else:
        sentiment = neutral

    if word in corpus.reverse:
        modifier = modifier_reverse
    else:
        modifier = modifier_default

    return (sentiment, modifier)
