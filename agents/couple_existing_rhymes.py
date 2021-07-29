import nltk

from util import phoneme_util
from util.rhyme_util import RHYME_LEVEL


def flatten(rhyme_pairs):
    flat = []
    for rhyme_pair in rhyme_pairs:
        flat.append(rhyme_pair[0])
        flat.append(rhyme_pair[1])
    return flat


def do(lines):
    all_phoneme_options = []
    for i in range(len(lines)):
        tokens_i = nltk.word_tokenize(lines[i])
        new_phoneme_options = phoneme_util.get_phoneme_lists_for_word_using_entries(tokens_i[-1])
        truncated_phoneme_options = [truncated[-RHYME_LEVEL:] for truncated in new_phoneme_options]
        all_phoneme_options.append(truncated_phoneme_options)
    non_couplet_rhymes = set()
    couplet_rhymes = set()
    for i, phoneme_options_i in enumerate(all_phoneme_options):
        for j, phoneme_options_j in enumerate(all_phoneme_options):
            if i == j:
                continue
            for phonemes_i in phoneme_options_i:
                for phonemes_j in phoneme_options_j:
                    if phonemes_i == phonemes_j:
                        if i + 1 == j or i - 1 == j:
                            couplet_rhymes.add(tuple(sorted([i, j])))
                        else:
                            non_couplet_rhymes.add(tuple(sorted([i, j])))
    flattened_couplet_rhymes = flatten(couplet_rhymes)
    for non_couplet_rhyme in non_couplet_rhymes:
        if non_couplet_rhyme[0] not in flattened_couplet_rhymes:
            line = lines.pop(non_couplet_rhyme[1])
            lines.insert(non_couplet_rhyme[0] + 1, line)
    return lines
