# noinspection PyUnresolvedReferences
from generation.cmu_dict_without_emphasis import custom_entries

RHYME_LEVEL = 2


def get_rhyming_words_for_phonemes(phoneme_options, rhyme_level=RHYME_LEVEL):
    # agents which want rhyming words for a certain word will first derive the phonemes for that word with another
    # utility and then submit those phonemes to this function to finally get rhyming words
    rhyming_words = []
    for phonemes in phoneme_options:
        if phonemes:
            rhyming_words += [word for word, phonemes_ in custom_entries
                              if phonemes_[-rhyme_level:] == phonemes[-rhyme_level:]]
    return rhyming_words
