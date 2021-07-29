from agents import *

from generation import gpt2_operations
from transform import all_lines, single_line, couplet_lines

# all the schedules that will be used in the set of experiments run from `main`
schedules = {
    # 'alpha': [
    #     [single_line, add_sensible_adjectives],
    #     [single_line, alliterate_line_synonymously]
    # ],
    # 'beta': [
    #     [couplet_lines, rhyme_two_lines_synonymously],
    #     [single_line, replace_with_antonym],
    #     [all_lines, couple_existing_rhymes]
    # ],
    # 'gamma': [
    #     [single_line, alliterate_line_synonymously],
    #     [couplet_lines, rhyme_two_lines_synonymously],
    #     [single_line, replace_with_hyponym]
    # ],
    # 'delta': [
    #     [all_lines, swap_conjugates],
    #     [all_lines, couple_existing_rhymes],
    #     [single_line, replace_with_synonym_of_synonym],
    #     [single_line, alliterate_line_synonymously],
    #     [couplet_lines, rhyme_two_lines_synonymously],
    #     [single_line, add_sensible_adjectives],
    #     [single_line, remove_random_adjective]
    # ],
    # 'epsilon': [
    #     [single_line, alliterate_line_synonymously],
    #     [single_line, replace_with_antonym],
    #     [single_line, replace_with_hyponym],
    #     [couplet_lines, rhyme_two_lines_synonymously],
    #     [single_line, replace_with_synonym],
    #     [single_line, replace_with_synonym_of_synonym],
    #     [couplet_lines, rhyme_two_lines_synonymously],
    #     [all_lines, swap_couplets],
    #     [all_lines, punctuation_spacing_correction],
    #     [single_line, remove_random_adjective],
    #     [single_line, add_sensible_adjectives]
    # ],
    'zeta': [
        [all_lines, swap_conjugates],
        [all_lines, couple_existing_rhymes],
        [single_line, replace_with_synonym_of_synonym],
        [single_line, alliterate_line_arbitrarily],
        [couplet_lines, rhyme_two_lines_arbitrarily],
        [single_line, add_sensible_adjectives],
        [single_line, remove_random_adjective]
    ],
    'eta': [
        [single_line, alliterate_line_arbitrarily],
        [couplet_lines, rhyme_two_lines_arbitrarily],
    ],
    'theta': [
        [couplet_lines, equalise_line_length]
    ]
}


class Allocator:

    def __init__(self, samples, schedule_key, max_iterations, quatrain_length, num_quatrains, random_seed=42):
        self.schedule_position = 0
        self.schedule_key = schedule_key
        self.random_seed = random_seed
        self.random_seed = random_seed
        self.max_iterations = max_iterations
        self.iterations = 0
        self.samples = samples
        self.quatrain_length = quatrain_length
        self.num_quatrains = num_quatrains
        self.required_lines = quatrain_length * num_quatrains

    def iterate(self, lines):
        if len(lines) != self.required_lines:
            # finds another appropriate quatrain according to sentiment similarity to add to the as-yet incomplete poem
            lines, self.samples = gpt2_operations.fill_poem(self.random_seed, lines, self.samples, self.required_lines)
            return lines

        # apply the next agent in the schedule
        self.schedule_position += 1
        if self.schedule_position == len(schedules[self.schedule_key]):
            self.schedule_position = 0
            self.iterations += 1
        # extract the pair containing the function which applies the `do` function and the `do` function itself
        [transform_function, expert_function] = schedules[self.schedule_key][self.schedule_position]
        self.random_seed += 1
        return transform_function(expert_function, lines, self.random_seed)
