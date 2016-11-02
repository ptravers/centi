# -*- coding: utf-8 -*-

"""
centi.tree
~~~~~~~~~~~~~~~
This module contains the methods for evaluating the grammar trees returned by 
the parser
"""

# from .sentiment import get_sentiment
from nltk.tree import Tree

# structure of components: [(label, (polarity, modifier))]
def resolve(components):
    # if we have only one component below a node, just propogate its attributes
    if len(components) == 1:
        return components[0][1]
    else:
        # DUMMY: rules are applied here
        return (0, '=')

def get_polarity(node):
    if type(node[0]) is not Tree:
        # DUMMY: return get_sentiment(node[0])
        return (0, '=')
    else:
        children = []
        for child in node:
            children += [(child.label(), get_polarity(child))]
        return resolve(children)