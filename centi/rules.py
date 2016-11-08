# -*- coding: utf-8 -*-

from .constants import *

def apply_rules(snodes, parent_label):
    has_positive = any([snode.sentiment is POSITIVE_SENTIMENT for snode in snodes])
    has_negative = any([snode.sentiment is NEGATIVE_SENTIMENT for snode in snodes])
    has_mixed    = any([snode.sentiment is MIXED_SENTIMENT    for snode in snodes])

    calculate_head(snodes, parent_label)

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

def get_noun_phrase_head(snodes):
    # Including pronouns
    noun_labels    = ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']
    for snode in snodes:
        if snode.label in noun_labels:
            snode.head = True
            break

def get_verb_phrase_head(snodes):
    verb_labels = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    for snode in snodes:
        if snode.label in verb_labels:
            snode.head = True
            break

def get_prepositional_phrase_head(snodes):
    for snode in snodes:
        if snode.label == 'IN':
            snode.head = True
            break

def get_adjective_phrase_head(snodes):
    adjective_labels = ['JJ', 'JJR', 'JJS']

    for snode in snodes:
        if snode.label in adjective_labels:
            snode.head = True
            break

def get_adverb_phrase_head(snodes):
    adverb_labels = ['RB', 'RBR', 'RBS']

    for snode in snodes:
        if snode.label in adverb_labels:
            snode.head = True
            break

def calculate_head(snodes, parent_label):
    """Marks, if applicable, a snode as the head
    """

    head_map = {
        "NP" : get_noun_phrase_head,
        "VP" : get_verb_phrase_head,
        "PP" : get_prepositional_phrase_head,
        "ADJP" : get_adjective_phrase_head,
        "ADVP" : get_adverb_phrase_head
    }

    try :
        head_map[parent_label](snodes)
    except KeyError as e:
        print "Key not found. Key was " + parent_label
