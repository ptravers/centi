# -*- coding: utf-8 -*-

"""
run centi
~~~~~~~~~~~~~~~
Usage:
python run_centi.py

You can access the centi library from this file
"""

import centi

parseTree = centi.parse_sentence("Not those bad trees.")[0]
print parseTree
evaluatedParseTree = centi.get_polarity(parseTree)
print evaluatedParseTree
