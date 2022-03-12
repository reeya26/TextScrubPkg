# importing required packages
from textscrub import clean
import unittest
import pandas as pd

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestingBasicCleaning(unittest.TestCase):

    def test_homogenize_column(self):

        non_uniform_df = pd.DataFrame(['CVS Pharmacy', 'cvs', 'Bartell Drugs', 'cvs pharmcy', 'bartell', 'Cvs Pharmacy', 'cvs', 'bartell drug'], columns=['Pharmacy'])
        expected_uniform_df = pd.DataFrame(['CVS Pharmacy', 'cvs', 'Bartell Drugs', 'CVS Pharmacy', 'bartell', 'CVS Pharmacy', 'cvs', 'Bartell Drugs'], columns=['Pharmacy'])

        clean_series = clean.homogenize_column(non_uniform_df['Pharmacy'], eps=3)
        clean_df = clean_series.to_frame(name='Pharmacy')

        mssg = 'Values are not equal'

        self.assertEqual(True, clean_df.equals(expected_uniform_df), mssg)

    def test_remove_hyperlinks(self):

        unclean_text = 'this line contains hyperlink - https://google.com/'
        expected_string = 'this line contains hyperlink - '

        mssg = 'Values are not equal'

        clean_text = clean.remove_hyperlinks(unclean_text)
        self.assertEqual(clean_text, expected_string, mssg)

    def test_remove_glyphs(self):

        unclean_text = '\x00 ß string'
        expected_string = 'string'

        mssg = 'Values are not equal'

        clean_text = clean.remove_glyphs(unclean_text)
        self.assertEqual(clean_text, expected_string, mssg)

    def test_remove_html_tags(self):

        unclean_text = """<body><div>This is a sample text with <b>lots of tags</b></div><br/></body>"""
        expected_string = "This is a sample text with lots of tags"

        mssg = 'Values are not equal'

        clean_text = clean.remove_html_tags(unclean_text)
        self.assertEqual(clean_text, expected_string, mssg)

    def test_remove_spaces(self):

        unclean_text = "This is a   sample text with lots of    spaces\n."
        expected_string = "This is a sample text with lots of spaces."

        mssg = 'Values are not equal'

        clean_text = clean.remove_spaces(unclean_text)
        self.assertEqual(clean_text, expected_string, mssg)

    def test_remove_punctuation(self):

        unclean_text = "A lot of !!!! .... ,,,, ;;;;;;;?????"
        expected_string = "A lot of "

        mssg = 'Values are not equal'

        clean_text = clean.remove_punctuation(unclean_text)
        self.assertEqual(clean_text, expected_string, mssg)


if __name__ == '__main__':
    unittest.main()
