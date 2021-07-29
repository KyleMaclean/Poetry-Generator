from collections import defaultdict

import nltk

import util.tagsets
from util import synonym_antonym_util, phoneme_util


def do(line):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    word_synonyms = {}
    first_phonemes = set()
    for i in range(len(tagged)):
        if tagged[i][1] in util.tagsets.replaceable:
            word_synonyms[i] = synonym_antonym_util.get_synonyms_for_word(tokens[i])
            for phoneme_list in phoneme_util.get_phoneme_lists_for_word_using_entries(tokens[i]):
                first_phonemes.add(phoneme_list[0])
    alliterative_matches = defaultdict(set)
    for first_phoneme in first_phonemes:
        for key in word_synonyms:
            for this_synonym in word_synonyms[key]:
                for this_synonym_phoneme_list in phoneme_util.get_phoneme_lists_for_word_using_entries(this_synonym):
                    if this_synonym_phoneme_list[0] == first_phoneme:
                        alliterative_matches[first_phoneme].add(key)
    if alliterative_matches:
        best_phoneme = max(alliterative_matches, key=lambda k: len(alliterative_matches[k]))
        for i in word_synonyms.keys():
            returned_synonym = get_synonym_according_to_phoneme(best_phoneme, tokens[i], word_synonyms[i])
            if returned_synonym not in tokens:
                tokens[i] = returned_synonym
    return ' '.join(tokens)


def get_synonym_according_to_phoneme(best_phoneme, word, word_synonyms_i):
    for this_synonym in word_synonyms_i:
        for phoneme_list in phoneme_util.get_phoneme_lists_for_word_using_entries(this_synonym):
            if phoneme_list[0] == best_phoneme:
                return this_synonym
    return word
