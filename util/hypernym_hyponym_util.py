from itertools import chain

from nltk.corpus import wordnet


def get_hypernyms(word):
    return list(chain(*[lemma.lemma_names() for lemma in wordnet.synsets(word)[0].hyprtnyms()]))


def get_hyponyms(word):
    synset_for_word = wordnet.synsets(word)
    if synset_for_word:
        return list(chain(*[lemma.lemma_names() for lemma in synset_for_word[0].hyponyms()]))
    return []
