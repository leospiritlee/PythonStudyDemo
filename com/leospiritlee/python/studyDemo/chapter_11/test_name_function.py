import unittest
from chapter_11_demo import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):

        name = get_formatted_name('leo','lee')
        print(name)
        self.assertEqual(name, 'Leo Lee')

unittest.main

