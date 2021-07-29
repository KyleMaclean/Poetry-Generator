import re


def do(lines):
    for i in range(len(lines)):
        lines[i] = re.sub(r'\s([,?.!"])', r'\1', lines[i])
    return lines
