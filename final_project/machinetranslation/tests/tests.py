import unittest
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_e2f(self):
        self.assertNotEqual(english_to_french('None'), '')
    def test_f2e(self):
        self.assertNotEqual(french_to_english('None'), '')
    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
unittest.main()