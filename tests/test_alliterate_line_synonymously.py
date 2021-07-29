from unittest import TestCase

from agents.alliterate_line_synonymously import do


class Test(TestCase):
    # reported
    def test_do(self):
        actual_line = do('hello world')
        self.assertEqual('hi humanity', actual_line)

    def test_do2(self):
        actual_line = do('bad door')
        self.assertEqual('defective doorway', actual_line)
