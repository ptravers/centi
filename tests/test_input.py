import unittest
import os
from centi_app import parser

class TestBasicInput(unittest.TestCase):

    def setUp(self):
        self.file = open('test.txt', 'w')
        self.file.write("This is a test.")
        self.cwd = os.getcwd()

    def test_single_string_input(self):
        try:
            parser.run("This is a test.")
        except Exception as e:
            #https://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occured
            template = "an exception of type {0}:\n{1!r}"
            self.fail("Single string input failed with " + template.format(type(e).__name__, e.args))

    def tearDown(self):
        self.file.close()
        os.remove('test.txt')
