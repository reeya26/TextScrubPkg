import sys,os

from sqlalchemy import false
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textscrub import normalize_text
import unittest

class TestingNormalize(unittest.TestCase):


    def test_normalize_text(self):

        a = 'I’m convinced that😭😭😭 is the most :)expressive emoji combo   and it sucks.'
        b = 'I’m convinced that is the most expressive emoji combo and it sucks.'

        mssg =  'Values are not equal'

        clean_text = normalize_text.normalize_text(a, 
                    remove_glyphs=True,
                    remove_html_tags = False,
                    remove_hyperlinks = False,
                    remove_punctuation = False,
                    remove_spaces = True,
                    tokenizing = True,
                    stopwords_removal = False,
                    lemmat = False,
                    remove_emojis = True,
                    replace_emojis = False)
        self.assertEqual(clean_text, b, mssg)

if __name__ == '__main__':
    unittest.main()