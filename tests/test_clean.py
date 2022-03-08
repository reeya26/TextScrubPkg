from textscrub import clean
import unittest

class TestingBasicCleaning(unittest.TestCase):

    def test_remove_non_ascii(self):

        a = 'Good bye in Swedish is Hej d\xe5'
        b = 'Good bye in Swedish is Hej d'

        mssg = 'Values are not equal'

        clean_text = clean.remove_non_ascii(a)       
        self.assertEqual(clean_text, b, mssg)

    def test_remove_hyperlinks(self):

        a = 'this line contains hyperlink - https://google.com/'
        b = 'this line contains hyperlink -'

        mssg =  'Values are not equal'

        clean_text = clean.remove_hyperlinks(a)
        self.assertEqual(clean_text, b, mssg)