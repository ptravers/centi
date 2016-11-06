# -*- coding: utf-8 -*-

"""
centi.sentiment
~~~~~~~~~~~~~~~
This module contains the methods for converting words into sentiment tuples
"""

import corpus
from .constants import *

def get_sentiment(word):
    """Creates sentiment and modifier tuple for a word
    Sentiment can be positive, neutral or negative
    Modifier can be pos, neg, invert or no modifier
    """

    if word in corpus.positive:
        sentiment = POSITIVE_SENTIMENT
    elif word in corpus.negative:
        sentiment = NEGATIVE_SENTIMENT
    else:
        sentiment = NEUTRAL_SENTIMENT

    if word in corpus.reverse:
        modifier = REVERSE_MODIFIER
    else:
        modifier = DEFAULT_MODIFIER

    return (sentiment, modifier)
