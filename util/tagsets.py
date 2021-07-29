# the Parts of Speech which make sense to replace (as counter-examples, we do not replace: pronouns, determiners, etc.)
replaceable = ['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNPS', 'NNS', 'RB', 'RBR', 'RBS', 'UH', 'VB', 'VBD', 'VBG',
               'VBN', 'VBP', 'VBZ', ]

# used in the nouns and adjectives utilities as a definition of the forms that adjective Parts of Speech tags can take
nouns = ['NNP', 'NNPS', 'NN', 'NNS']
adjectives = ['JJ', 'JJR', 'JJS']

# Parts of Speech which are appropriate to replace with hyponyms/hypernyms; used by the `replace_with_hyponym` agent
noun_and_proper_noun_tagset = ['NNP', 'NNPS', 'NN', 'NNS']