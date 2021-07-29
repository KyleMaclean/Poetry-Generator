from unittest import TestCase

from agents import decrease_to_single_adjective


class Test(TestCase):
    def test_do(self):
        line = 'it was a hot sunny day'
        expected_line = 'it was a sunny day'
        actual_line = (decrease_to_single_adjective(line))
        self.assertEqual(expected_line, actual_line)

    # reported
    def test_do2(self):
        line = 'it was a hot, sunny, windy day'
        expected_line = 'it was a sunny day'
        actual_line = (decrease_to_single_adjective(line))
        self.assertEqual(expected_line, actual_line)
