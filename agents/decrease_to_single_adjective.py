import nltk

from util import adjective_util


def do(line):
    # inspired by the work of Colin Johnson (https://scholar.google.com/citations?hl=en&user=6W7BtygAAAAJ)
    tokens = nltk.word_tokenize(line)
    adjacent_adjective_indices = adjective_util.get_indices_of_adjacent_adjectives(line)
    for adjacent_group in adjacent_adjective_indices:
        while len(adjacent_group) > 1:
            index = adjacent_group.pop()
            del tokens[index]
    if ',' in tokens:
        comma_index = tokens.index(',')
        del tokens[comma_index]
    return ' '.join(tokens)
