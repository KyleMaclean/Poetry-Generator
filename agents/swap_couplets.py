import random


def do(lines, random_seed=42):
    couplets = []
    n_couplets = len(lines) // 2
    for i in range(n_couplets):
        couplets.append([lines[2 * i], lines[2 * i + 1]])
    random.seed(random_seed)
    random_index = random.randrange(0, len(couplets) - 1)
    temp = couplets[random_index]
    couplets[random_index] = couplets[random_index + 1]
    couplets[random_index + 1] = temp
    new_lines = []
    for couplet in couplets:
        new_lines.append(couplet[0])
        new_lines.append(couplet[1])
    if len(lines) % 2 != 0:
        new_lines.append(lines[-1])
    return new_lines
