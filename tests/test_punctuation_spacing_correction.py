from unittest import TestCase

from agents import punctuation_spacing_correction


class Test(TestCase):
    def test_do(self):
        lines = ['there was a mouse , cat , dog and flower', 'on the highest, weirdest , most abominable place']
        expected_lines = ['there was a mouse, cat, dog and flower', 'on the highest, weirdest, most abominable place']
        actual_lines = (punctuation_spacing_correction(lines))
        self.assertEqual(expected_lines, actual_lines)

    # reported
    def test_do2(self):
        lines = ['there was a mouse , cat , dog and flower !']
        expected_lines = ['there was a mouse, cat, dog and flower!']
        actual_lines = (punctuation_spacing_correction(lines))
        self.assertEqual(expected_lines, actual_lines)
