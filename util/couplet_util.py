from util import rhyme_util, synonym_antonym_util, phoneme_util


# get rhyming words from either of the two corpora for the last word in the first line of a couplet
def get_rhyming_words_using_9802(couplet):
    return rhyme_util.get_rhyming_words_for_phonemes(
        phoneme_util.get_applicable_words_starting_with_phoneme_using_9802(couplet[0].split(' ')[-1]))


def get_rhyming_words_using_entries(couplet):
    return rhyme_util.get_rhyming_words_for_phonemes(
        phoneme_util.get_phoneme_lists_for_word_using_entries(couplet[0].split(' ')[-1]))


# used by the `rhyme_two_lines_synonymously` agent to find words that rhyme with the last word in the first line of the
# couplet and are synonyms of the last word in the second line of the couplet to replace it
def get_intersection_using_entries(couplet):
    # inspired by the work of Colin Johnson (https://scholar.google.com/citations?hl=en&user=6W7BtygAAAAJ)
    rhyming_words = get_rhyming_words_using_entries(couplet)
    synonymous_words = synonym_antonym_util.get_synonyms_for_word(couplet[1].split(' ')[-1])
    return [word for word in rhyming_words if word in synonymous_words]
