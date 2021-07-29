from unittest import TestCase

from agents import rhyme_two_lines_arbitrarily


class Test(TestCase):
    def test_do(self):
        couplet = ['a forest of sticks', 'that looked like a wood']
        expected_couplet = ['a forest of sticks', 'that looked like a pix']
        actual_couplet = rhyme_two_lines_arbitrarily(couplet)
        self.assertEqual(expected_couplet, actual_couplet)

    def test_do2(self):
        couplet = ['rosemary in the nose', 'is like happiness']
        expected_couplet = ['rosemary in the nose', 'is like d\'angelo\'s']
        actual_couplet = rhyme_two_lines_arbitrarily(couplet, random_seed=55)
        self.assertEqual(expected_couplet, actual_couplet)

    def test_do3(self):
        # reported
        couplet = ['trees like you', 'are very tall']
        expected_couplet = ['trees like you', 'are very new']
        actual_couplet = rhyme_two_lines_arbitrarily(couplet)
        self.assertEqual(expected_couplet, actual_couplet)
