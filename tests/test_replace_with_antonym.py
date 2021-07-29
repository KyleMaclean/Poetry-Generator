from unittest import TestCase

from agents.replace_with_antonym import do


class Test(TestCase):

    # reported
    def test_do(self):
        actual_line = do('we saw the happy Heffalump')
        self.assertEqual(actual_line, 'we saw the unhappy Heffalump')
