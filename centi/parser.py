# -*- coding: utf-8 -*-

"""
centi.parser
~~~~~~~~~~~~~~~
This module contains the methods for parsing input into grammar trees
"""

from nltk.parse import stanford, ProjectiveDependencyParser
from nltk.grammar import DependencyGrammar

def parse_sentence(raw_sentence):
    parser = stanford.StanfordParser()

    parser_output = parser.raw_parse(raw_sentence)

    return [tree[0] for tree in parser_output]


def parse_sentences(raw_sentences):
    parser = stanford.StanfordParser()

    raw_trees = parser.raw_parse_sents(raw_sentences)

    # Converts messy iterables into simple list of trees
    return [raw_tree[0] for sublist in raw_trees for raw_tree in sublist]
