from unittest import TestCase

from agents import replace_with_synonym


class Test(TestCase):

    def test_do1(self):
        line = 'we discovered a new realm'
        expected_line = 'we expose a new realm'
        actual_line = replace_with_synonym(line, random_seed=44)
        self.assertEqual(expected_line, actual_line)

    # reported
    def test_do2(self):
        line = 'we discovered a new realm'
        expected_line = 'we discovered a new kingdom'
        actual_line = replace_with_synonym(line, random_seed=45)
        self.assertEqual(expected_line, actual_line)

    def test_do3(self):
        line = 'we discovered a new realm'
        expected_line = 'we expose a young realm'
        actual_line = replace_with_synonym(line, random_seed=44)
        actual_line = replace_with_synonym(actual_line, random_seed=47)
        self.assertEqual(expected_line, actual_line)
