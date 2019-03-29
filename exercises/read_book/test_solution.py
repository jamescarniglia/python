#!/usr/local/bin/python


import unittest
from solution import *
from collections import deque


class SolutionTestCase(unittest.TestCase):
    """Tests for `solution.py`."""

    def test_is_clean_data(self):
        """Clean items of punctuation, case and newlines, etc"""
        random_data = "bla bhal!!, blah heLLO junk\ntest here is some more stuFF"
        self.assertEqual(clean_data(random_data), deque(['bla', 'bhal', 'blah', 'hello', 'junk', 'test', 'here', 'is', 'some', 'more', 'stuff']))

    def test_is_pop_through_data(self):
        """Find matches in list using pop_through_data"""
        random_data_list = deque(['blah', 'blah', 'blah', 'hello', 'junk', 'blah', 'blah', 'blah', 'some', 'more', 'stuff'])
        self.assertEqual(pop_through_data(random_data_list), [('blah blah blah', 2), ('blah blah some', 1), ('blah blah hello', 1), ('hello junk blah', 1), ('junk blah blah', 1), ('blah some more', 1), ('blah hello junk', 1)])

    def test_read_in_file(self):
        """Find matches in file using read_in"""
        correct_list = deque(['the', 'project', 'gutenberg', 'ebook', 'of', 'on', 'the', 'origin', 'of', 'species', 'by', 'charles', 'darwin', 'this', 'ebook', 'is', 'for', 'the', 'use', 'this', 'ebook', 'is', 'for', 'the', 'use', 'of', 'anyone', 'anywhere', 'at', 'no', 'cost', 'and', 'with', 'almost', 'no', 'restrictions', 'whatsoever', 'you', 'may', 'copy', 'it', 'give', 'it', 'away', 'or'])
        files = ['test_pg2009_small.txt']
        self.assertEqual(read_in_file(files, False), correct_list)

    def test_read_in_stdin(self):
        """Find matches in file using stdin"""
        file_stdin = 'test_pg2009_small.txt'
        # fake stdin
        sys.stdin = open(file_stdin, 'r')
        correct_list = deque(['the', 'project', 'gutenberg', 'ebook', 'of', 'on', 'the', 'origin', 'of', 'species', 'by', 'charles', 'darwin', 'this', 'ebook', 'is', 'for', 'the', 'use', 'this', 'ebook', 'is', 'for', 'the', 'use', 'of', 'anyone', 'anywhere', 'at', 'no', 'cost', 'and', 'with', 'almost', 'no', 'restrictions', 'whatsoever', 'you', 'may', 'copy', 'it', 'give', 'it', 'away', 'or'])
        self.assertEqual(read_in_file(False, sys.stdin), correct_list)

    def test_main_stdin(self):
        """Find matches in file using main"""
        file_stdin = 'test_pg2009_small.txt'
        sys.argv = ['script', '-stdin']
        # fake stdin
        sys.stdin = open(file_stdin, 'r')
        # looks odd bc it is a table
        main_stdin_correct_list = 'Phrase                         Occurances\n---------------------------  ------------\nis for the                              2\nthis ebook is                           2\nebook is for                            2\nfor the use                             2\nby charles darwin                       1\nebook of on                             1\ngive it away                            1\nit give it                              1\nat no cost                              1\norigin of species                       1\nyou may copy                            1\nthe use this                            1\nof species by                           1\nalmost no restrictions                  1\nno restrictions whatsoever              1\nuse this ebook                          1\nthe project gutenberg                   1\nthe use of                              1\nmay copy it                             1\ndarwin this ebook                       1\ncost and with                           1\ncharles darwin this                     1\non the origin                           1\nspecies by charles                      1\nof anyone anywhere                      1\nproject gutenberg ebook                 1\nwhatsoever you may                      1\ncopy it give                            1\ngutenberg ebook of                      1\nand with almost                         1\nrestrictions whatsoever you             1\nof on the                               1\nno cost and                             1\nanywhere at no                          1\nwith almost no                          1\nthe origin of                           1\nanyone anywhere at                      1\nuse of anyone                           1'
        self.assertEqual(main(), main_stdin_correct_list)


if __name__ == '__main__':
    unittest.main()
