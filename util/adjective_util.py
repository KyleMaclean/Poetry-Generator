# provides adjective-related functions to the agents so that multiple agents can share the same code

import random

import nltk
from nltk import ngrams
from nltk.corpus import brown

from util import tagsets


def get_indices_of_adjacent_adjectives(line):
    tagged_words = nltk.pos_tag(nltk.word_tokenize(line))
    adjective_indices = [i for i, v in enumerate(tagged_words) if v[1] in tagsets.adjectives]
    adjacent_indices = []
    for index in adjective_indices:
        adjacent_group = set()
        while True:
            if index + 1 in adjective_indices:
                adjacent_group.add(index)
                adjacent_group.add(index + 1)
                index += 1
            if tagged_words[index + 1][1] == ',' and index + 2 in adjective_indices:
                adjacent_group.add(index)
                adjacent_group.add(index + 2)
                index += 2
            else:
                break
        adjacent_indices.append(adjacent_group)
    return adjacent_indices


def remove_adjective(line):
    # inspired by the work of Colin Johnson (https://scholar.google.com/citations?hl=en&user=6W7BtygAAAAJ)
    tagged_words = nltk.pos_tag(nltk.word_tokenize(line))
    adjective_indices = [i for i, v in enumerate(tagged_words) if v[1] in tagsets.adjectives]
    if not adjective_indices:
        return line
    del tagged_words[random.choice(adjective_indices)]
    return ' '.join([tag[0] for tag in tagged_words])


def add_adjectives(line, random_seed=42):
    # inspired by the work of Colin Johnson (https://scholar.google.com/citations?hl=en&user=6W7BtygAAAAJ)
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    noun_positions = [noun_position for noun_position, noun in enumerate(tagged) if noun[1] in tagsets.nouns]
    if not noun_positions:
        return line
    for i in range(len(noun_positions)):
        chosen_noun = tagged[noun_positions[i]][0]
        chosen_noun_position = tokens.index(chosen_noun)
        if chosen_noun_position - 1 >= 0 and tagged[chosen_noun_position - 1][1] in tagsets.adjectives:
            continue
        else:
            pre_words = [bg[0] for bg in ngrams(brown.words(), 2) if bg[1] == chosen_noun]
            tagged_pre_words = nltk.pos_tag(pre_words)
            adjectives = [pw[0] for pw in tagged_pre_words if (pw[1] in tagsets.adjectives)]
            if not adjectives:
                return line
            random.seed(random_seed)
            random_adjective_index = random.randrange(len(adjectives))
            random_adjective = adjectives[random_adjective_index].lower()
            if tokens[chosen_noun_position - 1] != random_adjective and \
                    tokens[chosen_noun_position] != random_adjective:
                tokens.insert(chosen_noun_position, adjectives[random_adjective_index].lower())
            return ' '.join(tokens)
    return line
