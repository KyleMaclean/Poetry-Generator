from unittest import TestCase

from agents import add_sensible_adjectives


class Test(TestCase):
    # reported
    def test_do1(self):
        line = add_sensible_adjectives('the bread and wine')
        self.assertEqual('the white bread and wine', line)

    def test_do2(self):
        line = add_sensible_adjectives('the bread and wine', random_seed=43)
        self.assertEqual('the wholewheat bread and wine', line)

    def test_do3(self):
        line = add_sensible_adjectives('the bread and wine')
        line = add_sensible_adjectives(line)
        self.assertEqual('the white bread and more wine', line)
