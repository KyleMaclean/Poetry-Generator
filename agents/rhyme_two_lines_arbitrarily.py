import random

import nltk

from util import couplet_util


def do(couplet, random_seed=42):
    rhyming_words = couplet_util.get_rhyming_words_using_entries(couplet)
    random.seed(random_seed)
    random.shuffle(rhyming_words)
    tokens1 = nltk.word_tokenize(couplet[1])
    tagged1 = nltk.pos_tag(tokens1)
    last_word_second_line = tagged1[-1]
    for rhyming_word in rhyming_words:
        rhyming_word_tag = nltk.pos_tag([rhyming_word])[0][1]
        if rhyming_word_tag == last_word_second_line[1]:
            tokens1[-1] = rhyming_word
            couplet[1] = ' '.join(tokens1)
            break
    return couplet
