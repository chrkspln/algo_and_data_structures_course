import unittest
from src.BFSShortMinesPath import *


class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        file = "../src/resources/input_BFSShortMinesPath1.txt"
        out = "../src/resources/output_BFSShortMinesPath1.txt"
        short_mines_path_search(file, out)
        with open("../src/resources/output_BFSShortMinesPath1.txt") as output_file:
            output = output_file.read()
        expected = (
            "([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),"
            " (1, 6), (0, 6), (0, 7), (0, 8), (0, 9)], 12)"
        )
        self.assertEqual(output, expected)

    def test_empty_input(self):
        file = "../src/resources/input_BFSShortMinesPath2.txt"
        out = "../src/resources/output_BFSShortMinesPath2.txt"
        short_mines_path_search(file, out)
        with open("../src/resources/output_BFSShortMinesPath2.txt") as output_file:
            output = output_file.read()
        expected = "(-1, -1)"
        self.assertEqual(output, expected)
