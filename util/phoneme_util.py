# many agents need to determine how many phonemes are in a single word or a line of words.
# this utility offers slower, more robust ways to calculate the number of phonemes and faster, less robust ways.

import re
import nltk

# noinspection PyUnresolvedReferences
from generation.cmu_dict_without_emphasis import custom_entries
from generation.words_pos_phonemes_9802 import dictionary
from util.tagsets import replaceable


def get_applicable_words_starting_with_phoneme_using_9802(phoneme):
    # uses the Part of Speech tag in the custom '9802' corpus to determine which words are "replaceable" in the sense
    # that words in the part of speech often make sense to be swapped out for similar words (as a counter example, it
    # does not make sense to consider replacing the word "the" with a synonym)
    words = []
    for key in dictionary:
        if dictionary[key][0] in replaceable and dictionary[key][1][0][0] == phoneme:
            words.append(key)
    return words


def get_words_starting_with_phoneme_using_entries(phoneme):
    return [candidate_word for candidate_word, candidate_phonemes in custom_entries if candidate_phonemes[0] == phoneme]


def get_phoneme_lists_for_word_using_entries(word):
    return [candidate_phonemes for candidate_word, candidate_phonemes in custom_entries if candidate_word == word]


def quickly_get_first_phoneme_for_word_using_entries(word):
    # used a lot by `alliterate_line_arbitrarily` agent, so we prefer to take the first possible pronunciation's phoneme
    phonemes = quickly_get_phonemes_for_word_using_entries(word)
    if phonemes:
        return phonemes[0]
    return None


def quickly_get_phonemes_for_word_using_entries(word):
    # the `equalise_line_length` agent already does a lot of computation, so we just assume the first pronunciation that
    # we find in the list of entries is the one we want. the `remove_unrhymable_couplet` agent can, in the worst case,
    # check every couplet in the poem, so it also requires a fast way to get the phonemes in order to find synonyms
    for candidate_word, candidate_phonemes in custom_entries:
        if candidate_word == word:
            return candidate_phonemes


def get_number_of_phonemes_in_line_using_entries(line):
    # the slower method: find all the phoneme lists of a word and then state their average length to be the phoneme
    # length of that word.
    if not line:
        return 0
    tokens = nltk.word_tokenize(line)
    num = 0
    for word in tokens:
        phoneme_lists_for_word = get_phoneme_lists_for_word_using_entries(word)
        if phoneme_lists_for_word:
            word_num = 0
            for phoneme_list_for_word in phoneme_lists_for_word:
                word_num += len(phoneme_list_for_word)
            num += word_num // len(phoneme_lists_for_word)
    return num


def process_phoneme_options(phoneme_options):
    # used during evaluation to prevent numbers in the words from interfering with the number of phonemes calculations
    for i in range(len(phoneme_options)):
        phoneme_options[i] = [re.sub(r'[0-9]+', '', phoneme) for phoneme in phoneme_options[i]]
    return phoneme_options
