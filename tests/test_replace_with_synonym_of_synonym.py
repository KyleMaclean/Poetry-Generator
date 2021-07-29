from unittest import TestCase

from agents import replace_with_synonym_of_synonym


class Test(TestCase):

    # reported
    def test_do(self):
        line = 'today is a huge day'
        expected_line = 'today is a vast day'
        actual_line = (replace_with_synonym_of_synonym(line))
        self.assertEqual(expected_line, actual_line)
