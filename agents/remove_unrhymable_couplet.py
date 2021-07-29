# checks if the two words on the ends of each line in each couplet have any common rhymes, and removes the first couplet
# where the end words do not have any common rhymes. the search goes top-to-bottom through all the lines in the poem.

import nltk

from util import phoneme_util, synonym_antonym_util
from util import rhyme_util


def do(lines, rhyme_level=1):
    for couplet_index in range(0, len(lines), 2):
        couplet = [lines[couplet_index], lines[couplet_index + 1]]
        last_word0 = nltk.word_tokenize(couplet[0])[-1]
        last_word1 = nltk.word_tokenize(couplet[1])[-1]
        synonyms0 = synonym_antonym_util.get_synonyms_for_word(last_word0) + [last_word0]
        synonyms1 = synonym_antonym_util.get_synonyms_for_word(last_word1) + [last_word1]
        list_of_phonemes0 = []
        list_of_phonemes1 = []
        for synonym0 in synonyms0:
            if synonym0:
                list_of_phonemes0.append(phoneme_util.quickly_get_phonemes_for_word_using_entries(synonym0))
        for synonym1 in synonyms1:
            if synonym1:
                list_of_phonemes1.append(phoneme_util.quickly_get_phonemes_for_word_using_entries(synonym1))

        rhyming0 = rhyme_util.get_rhyming_words_for_phonemes(list_of_phonemes0, rhyme_level) + [last_word0]
        rhyming1 = rhyme_util.get_rhyming_words_for_phonemes(list_of_phonemes1, rhyme_level) + [last_word1]

        if set(synonyms0) & set(rhyming1) or set(synonyms1) & set(rhyming0):
            continue
        else:
            lines[couplet_index:couplet_index + 2] = []
            return lines
    return lines
