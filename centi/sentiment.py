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

    word = word.lower()

    if word in corpus.positive:
        return POSITIVE_SENTIMENT
    elif word in corpus.negative:
        return NEGATIVE_SENTIMENT
    else:
        return NEUTRAL_SENTIMENT

def get_modifier(word):
    """Returns whether a word has special sentiment modifying properties
    """

    word = word.lower()

    if word in corpus.reverse_modifiers:
        return REVERSE_MODIFIER
    elif word in corpus.positive_modifiers:
        return POSITIVE_MODIFIER
    elif word in corpus.negative_modifiers:
        return NEGATIVE_MODIFIER
    else:
        return DEFAULT_MODIFIER
