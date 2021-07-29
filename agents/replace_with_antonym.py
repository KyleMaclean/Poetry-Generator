import random

import nltk

import util.tagsets
from util import synonym_antonym_util


def do(line, random_seed=42):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    random_indices = list(range(len(tokens)))
    random.seed(random_seed)
    random.shuffle(random_indices)
    for i in random_indices:
        if tagged[i][1] in util.tagsets.replaceable:
            antonyms = synonym_antonym_util.get_antonyms_for_word(tokens[i])
            if antonyms:
                random_synonym_index = random.randrange(len(antonyms))
                tokens[i] = antonyms[random_synonym_index]
                return ' '.join(tokens)
    return line
