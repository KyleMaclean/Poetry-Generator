from unittest import TestCase

from agents.add_metaphor import do


class Test(TestCase):
    # reported
    def test_do(self):
        actual_line = do('you are beautiful')
        self.assertEqual(actual_line, 'you are beautiful as the vivid colors of a painting')
