# functions to apply the three kinds of agents: those that work on single lines, those that work on a couplet
# and those that work on all the lines of the poem. each receives an agent's `do` function and selects the
# appropriate number of lines from the `lines` parameter, which contains the entire current poem to be transformed

import random


def single_line(agent, lines, random_seed, mode='any'):
    # by default, any random line is chosen but `last_in_random_quatrain` chooses the last line in a random quatrain
    random_seed += 1
    random.seed(random_seed)
    if mode == 'any':
        index = random.randrange(len(lines))
    elif mode == 'last_in_random_quatrain':
        random_quatrain_index = random.randrange(len(lines))
        index = random_quatrain_index * 4 + 3
    else:
        raise ValueError('mode', mode, 'not supported in transform.single_line()')
    new_line = agent(lines[index])
    lines[index] = new_line
    return lines


def couplet_lines(agent, lines, random_seed):
    random.seed(random_seed)
    if len(lines) < 2:
        raise IndexError
    random_index = random.randrange(0, len(lines) // 2) * 2
    if random_index % 2 == 0:
        index0 = random_index
        index1 = random_index + 1
    else:
        index0 = random_index - 1
        index1 = random_index
    couplet = agent([lines[index0], lines[index1]])
    lines[index0] = couplet[0]
    lines[index1] = couplet[1]
    return lines


# noinspection PyUnusedLocal
def all_lines(agent, lines, unused):
    # random_seed parameter is not used but we require the same function signature as those above
    return agent(lines)
