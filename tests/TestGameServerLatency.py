import unittest
from src.GameServerLatency import *


class TestGameServerLatency(unittest.TestCase):
    def test_normal_case(self):
        file = "../src/gamsrv_in1.txt"
        out = "../src/gamsrv_out1.txt"
        find_server_position(file, out)
        with open("../src/gamsrv_out1.txt") as output_file:
            output = output_file.read()
        expected = "100"
        self.assertEqual(output, expected)

    def test_empty_input(self):
        file = "../src/gamsrv_in2.txt"
        out = "../src/gamsrv_out2.txt"
        find_server_position(file, out)
        with open("../src/gamsrv_out2.txt") as output_file:
            output = output_file.read()
        expected = "-1"
        self.assertEqual(output, expected)
