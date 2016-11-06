# -*- coding: utf-8 -*-

"""
centi.sentiment
~~~~~~~~~~~~~~~
This module contains the methods for converting words into sentiment tuples
"""

import corpus
from .constants import *

def get_sentiment(word):
    """Returns whether word is positive, neutral, or negative
    """

    if word in corpus.positive:
        return POSITIVE_SENTIMENT
    elif word in corpus.negative:
        return NEGATIVE_SENTIMENT
    else:
        return NEUTRAL_SENTIMENT

def get_modifier(word):
    """Returns whether a word has special sentiment modifying properties
    """
    if word in corpus.reverse:
        return REVERSE_MODIFIER
    else:
        return DEFAULT_MODIFIER
