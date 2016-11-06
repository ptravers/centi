# -*- coding: utf-8 -*-

from .constants import *

def apply_rules(snodes):
    # Placeholder happiness wins rule (any happy means all happy)
    if any([snode.sentiment is POSITIVE_SENTIMENT for snode in snodes]):
        return POSITIVE_SENTIMENT, DEFAULT_MODIFIER
    else:
        return NEUTRAL_SENTIMENT, DEFAULT_MODIFIER

def negator(nodes):
    #does nothing for now
    for node in nodes:
        node[1][0]
    return nodes
