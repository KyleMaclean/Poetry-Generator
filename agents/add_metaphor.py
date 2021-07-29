import random
from urllib.request import Request, urlopen

import nltk

# noinspection HttpUrlsUsage
REQUEST_URL = 'http://bonnat.ucd.ie/jigsaw/index.jsp?q='


def do(line, random_seed=42):
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)
    adjectives = [(index, word) for index, (word, tag) in enumerate(tagged) if tag == 'JJ']
    metaphors = {}
    for adjective in adjectives:
        with urlopen(Request(REQUEST_URL + adjective[1])) as response:
            metaphors[adjective[0]] = list(map(
                lambda x: x.split("\">")[0], str(response.read()).split('longvehicle=')))[1:]
    random.seed(random_seed)
    keys = list(metaphors.keys())
    random.shuffle(keys)
    for key in keys:
        choice = metaphors[key]
        if choice:
            metaphor = random.choice(choice)
            tokens[key:key + 1] = tokens[key], 'as', metaphor
            return ' '.join(tokens)
    return ' '.join(tokens)
