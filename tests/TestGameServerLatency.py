import unittest
from src.GameServerLatency import *


class TestGameServerLatency(unittest.TestCase):
    def test_incomplete_connections_list(self):
        v, e = 6, 6
        clients = [1, 2, 6]
        connections = [
            [1, 3, 10],
            [3, 4, 80],
            [4, 5, 50],
            [5, 6, 20],
            [2, 3, 40],
            [2, 4, 100],
        ]
        self.assertEqual(find_server_position(v, e, clients, connections), 100)

    def test_normal_case(self):
        v, e = 9, 12
        clients = [2, 4, 6]
        connections = [
            [1, 2, 20],
            [2, 3, 20],
            [3, 6, 20],
            [6, 9, 20],
            [9, 8, 20],
            [8, 7, 20],
            [7, 4, 20],
            [4, 1, 20],
            [5, 2, 10],
            [5, 4, 10],
            [5, 6, 10],
            [5, 8, 10],
        ]
        self.assertEqual(find_server_position(v, e, clients, connections), 10)

    def test_big_num(self):
        v, e = 3, 2
        clients = [1, 3]
        connections = [[1, 2, 50], [2, 3, 1000000000]]
        self.assertEqual(find_server_position(v, e, clients, connections), 1000000000)

    def test_empty_input(self):
        v, e, clients, connections = None, None, None, None
        self.assertEqual(find_server_position(v, e, clients, connections), -1)
