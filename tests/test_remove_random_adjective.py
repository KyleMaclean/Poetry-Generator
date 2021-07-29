from unittest import TestCase

from agents import remove_random_adjective


class Test(TestCase):

    # reported
    def test_do(self):
        line = 'i saw a bright light'
        expected_line = 'i saw a light'
        actual_line = remove_random_adjective(line)
        self.assertEqual(expected_line, actual_line)
