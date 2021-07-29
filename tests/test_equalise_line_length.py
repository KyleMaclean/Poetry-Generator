import copy
from unittest import TestCase

from agents import equalise_line_length
from agents.equalise_line_length import EPSILON
from agents.equalise_line_length import chop_line
from util.phoneme_util import get_number_of_phonemes_in_line_using_entries


def get_differences(actual_lines):
    actual_phoneme_length0 = get_number_of_phonemes_in_line_using_entries(actual_lines[0])
    actual_phoneme_length1 = get_number_of_phonemes_in_line_using_entries(actual_lines[1])
    return abs(actual_phoneme_length0 - actual_phoneme_length1)


class TestDo(TestCase):

    def test_do(self):
        input_lines = ['there was a cat', 'and a roof']
        actual_lines = (equalise_line_length(copy.deepcopy(input_lines)))
        self.assertLessEqual(get_differences(actual_lines), EPSILON)

    def test_do2(self):
        input_lines = ['we saw a large house with an antenna on it', 'but no cats']
        actual_lines = (equalise_line_length(copy.deepcopy(input_lines)))
        self.assertLessEqual(get_differences(actual_lines), EPSILON)

    def test_do3(self):
        input_lines = ['all the people sat around the fire', 'but no cats']
        actual_lines = (equalise_line_length(copy.deepcopy(input_lines)))
        difference = get_differences(actual_lines)
        self.assertLessEqual(difference, EPSILON)

    def test_do4(self):
        # reported
        input_lines = ['eating from a big bowl of strawberries', 'on the blanket']
        actual_lines = (equalise_line_length(copy.deepcopy(input_lines)))
        difference = get_differences(actual_lines)
        self.assertLessEqual(difference, EPSILON)


class TestChopLine(TestCase):
    def test_chop_line(self):
        desired_phonemes = 8
        input_line = 'this is a long line'
        input_phonemes = get_number_of_phonemes_in_line_using_entries(input_line)
        self.assertLessEqual(desired_phonemes, input_phonemes)
        new_line = chop_line(input_line, [input_phonemes, desired_phonemes])
        new_phonemes = get_number_of_phonemes_in_line_using_entries(new_line)
        difference = abs(new_phonemes - desired_phonemes)
        self.assertLessEqual(difference, 2)

    def test_chop_line2(self):
        desired_phonemes = 14
        input_line = 'we have congratulated the funny people who arbitrated the proceedings'
        input_phonemes = get_number_of_phonemes_in_line_using_entries(input_line)
        self.assertLessEqual(desired_phonemes, input_phonemes)
        new_line = chop_line(input_line, [input_phonemes, desired_phonemes])
        new_phonemes = get_number_of_phonemes_in_line_using_entries(new_line)
        difference = abs(new_phonemes - desired_phonemes)
        self.assertLessEqual(difference, 4)

    def test_chop_line3(self):
        desired_phonemes = 20
        input_line = 'we enjoyed delectable slices of mango'
        input_phonemes = get_number_of_phonemes_in_line_using_entries(input_line)
        self.assertLessEqual(desired_phonemes, input_phonemes)
        new_line = chop_line(input_line, [input_phonemes, desired_phonemes])
        new_phonemes = get_number_of_phonemes_in_line_using_entries(new_line)
        difference = abs(new_phonemes - desired_phonemes)
        self.assertLessEqual(difference, 3)
