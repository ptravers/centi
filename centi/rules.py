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
        return NEUTRAL_SENTIMENT, DEFAULT_MODIFIER        return NEUTRAL_SENTIMENT, DEFAULT_MODIFIER

def calculate_head(snodes, parent_label):
    """Marks, if applicable, a snode as the head
    """

    # Noun Phrase
    if parent_label == "NP":
        # Including pronouns
        noun_labels    = ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']
        for snode in snodes:
            if snode.label in noun_labels:
                snode.head = True
                break
    
    # Verb Phrase
    elif parent_label == 'VP':
        verb_labels = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        
        for snode in snodes:
            if snode.label in verb_labels:
                snode.head = True
                break
    
    # Prepositional Phrase
    elif parent_label == 'PP':
        for snode in snodes:
            if snode.label == 'IN':
                snode.head = True
                break
    
    # Adjective Phrase
    elif parent_label == 'ADJP':
        adjective_labels = ['JJ', 'JJR', 'JJS']
        
        for snode in snodes:
            if snode.label in adjective_labels:
                snode.head = True
                break
    
    # Adverb Phrase
    elif parent_label == 'ADVP':
        adverb_labels = ['RB', 'RBR', 'RBS']
        
        for snode in snodes:
            if snode.label in adverb_labels:
                snode.head = True
                break
