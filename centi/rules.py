# -*- coding: utf-8 -*-

from .constants import *


def apply_rules(snodes, parent_label):

    head_snode_index = calculate_head(snodes, parent_label)

    sentiment = NEUTRAL_SENTIMENT
    modifier = DEFAULT_MODIFIER

    has_positive = any([snode.sentiment is POSITIVE_SENTIMENT for snode in snodes])
    has_negative = any([snode.sentiment is NEGATIVE_SENTIMENT for snode in snodes])
    has_mixed    = any([snode.sentiment is MIXED_SENTIMENT    for snode in snodes])

    if has_mixed:
        sentiment = MIXED_SENTIMENT

    elif has_positive and has_negative:
        sentiment = MIXED_SENTIMENT

    elif has_positive and not has_negative:
        sentiment = POSITIVE_SENTIMENT

    elif has_negative and not has_positive:
        sentiment = NEGATIVE_SENTIMENT

    if head_snode_index :
        head_snode = snodes[head_snode_index]
        if 0 < head_snode_index:
            for snode in snodes:
                pre_head_rules(snode, head_snode, sentiment, modifier)

    return sentiment, modifier

def pre_head_rules(snode, head_snode, sentiment, modifier):
    #Pre Head Rules are added below

    if snode.modifier == REVERSE_MODIFIER:
        labels = NOUN_LABELS + ADVERB_LABELS + ADJ_LABELS + ["VBP", "VP","PP"]
        if head_snode.label in labels:
            sentiment = NEGATIVE_SENTIMENT*head_snode.sentiment
            modifier = NEUTRAL_MODIFIER

def calculate_head(snodes, parent_label):
    """Marks, if applicable, a snode as the head
    """

    head_map = {
        "NP" : get_noun_phrase_head,
        "VP" : get_verb_phrase_head,
        "VBP" : get_verb_phrase_head,
        "PP" : get_prepositional_phrase_head,
        "ADJP" : get_adjective_phrase_head,
        "ADVP" : get_adverb_phrase_head,
        "S" : get_sentence_head
    }

    try :
        return head_map[parent_label](snodes)
    except KeyError as e:
        print type(e).__name__ + ": Key not found. Key was " + parent_label



def get_noun_phrase_head(snodes):
    # Including pronouns
    noun_labels    = NOUN_LABELS
    for index, snode in enumerate(snodes):
        if snode.label in noun_labels:
            snode.head = True
            return index

def get_verb_phrase_head(snodes):
    head_labels = VERB_LABELS + VERB_PHRASE_LABELS

    for index in xrange(len(snodes)-1, 0, -1):
        snode = snodes[index]
        if snode.label in head_labels:
            snode.head = True
            return index

def get_prepositional_phrase_head(snodes):
    for index, snode in enumerate(snodes):
        if snode.label == 'IN':
            snode.head = True
            return index

def get_adjective_phrase_head(snodes):
    adjective_labels = ADJ_LABELS

    for index, snode in enumerate(snodes):
        if snode.label in adjective_labels:
            snode.head = True
            return index

def get_adverb_phrase_head(snodes):
    adverb_labels = ADVERB_LABELS

    for index, snode in enumerate(snodes):
        if snode.label in adverb_labels:
            snode.head = True
            return index

def get_sentence_head(snodes):
    verb_phrase_labels = VERB_PHRASE_LABELS

    for index, snode in enumerate(snodes):
        if snode.label in verb_phrase_labels:
            snode.head = True
            return index

