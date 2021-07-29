from unittest import TestCase

from agents import a_an_correction


class Test(TestCase):
    # reported
    def test_do(self):
        lines = ['it is an mistake', 'to see a elephant']
        expected_lines = ['it is a mistake', 'to see an elephant']
        actual_lines = a_an_correction(lines)
        self.assertEqual(expected_lines, actual_lines)
