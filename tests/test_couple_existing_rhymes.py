from unittest import TestCase

from agents import couple_existing_rhymes


class Test(TestCase):

    # reported
    def test_do(self):
        lines = ['there was a cat', 'and a roof', 'on which it sat']
        expected_lines = ['there was a cat', 'on which it sat', 'and a roof']
        actual_lines = (couple_existing_rhymes(lines))
        self.assertEqual(expected_lines, actual_lines)

    def test_do2(self):
        lines = ['there it was', 'and said today', 'hip hip hooray']
        expected_lines = ['there it was', 'and said today', 'hip hip hooray']
        actual_lines = (couple_existing_rhymes(lines))
        self.assertEqual(expected_lines, actual_lines)

    def test_do3(self):
        lines = ['the jovial cat', 'wore a top hat', 'on its mat']
        expected_lines = ['the jovial cat', 'wore a top hat', 'on its mat']
        actual_lines = (couple_existing_rhymes(lines))
        self.assertEqual(expected_lines, actual_lines)

    def test_do4(self):
        lines = ['the jovial cat', 'wore a top hat', 'with the funny human', 'on its mat']
        expected_lines = ['the jovial cat', 'wore a top hat', 'with the funny human', 'on its mat']
        actual_lines = (couple_existing_rhymes(lines))
        self.assertEqual(expected_lines, actual_lines)
