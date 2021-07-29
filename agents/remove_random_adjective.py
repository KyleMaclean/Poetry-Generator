# has a tunable chance to remove one adjective from a random line
from util import adjective_util


def do(line):
    return adjective_util.remove_adjective(line)
