import copy
import random

import nltk

from agents import replace_with_synonym
from util import synonym_antonym_util


def do(line, random_seed=42):
    new_line = replace_with_synonym(copy.deepcopy(line))
    new_line_tokens = nltk.word_tokenize(new_line)
    line_tokens = nltk.word_tokenize(line)
    new_line_difference = list(set(new_line_tokens) - set(line_tokens))
    if not new_line_difference:
        return line
    synonym = new_line_difference[0]
    i = new_line_tokens.index(synonym)
    synonyms = synonym_antonym_util.get_synonyms_for_word(new_line_tokens[i])
    if synonyms:
        random.seed(random_seed)
        random_synonym_index = random.randrange(len(synonyms))
        new_line_tokens[i] = synonyms[random_synonym_index]
        return ' '.join(new_line_tokens)
    return line
