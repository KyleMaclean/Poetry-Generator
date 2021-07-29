from unittest import TestCase

from agents.swap_conjugates import do


class Test(TestCase):

    # reported
    def test_do1(self):
        lines = ['red apple and yellow pear']
        expected_lines = ['yellow pear and red apple']
        actual_lines = do(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do2(self):
        lines = ['juicy apple and yellow pear']
        expected_lines = ['yellow pear and juicy apple']
        actual_lines = do(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do3(self):
        lines = ['juicy apples and yellow pears']
        expected_lines = ['yellow pears and juicy apples']
        actual_lines = do(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do4(self):
        lines = ['And their snakes and their black demons']
        expected_lines = ['And their black demons and their snakes']
        actual_lines = do(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do5(self):
        lines = ['But ye and I are friends']
        expected_lines = ['But I and ye are friends']
        actual_lines = do(lines)
        self.assertEqual(expected_lines, actual_lines)

    def test_do6(self):
        lines = ['And to be dazed and mad and blind']
        expected_lines = ['And to be dazed and mad and blind']
        actual_lines = do(lines)
        self.assertEqual(expected_lines, actual_lines)
