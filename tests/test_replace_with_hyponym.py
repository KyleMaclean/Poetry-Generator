from unittest import TestCase

import agents.replace_with_hyponym


class Test(TestCase):

    # reported
    def test_do(self):
        input_text = 'the apple is on the floor'
        actual_line = agents.replace_with_hyponym(input_text)
        self.assertEqual(actual_line, 'the crab apple is on the floor')
