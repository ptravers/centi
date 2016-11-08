# -*- coding: utf-8 -*-

"""
centi.snode

Class for creating instances of propagated sentiment

"""

class Snode:
    def __init__(self, label, sentiment, modifier):
        self.label     = label
        self.sentiment = sentiment
        self.modifier  = modifier
        self.head      = False
