# -*- coding: utf-8 -*-

"""
Headlines
~~~~~~~~~~~~~~~
Usage:
python headlines.py

Runs centi over news headlines to observe success of sentiment determination
"""

import headline_data
import centi
import csv

headlines = headline_data.articles

keys = ['sentiment', 'centi']

i = 0

with open('output.csv', 'wb') as output_csv:
    dict_writer = csv.DictWriter(output_csv, keys)
    dict_writer.writeheader()
    
    for headline in headlines:
        i += 1
        print "Article #{0}".format(i)
        sentiment = centi.get_polarity(centi.parse_sentence(headline[0])[0]).sentiment
        
        output = {
            'sentiment' : headline[1],
            'centi'     : sentiment
        }
        
        dict_writer.writerow(output)
