# adds a single adjective before each noun
from util import adjective_util


def do(line, random_seed=42):
    return adjective_util.add_adjectives(line, random_seed)
