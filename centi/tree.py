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
from .rules     import apply_rules
from nltk.tree  import Tree

def resolve(snodes, parent_label):
    # If there is only one snode then propagate sentiment/modifier to parent
    if len(snodes) == 1:
        return snodes[0].sentiment, snodes[0].modifier
    else:
        return apply_rules(snodes, parent_label)

def get_polarity(node):
    if type(node[0]) is Tree:
        children = []
        
        for child in node:
            children.append(get_polarity(child))
        
        label               = node.label()
        sentiment, modifier = resolve(children, label)
    else:
        label     = node.label()
        sentiment = get_sentiment(node[0])
        modifier  = get_modifier(node[0])
    
    print "Node {0} ({1})[{2}]".format(label, sentiment, modifier)
    
    return Snode(label, sentiment, modifier)
