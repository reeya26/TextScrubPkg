import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textscrub import clean
import unittest


class TestingBasicCleaning(unittest.TestCase):

    def test_remove_hyperlinks(self):

        a = 'this line contains hyperlink - https://google.com/'
        b = 'this line contains hyperlink - '

        mssg =  'Values are not equal'

        clean_text = clean.remove_hyperlinks(a)
        self.assertEqual(clean_text, b, mssg)

    def test_remove_glyphs(self):

        a = '\x00\x01string'
        b = 'string'

        mssg = 'Values are not equal'

        clean_text = clean.remove_glyphs(a)       
        self.assertEqual(clean_text, b, mssg)

if __name__ == '__main__':
    unittest.main()