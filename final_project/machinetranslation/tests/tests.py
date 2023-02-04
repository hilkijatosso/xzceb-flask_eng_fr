import unittest

from translator import english_to_french, french_to_english

class TestLanguageTranslator(unittest.TestCase):

    def test_englishToFrench_null_input(self):      
        with self.assertRaises(Exception):
            english_to_french("")

    def test_frenchToEnglish_null_input(self):
        with self.assertRaises(Exception):
            french_to_english("")

    def test_englishToFrench_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()