import unittest
from src.IJonesLabyrinth import *


class TestIJonesLabyrinth(unittest.TestCase):
    def test_normal_case(self):
        file = "../src/resources/ijones_normal_case_in.csv"
        out = "../src/resources/ijones_normal_case_out.txt"
        find_all_possible_paths(file, out)
        with open("../src/resources/ijones_normal_case_out.txt") as output_file:
            output = output_file.read()
        expected = "5"
        self.assertEqual(output, expected)

    def test_line_case(self):
        file = "../src/resources/ijones_line_case_in.csv"
        out = "../src/resources/ijones_line_case_out.txt"
        find_all_possible_paths(file, out)
        with open("../src/resources/ijones_line_case_out.txt") as output_file:
            output = output_file.read()
        expected = "2"
        self.assertEqual(output, expected)

    def test_a_case(self):
        file = "../src/resources/ijones_a_case_in.csv"
        out = "../src/resources/ijones_a_case_out.txt"
        find_all_possible_paths(file, out)
        with open("../src/resources/ijones_a_case_out.txt") as output_file:
            output = output_file.read()
        expected = "201684"
        self.assertEqual(output, expected)
