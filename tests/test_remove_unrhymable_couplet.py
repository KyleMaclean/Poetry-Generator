from unittest import TestCase

from agents import remove_unrhymable_couplet


class Test(TestCase):
    def test_do(self):
        # reported
        lines = ['a patch of silver', 'on the orange']
        expected_lines = []
        actual_lines = (remove_unrhymable_couplet(lines))
        self.assertEqual(expected_lines, actual_lines)

    def test_do2(self):
        lines = ['he was a hero', 'who said hi']
        expected_lines = ['he was a hero', 'who said hi']
        actual_lines = (remove_unrhymable_couplet(lines))
        self.assertEqual(expected_lines, actual_lines)

    def test_do3(self):
        lines = ['a patch of silver', 'on the orange', 'he was a hero', 'who said hi']
        expected_lines = ['he was a hero', 'who said hi']
        actual_lines = (remove_unrhymable_couplet(lines))
        self.assertEqual(expected_lines, actual_lines)

    def test_do4(self):
        lines = ['he was a hero', 'who said hi', 'a patch of silver', 'on the orange']
        expected_lines = ['he was a hero', 'who said hi']
        actual_lines = (remove_unrhymable_couplet(lines))
        self.assertEqual(expected_lines, actual_lines)
