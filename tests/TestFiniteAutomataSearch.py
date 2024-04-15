import unittest
from src.FiniteAutomataSearch import *


class TestFiniteAutomataSearch(unittest.TestCase):
    def test1_pattern_is_found(self):
        # Test case where pattern is found in the string
        fa = finite_automata_search("abc", "xabcy")
        self.assertEqual(fa, [1])

    def test2_pattern_is_found(self):
        # Test case where pattern is found in the string
        fa = finite_automata_search("aaa", "aaabaaa")
        self.assertEqual(fa, [0, 4])

    def test3_pattern_is_found(self):
        # Test case where pattern is found in the string
        fa = finite_automata_search("ababaca", "ababacababacabbb")
        self.assertEqual(fa, [0, 6])

    def test_pattern_not_found(self):
        # Test case where pattern is not found in the string
        fa = finite_automata_search("abc", "xaybzc")
        self.assertEqual(fa, [])

    def test_empty_string(self):
        # Test case where pattern is empty
        fa = finite_automata_search("", "any_string")
        self.assertEqual(fa, [])

    def test_empty_pattern(self):
        # Test case where string is empty
        fa = finite_automata_search("abc", "")
        self.assertEqual(fa, [])

    def test_pattern_longer_than_string(self):
        # Test case where pattern is longer than string
        fa = finite_automata_search("abcdef", "abc")
        self.assertEqual(fa, [])

    def test_same_pattern_and_string(self):
        # Test case where pattern and string are the same
        fa = finite_automata_search("abc", "abc")
        self.assertEqual(fa, [0])


if __name__ == "__main__":
    unittest.main()
