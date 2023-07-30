import unittest

from translator import englishtofrench, frenchtoenglish

class tests_englishtofrench(unittest.TestCase):

    def test1_englishtofrench(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

    def test2_englishtofrench(self):
        self.assertNotEqual(englishtofrench('Hello'), 'Bonjourno')

class tests_frenchtoenglish(unittest.TestCase):

    def test1_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
    
    def test2_frenchtoenglish(self):
        self.assertNotEqual(frenchtoenglish('Bonjour'), 'Cat')

unittest.main()