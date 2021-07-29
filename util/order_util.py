import nltk

tags_before_and = ['PRP$', 'DT', 'JJ', 'NN', 'NNS', 'PRP']


def swap_around_and(line):
    # only used by the `swap_conjugates` agent to intelligently locate the clauses surrounding an 'and' to swap them
    tokens = nltk.word_tokenize(line)
    ands = [and_ for and_ in tokens[1:] if and_ == 'and']
    if len(ands) != 1:
        return line
    tagged = nltk.pos_tag(tokens)
    and_idx = tagged[1:].index(('and', 'CC')) + 1
    l_idx = and_idx - 1
    l_term = ''
    while l_idx >= 0 and tagged[l_idx][1] in tags_before_and:
        l_term = tagged[l_idx][0] + ' ' + l_term
        l_idx -= 1
        if l_idx < 0:
            break
    r_idx = and_idx + 1
    r_term = ''
    while r_idx < len(tagged) and tagged[r_idx][1] in tags_before_and:
        r_term = r_term + ' ' + tagged[r_idx][0]
        r_idx += 1
        if r_idx == len(tagged):
            break
    l_term = l_term.strip()
    r_term = r_term.strip()
    if l_term != '' and r_term != '':
        line = line.replace(l_term, '_').replace(r_term, l_term).replace('_', r_term)
    return line
