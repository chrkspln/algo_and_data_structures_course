import unittest
from src.GameServerLatency import *


class TestGameServerLatency(unittest.TestCase):
    def test_normal_case(self):
        file = "./src/resources/gamsrv_in1.txt"
        out = "./src/resources/gamsrv_out1.txt"
        find_server_position(file, out)
        with open("./src/resources/gamsrv_out1.txt") as output_file:
            output = output_file.read()
        expected = "100"
        self.assertEqual(output, expected)

    def test_empty_input(self):
        file = "./src/resources/gamsrv_in2.txt"
        out = "./src/resources/gamsrv_out2.txt"
        find_server_position(file, out)
        with open("./src/resources/gamsrv_out2.txt") as output_file:
            output = output_file.read()
        expected = "-1"
        self.assertEqual(output, expected)
