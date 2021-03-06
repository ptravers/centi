# -*- coding: utf-8 -*-

"""
centi.parser
~~~~~~~~~~~~~~~
This module contains the methods for parsing input into grammar trees
"""

from nltk.parse.stanford import StanfordParser
import nltk

def parse_sentence(raw_sentence):
    parser = StanfordParser()

    parser_output = parser.raw_parse(raw_sentence)

    return [tree[0] for tree in parser_output]


def parse_sentences(raw_sentences):
    parser = StanfordParser()

    raw_trees = parser.raw_parse_sents(raw_sentences)

    # Converts messy iterables into simple list of trees
    return [raw_tree[0] for sublist in raw_trees for raw_tree in sublist]

def parse_text(raw_text):
    
    sentences = nltk.tokenize.sent_tokenize(raw_text)
    
    return parse_sentences(sentences)
