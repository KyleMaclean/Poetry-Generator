# replaces 'a' with 'an' and vice versa as is grammatically appropriate

import nltk


def do(lines):
    # inspired by the work of Colin Johnson (https://scholar.google.com/citations?hl=en&user=6W7BtygAAAAJ)
    pronunciation_dictionary = nltk.corpus.cmudict.dict()
    for i in range(len(lines)):
        tokens = nltk.word_tokenize(lines[i])
        for j, word in enumerate(tokens):
            if (word == 'a' or word == 'an') and j < len(tokens) - 1:
                next_word = tokens[j + 1]
                if next_word not in pronunciation_dictionary.keys():
                    first_char = next_word[0]
                else:
                    first_char = pronunciation_dictionary[next_word][0][0][0]
                vowels = ['A', 'E', 'I', 'O', 'U']
                if first_char in vowels and word == 'a':
                    tokens[j] = 'an'
                elif first_char not in vowels and word == 'an':
                    tokens[j] = 'a'
        lines[i] = ' '.join(tokens)
    return lines
