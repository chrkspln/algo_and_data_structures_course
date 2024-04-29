import unittest
from src.VeniceIslandsInternet import *


class TestVeniceIslandsInternet(unittest.TestCase):
    def test_normal_case(self):
        file = "../src/resources/islands_normal_case.csv"
        out = "../src/resources/islands_out_normal_case.txt"
        find_min_cable_length(file, out)
        with open("../src/resources/islands_out_normal_case.txt") as output_file:
            output = output_file.read()
        expected = "4"
        self.assertEqual(output, expected)

    def test_empty_input(self):
        file = "../src/resources/islands_empty_case.csv"
        out = "../src/resources/islands_out_empty_case.txt"
        find_min_cable_length(file, out)
        with open("../src/resources/islands_out_empty_case.txt") as output_file:
            output = output_file.read()
        expected = ""
        self.assertEqual(output, expected)
