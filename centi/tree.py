# -*- coding: utf-8 -*-

"""
centi.tree
~~~~~~~~~~~~~~~
This module contains the methods for evaluating the grammar trees returned by
the parser
"""
from .constants import *
from .sentiment import get_sentiment, get_modifier
from .snode     import Snode
from nltk.tree  import Tree

def resolve(snodes):
    # If there is only one snode then propagate sentiment/modifier to parent
    if len(snodes) == 1:
        return snodes[0].sentiment, snodes[0].modifier
    else:
        # DUMMY: rules are applied here
        return NEUTRAL_SENTIMENT, DEFAULT_MODIFIER

def get_polarity(node):
    if type(node[0]) is Tree:
        children = []
        
        for child in node:
            children.append(get_polarity(child))
        
        sentiment, modifier = resolve(children)
        
        return Snode(node.label(), sentiment, modifier)
    else:
        return Snode(node.label(), get_sentiment(node[0]), get_modifier(node[0]))

