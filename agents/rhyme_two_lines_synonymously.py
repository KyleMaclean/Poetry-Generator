# randomly choose pair of lines;
# replace final word on second line with word rhyming with final word on first line
# that is also a synonym with the original last word in the second line

import random

import nltk

from util import couplet_util


def do(couplet, random_seed=42):
    intersection = couplet_util.get_intersection_using_entries(couplet)
    tokens0 = nltk.word_tokenize(couplet[0])
    tokens1 = nltk.word_tokenize(couplet[1])
    end_words = [tokens0[-1], tokens1[-1]]
    intersection = [word for word in intersection if word not in end_words]
    if intersection:
        random.seed(random_seed)
        rhyming_synonym = intersection[random.randrange(len(intersection))]
        tokens = nltk.word_tokenize(couplet[1])
        tokens[-1] = rhyming_synonym
        couplet[1] = ' '.join(tokens)
    return couplet
