import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textscrub import clean
import unittest


class TestingBasicCleaning(unittest.TestCase):

    def test_remove_hyperlinks(self):

        unclean_text = 'this line contains hyperlink - https://google.com/'
        expected_string = 'this line contains hyperlink - '

        mssg =  'Values are not equal'

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

if __name__ == '__main__':
    unittest.main()