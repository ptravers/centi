# -*- coding: utf-8 -*-

"""
evaluate centi
~~~~~~~~~~~~~~~
Usage:
python evaluate.py

Runs centi over a directory of text and generates a CSV of performance stats
"""

import centi
import sys
import glob
import os
import csv

if len(sys.argv) > 2:
    lex_directory = sys.argv[2]
else:
    raise ValueError("Must pass path to directory of .txt files")
    sys.exit(1)

if not os.path.isdir(lex_directory):
    raise ValueError("Must pass path of a valid directory")
    sys.exit(1)


lex_files = os.path.join(lex_directory + '/*.txt')

summary_keys = ['file', 'sentences', 'positive', 'negative', 'neutral', 'mixed']

skip_files = []

if len(sys.argv) == 4:
    with open(sys.argv[3]) as input_csv:
        reader = csv.DictReader(input_csv)
        
        skip_files = [old_summary['file'] for old_summary in reader]

with open(sys.argv[1] + '.csv', 'wb') as output_csv:
    dict_writer = csv.DictWriter(output_csv, summary_keys)
    dict_writer.writeheader()
    
    for lex_filename in glob.iglob(lex_files):
        if os.path.basename(lex_filename) in skip_files:
            print "Skipping: " + lex_filename
            continue
        
        print "Opening: " + lex_filename
        
        with open(lex_filename, 'r') as lex_file:
            text = lex_file.read()
        
        text = text.replace('<br /><br />', ' ').decode("utf8","ignore")
        
        try:
            summary = centi.summarise_text(text)
        except:
            print "Something went wrong, skipping!"
            continue 
        
        summary['file'] = os.path.basename(lex_filename)
        
        dict_writer.writerow(summary)
