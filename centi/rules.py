# -*- coding: utf-8 -*-

from .constants import *

def apply_rules(snodes, parent_label):
    has_positive = any([snode.sentiment is POSITIVE_SENTIMENT for snode in snodes])
    has_negative = any([snode.sentiment is NEGATIVE_SENTIMENT for snode in snodes])
    has_mixed    = any([snode.sentiment is MIXED_SENTIMENT    for snode in snodes])

    if has_mixed:
        print "Propagating mixed sentiment"
        return MIXED_SENTIMENT, DEFAULT_MODIFIER

    elif has_positive and has_negative:
        print "Sentiment conflict!"
        return MIXED_SENTIMENT, DEFAULT_MODIFIER

    elif has_positive and not has_negative:
        print "Propagating positive sentiment"
        return POSITIVE_SENTIMENT, DEFAULT_MODIFIER

    elif has_negative and not has_positive:
        print "Propagating negative sentiment"
        return NEGATIVE_SENTIMENT, DEFAULT_MODIFIER

    else:
        print "Propagating neutral sentiment"
        return NEUTRAL_SENTIMENT, DEFAULT_MODIFIER