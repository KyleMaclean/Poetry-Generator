import random

import nltk

import util.tagsets
from util import hypernym_hyponym_util


def do(line, random_seed=42):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    random_indices = list(range(len(tokens)))
    random.seed(random_seed)
    random.shuffle(random_indices)
    for i in random_indices:
        if tagged[i][1] in util.tagsets.noun_and_proper_noun_tagset:
            hyponyms = hypernym_hyponym_util.get_hyponyms(tokens[i])
            if hyponyms:
                random_hyponym_index = random.randrange(len(hyponyms))
                tokens[i] = hyponyms[random_hyponym_index].replace('_', ' ')
                return ' '.join(tokens)
    return line
