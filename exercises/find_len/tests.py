#!/usr/local/bin/python


import unittest
import find_len
from collections import Counter


class SolutionTestCase(unittest.TestCase):
    """Tests for `find_len.py`."""

    def test_create_dic(self):
        """Clean items of punctuation, case and newlines, etc"""
        random_data = 'Gambino head Francesco "Franky Boy" Cali was shot eight times then run over outside his Staten Island home Wednesday night. The Daily Beast: \n The'
        self.assertEqual(find_len.create_dic(random_data), Counter({'Francesco': 9, 'Wednesday': 9, 'Gambino': 7, '"Franky': 7, 'outside': 7, 'Staten': 6, 'Island': 6, 'night.': 6, 'Beast:': 6, 'eight': 5, 'times': 5, 'Daily': 5, 'head': 4, 'Boy"': 4, 'Cali': 4, 'shot': 4, 'then': 4, 'over': 4, 'home': 4, 'was': 3, 'run': 3, 'his': 3, 'The': 3}))


if __name__ == '__main__':
    unittest.main()
