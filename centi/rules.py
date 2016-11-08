# -*- coding: utf-8 -*-

from .constants import *

def apply_rules(snodes, parent_label):

    calculate_head(snodes, parent_label)

    sentiment_to_propogate = NEUTRAL_SENTIMENT
    modifier_to_propogate = DEFAULT_MODIFIER

    has_positive = any([snode.sentiment is POSITIVE_SENTIMENT for snode in snodes])
    has_negative = any([snode.sentiment is NEGATIVE_SENTIMENT for snode in snodes])
    has_mixed    = any([snode.sentiment is MIXED_SENTIMENT    for snode in snodes])

    if has_mixed:
        print "Propagating mixed sentiment"
        sentiment_to_propogate = MIXED_SENTIMENT

    elif has_positive and has_negative:
        print "Sentiment conflict!"
        sentiment_to_propogate = MIXED_SENTIMENT

    elif has_positive and not has_negative:
        print "Propagating positive sentiment"
        sentiment_to_propogate = POSITIVE_SENTIMENT

    elif has_negative and not has_positive:
        print "Propagating negative sentiment"
        sentiment_to_propogate = NEGATIVE_SENTIMENT

    return sentiment_to_propogate, modifier_to_propogate

def pre_head_rules(snodes):
    #Pre Head Rules are added below
    if snodes:
        return snodes

def get_noun_phrase_head(snodes):
    # Including pronouns
    noun_labels    = NOUN_LABELS
    for snode in snodes:
        if snode.label in noun_labels:
            snode.head = True
            break

def get_verb_phrase_head(snodes):
    verb_labels = VERB_LABELS

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
    adjective_labels = ADJ_LABELS

    for snode in snodes:
        if snode.label in adjective_labels:
            snode.head = True
            break

def get_adverb_phrase_head(snodes):
    adverb_labels = ADVERB_LABELS

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
        print type(e).__name__ + ": Key not found. Key was " + parent_label



