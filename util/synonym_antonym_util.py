# uses the nltk wordnet to retrieve synonyms and antomyms for a given word

from nltk.corpus import wordnet


def get(word, mode):
    # inspired by the work of Colin Johnson (https://scholar.google.com/citations?hl=en&user=6W7BtygAAAAJ)
    words = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            if mode == 'synonyms':
                words.add(lemma.name().replace('_', ' '))
            elif mode == 'antonyms':
                if lemma.antonyms():
                    words.add(lemma.antonyms()[0].name().replace('_', ' '))
    if word in words:
        words.remove(word)
    return sorted(list(words))


def get_synonyms_for_word(word):
    # used by many agents which aim to maintain semantics when trying to maximise other quality components like
    # alliteration or rhyme
    return get(word, 'synonyms')


def get_antonyms_for_word(word):
    # used by the `replace_with_antonym` agent
    return get(word, 'antonyms')
