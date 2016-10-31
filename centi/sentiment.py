# -*- coding: utf-8 -*-

"""
centi.sentiment
~~~~~~~~~~~~~~~
This module contains the methods for converting words into sentiment tuples
"""

import os

def abs_path(relative_path):
    """Resolves relative path to absolute path"""
    return os.path.join(os.path.dirname(__file__), relative_path)

def get_sentiment(word):
    """Creates sentiment and modifier tuple for a word
    Sentiment can be positive (1), neutral (0) or negative (-1)
    Modifier can be pos (P), neg (N), invert (¬) or no modifier (=)
    """
    
    sentiment = 0   # Default neutral sentiment
    modifier  = '=' # Default no modifier
    
    word += "\n"
    
    with open(abs_path('corpus/negative.txt'), 'r') as negativeWords:
        for negWord in negativeWords:
            if word == negWord:
                sentiment = -1
    
    with open(abs_path('corpus/positive.txt'), 'r') as positiveWords:
        for posWord in positiveWords:
            if word == posWord:
                sentiment = 1
    
    with open(abs_path('corpus/reverse.txt'), 'r') as reverseWords:
        for revWord in reverseWords:
            if word == revWord:
                modifier = '¬'
    
    return (sentiment, modifier)
