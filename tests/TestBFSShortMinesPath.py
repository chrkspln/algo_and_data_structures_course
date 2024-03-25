import unittest
from src.BFSShortMinesPath import *


class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        grid = [
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(short_mines_path_search(grid), 12)

    def test_shortest_path_isnt_from_first_node(self):
        grid = [
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(short_mines_path_search(grid), 6)

    def test_empty_input(self):
        grid = [[]]
        self.assertEqual(short_mines_path_search(grid), -1)
