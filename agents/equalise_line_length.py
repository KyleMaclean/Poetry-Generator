import random

import nltk

import util.tagsets
from util import phoneme_util, adjective_util, synonym_antonym_util
from util.phoneme_util import quickly_get_phonemes_for_word_using_entries

EPSILON = 3


def change_length_with_synonym(line, mode, random_seed):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    random_indices = list(range(len(tokens)))
    random.seed(random_seed)
    random.shuffle(random_indices)
    for i in random_indices:
        if tagged[i][1] in util.tagsets.replaceable:
            synonyms = synonym_antonym_util.get_synonyms_for_word(tokens[i])
            if synonyms:
                if mode == 'min':
                    chosen_synonym = min(synonyms, key=len)
                elif mode == 'max':
                    chosen_synonym = max(synonyms, key=len)
                else:
                    raise ValueError('supported synonym choosing modes: `min` and `max`')
                tokens[i] = synonyms[synonyms.index(chosen_synonym)]
                return ' '.join(tokens)


def chop_line(long_line, num_phonemes):
    phonemes_to_chop = max(num_phonemes) - min(num_phonemes)
    tokens = nltk.word_tokenize(long_line)
    reversed_long_line = tokens[-1::-1]
    line_sum = 0
    count = 0
    for word in reversed_long_line:
        phonemes_for_word = quickly_get_phonemes_for_word_using_entries(word)
        if phonemes_for_word:
            len_word = len(phonemes_for_word)
        else:
            len_word = 0
        if line_sum + len_word >= phonemes_to_chop:
            pre_diff = abs(line_sum - phonemes_to_chop)
            post_diff = abs(line_sum + len_word - phonemes_to_chop)
            if post_diff < pre_diff:
                count += 1
            break
        count += 1
        line_sum += len_word
    reversed_long_line = reversed_long_line[count:]
    return ' '.join(reversed_long_line[-1::-1])


def do(couplet):
    random_seed = random.randrange(0, 100, 1)
    attempts = 0
    while True:
        attempts += 1
        num_phonemes = [phoneme_util.get_number_of_phonemes_in_line_using_entries(couplet[0]),
                        phoneme_util.get_number_of_phonemes_in_line_using_entries(couplet[1])]
        if num_phonemes[0] + EPSILON < num_phonemes[1] or num_phonemes[1] + EPSILON < num_phonemes[0]:
            if num_phonemes[0] + EPSILON < num_phonemes[1]:
                short_line_index = 0
                long_line_index = 1
            else:
                short_line_index = 1
                long_line_index = 0
            if attempts == 1:
                couplet[short_line_index] = adjective_util.add_adjectives(couplet[short_line_index])
            elif attempts == 2:
                couplet[long_line_index] = adjective_util.remove_adjective(couplet[long_line_index])
            elif attempts == 3:
                couplet[short_line_index] = change_length_with_synonym(couplet[short_line_index], 'max', random_seed)
            elif attempts == 4:
                couplet[long_line_index] = change_length_with_synonym(couplet[long_line_index], 'min', random_seed)
            elif attempts == 5:
                couplet[long_line_index] = chop_line(couplet[long_line_index], num_phonemes)
            else:
                return couplet
        else:
            return couplet
