# swaps the order of a conjugate from a random line
import random

from util import order_util


def do(lines, random_seed=42):
    indices = list(range(len(lines)))
    random.seed(random_seed)
    random.shuffle(indices)
    for i in indices:
        if 'and' in lines[i]:
            lines[i] = order_util.swap_around_and(lines[i])
            return lines
    return lines
