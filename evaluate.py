# this module contains the implementation of the policies which dictate a poem's quality.

from collections import defaultdict
from statistics import mean

import nltk

from util import phoneme_util

COMPONENT_SCHEMA = 'poem_id,prompt_id,iterations,schedule,emotion,measure,value,weight,weighted_value'
OVERALL_SCHEMA = 'poem_id,prompt_id,iterations,schedule,emotion,score'

# these weights can be adjusted to emphasise the importance of different component scores when calculating the overall
# quality of a poem
WEIGHTS = {
    'RHYME': 100,
    'ALLITERATION_CHAIN': 50,
    'ALLITERATION_TOTAL': 5,
    'PHONEME': 1
}


def get_rhyme_level_score(couplet):
    # compares how well the words at the ends of each line in a couplet rhyme
    tokens0 = nltk.word_tokenize(couplet[0])
    tokens1 = nltk.word_tokenize(couplet[1])

    if tokens0[-1] == tokens1[-1]:
        return 0  # no score if the words are the same (it's cheating to rhyme a word with itself!)

    phoneme_options0 = phoneme_util.get_phoneme_lists_for_word_using_entries(tokens0[-1])
    phoneme_options1 = phoneme_util.get_phoneme_lists_for_word_using_entries(tokens1[-1])
    phoneme_options0 = phoneme_util.process_phoneme_options(phoneme_options0)
    phoneme_options1 = phoneme_util.process_phoneme_options(phoneme_options1)

    potential_rhyme_scores = []
    for phonemes0 in phoneme_options0:
        for phonemes1 in phoneme_options1:
            potential_rhyme_score = 0
            if not phonemes0 or not phonemes1:
                break
            for i in range(1, min(len(phonemes0), len(phonemes1))):
                if phonemes0[-i] == phonemes1[-i]:
                    potential_rhyme_score += 1
                else:
                    break
            potential_rhyme_scores.append(potential_rhyme_score)
    if not potential_rhyme_scores:
        return 0
    else:
        return mean(potential_rhyme_scores)


def get_alliteration_scores(couplet):
    # calculates the two alliteration-related metrics
    longest_alliteration_chain = 0
    alliteration_total = 0

    for line in couplet:
        tokens = nltk.word_tokenize(line)
        first_phoneme_dictionary = defaultdict(int)
        current_chain_length = 0
        longest_chain_length = 0
        previous_first_phoneme_set = set()
        for i in range(len(tokens)):
            first_phoneme_set = set()
            for phoneme_list in phoneme_util.get_phoneme_lists_for_word_using_entries(tokens[i]):
                first_phoneme_set.add(phoneme_list[0])
            for first_phoneme in first_phoneme_set:
                first_phoneme_dictionary[first_phoneme] += 1
            if previous_first_phoneme_set.intersection(first_phoneme_set):
                current_chain_length += 1
                if current_chain_length > longest_chain_length:
                    longest_chain_length = current_chain_length
                previous_first_phoneme_set = previous_first_phoneme_set.union(first_phoneme_set)
            else:
                current_chain_length = 0
                previous_first_phoneme_set = first_phoneme_set
        alliteration_total += sum([score - 1 for score in first_phoneme_dictionary.values()])
        longest_alliteration_chain += longest_chain_length

    return longest_alliteration_chain, alliteration_total


def get_couplet_phoneme_consistency_score(couplet):
    # a simple magnitude inversely proportional to the difference between the number of phonemes in a couplet
    n_phonemes0 = phoneme_util.get_number_of_phonemes_in_line_using_entries(couplet[0])
    n_phonemes1 = phoneme_util.get_number_of_phonemes_in_line_using_entries(couplet[1])
    return max(0, 10 - abs(n_phonemes0 - n_phonemes1))


def get_couplet_scores(couplet):
    rhyme_level_score = get_rhyme_level_score(couplet)
    longest_alliteration_chain, alliteration_occurrences = get_alliteration_scores(couplet)
    couplet_phoneme_consistency_score = get_couplet_phoneme_consistency_score(couplet)
    return rhyme_level_score, longest_alliteration_chain, alliteration_occurrences, couplet_phoneme_consistency_score


def get_poem_scores(lines):
    # executes all the above functions to collect all the quality scores and return them all in one group
    rhyme_level_scores = []
    longest_alliteration_chains = []
    alliteration_totals = []
    couplet_phoneme_consistency_scores = []
    for i in range(0, len(lines), 2):
        rhyme_level_score, longest_alliteration_chain, alliteration_total, couplet_phoneme_consistency_score = \
            get_couplet_scores([lines[i], lines[i + 1]])
        rhyme_level_scores.append(rhyme_level_score)
        longest_alliteration_chains.append(longest_alliteration_chain)
        alliteration_totals.append(alliteration_total)
        couplet_phoneme_consistency_scores.append(couplet_phoneme_consistency_score)
    mean_rhyme_level_score = mean(rhyme_level_scores)
    mean_longest_alliteration_chain = mean(longest_alliteration_chains)
    mean_alliteration_total = mean(alliteration_totals)
    mean_couplet_phoneme_consistency_score = mean(couplet_phoneme_consistency_scores)
    return \
        mean_rhyme_level_score, mean_longest_alliteration_chain, \
        mean_alliteration_total, mean_couplet_phoneme_consistency_score


def get_poeticity(lines, filename, iterations, schedule):
    # outputs all the quality metrics in a comma-separated value string
    mean_rhyme_level, mean_longest_alliteration_chain, mean_alliteration_total, mean_couplet_phoneme_consistency = \
        get_poem_scores(lines)
    weighted_mean_rhyme_level = mean_rhyme_level * WEIGHTS['RHYME']
    weighted_longest_alliteration_chain = mean_longest_alliteration_chain * WEIGHTS['ALLITERATION_CHAIN']
    weighted_alliteration_total = mean_alliteration_total * WEIGHTS['ALLITERATION_TOTAL']
    weighted_couplet_phoneme_consistency = mean_couplet_phoneme_consistency * WEIGHTS['PHONEME']
    underscored_sections = filename.split('_')
    prompt_id = underscored_sections[0][-1]
    poem_id = underscored_sections[1][len('poem='):]
    emotion = underscored_sections[2][len('emotion='):]
    id_cols = '\n' + poem_id + ',' + prompt_id + ',' + iterations + ',' + schedule + ',' + emotion + ','
    return \
        id_cols + 'mean_rhyme_level,' + str(mean_rhyme_level) + ',' + \
        str(WEIGHTS['RHYME']) + ',' + str(weighted_mean_rhyme_level) + \
        id_cols + 'mean_longest_alliteration_chain,' + str(mean_longest_alliteration_chain) + ',' + \
        str(WEIGHTS['ALLITERATION_CHAIN']) + ',' + str(weighted_longest_alliteration_chain) + \
        id_cols + 'mean_alliteration_total,' + str(mean_alliteration_total) + ',' + \
        str(WEIGHTS['ALLITERATION_TOTAL']) + ',' + str(weighted_alliteration_total) + \
        id_cols + 'mean_couplet_phoneme_consistency,' + str(mean_couplet_phoneme_consistency) + \
        ',' + str(WEIGHTS['PHONEME']) + ',' + str(weighted_couplet_phoneme_consistency), \
        id_cols + str(weighted_mean_rhyme_level + weighted_longest_alliteration_chain + weighted_alliteration_total +
                      weighted_couplet_phoneme_consistency)
