# replaces a random word from a random line with its synonym

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
            synonyms = synonym_antonym_util.get_synonyms_for_word(tokens[i])
            if synonyms:
                random_synonym_index = random.randrange(len(synonyms))
                tokens[i] = synonyms[random_synonym_index]
                return ' '.join(tokens)
    return line
