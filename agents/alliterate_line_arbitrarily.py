import random

import nltk

import util.tagsets
from util import phoneme_util


def do(line, random_seed=42):
    random.seed(random_seed)
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    first_phonemes = set()
    for i in range(len(tagged)):
        if tagged[i][1] in util.tagsets.replaceable:
            first_phoneme = phoneme_util.quickly_get_first_phoneme_for_word_using_entries(tagged[i][0])
            if first_phoneme:
                first_phonemes.add(first_phoneme)
    if not first_phonemes:
        return line
    random_first_phoneme = random.choice(list(first_phonemes))
    words_starting_with_phoneme = phoneme_util.get_applicable_words_starting_with_phoneme_using_9802(
        random_first_phoneme)
    # random.shuffle(words_starting_with_phoneme)
    for i in range(len(tagged)):
        current_tag = tagged[i][1]
        if current_tag not in util.tagsets.replaceable:
            continue
        for word_starting_with_phoneme in words_starting_with_phoneme:
            if nltk.pos_tag([word_starting_with_phoneme])[0][1] == current_tag:
                tokens[i] = word_starting_with_phoneme
                words_starting_with_phoneme.remove(word_starting_with_phoneme)
                random.shuffle(words_starting_with_phoneme)
                break
    return ' '.join(tokens)
