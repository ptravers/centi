import os
from nltk.parse import stanford
import sys

def recurse(sentences, listiterator):
    if type(listiterator) is not type(sentences):
        print listiterator
        return
    for i in listiterator:
        recurse(sentences, i)


if __name__ == "main":
    args = sys.argv[1:len(sys.argv)]
    parser = stanford.StanfordParser()
    sentences = parser.raw_parse_sents(" ".join(args))
    for i in sentences:
        if type(i) is type(sentences):
            recurse(sentences, i)
        else:
            print i
