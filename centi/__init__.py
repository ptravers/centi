# -*- coding: utf-8 -*-

"""
centi

The recursive Semtiment Analysis tool

"""

# Import everything here you want available in the centi package
from .parser import parse_sentence, parse_sentences
from .sentiment import get_sentiment
from .tree import get_polarity
from .constants import negative, modifier_negative, positive, modifier_positive, modifier_reverse, neutral, modifier_default
