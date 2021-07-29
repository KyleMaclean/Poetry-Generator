from unittest import TestCase

from agents import rhyme_two_lines_synonymously


class Test(TestCase):

    # reported
    def test_do(self):
        couplet = ['there was a mouse', 'in his home']
        expected_couplet = ['there was a mouse', 'in his house']
        actual_couplet = rhyme_two_lines_synonymously(couplet)
        self.assertEqual(expected_couplet, actual_couplet)

    def test_do2(self):
        couplet = ['there was a house', 'called a home']
        expected_couplet = ['there was a house', 'called a home']
        actual_couplet = rhyme_two_lines_synonymously(couplet)
        self.assertEqual(expected_couplet, actual_couplet)
