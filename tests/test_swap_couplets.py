from unittest import TestCase

from agents import swap_couplets


class Test(TestCase):
    def test_do(self):
        lines = ['all on its own', 'we found a house', 'in the forest', 'with a box']
        expected_lines = ['in the forest', 'with a box', 'all on its own', 'we found a house']
        actual_lines = swap_couplets(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do2(self):
        lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        expected_lines = ['3', '4', '1', '2', '5', '6', '7', '8', '9', '10']
        actual_lines = swap_couplets(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do3(self):
        lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        expected_lines = ['1', '2', '3', '4', '7', '8', '5', '6', '9']
        actual_lines = swap_couplets(lines)
        self.assertEqual(expected_lines, actual_lines)
