import experiment
from allocator import schedules
from blackboard import Blackboard
from generation.gpt2_operations import *
from generation.pre_generated_prompts import PRE_GENERATED_PROMPTS

QUATRAIN_LENGTH = 4
NUM_QUATRAINS = 4
ITERATIONS = [10]
GENERATE_NEW_PROMPTS = False
PROMPT_ID = 0
RANDOM_SEEDS = [50]
N_PROMPTS = 25
EVALUATE_OUTPUT_DIRECTORY = True

if GENERATE_NEW_PROMPTS and PROMPT_ID != 0:
    raise ValueError('Only one dictionary of prompts can be generated at a time, so to generate new prompts, set '
                     'PROMPT_ID = 0, or choose an index for one of the desired PRE_GENERATED_PROMPTS dictionaries')

for random_seed in RANDOM_SEEDS:
    for iteration in ITERATIONS:
        # the number of iterations will be recorded in the output CSVs which also record quality scores
        for schedule_key in schedules:
            # an experiment with every schedule listed in `allocator.py` will be conducted
            samples = load_sample_quatrains(QUATRAIN_LENGTH)
            if GENERATE_NEW_PROMPTS:
                # generate a new random dictionary of prompts for 25 emotions
                prompts = [get_n_prompts(samples, N_PROMPTS, QUATRAIN_LENGTH)]
            else:
                # choose a pre-generated random dictionary of prompts for 25 emotions by setting PROMPT_ID:
                prompts = PRE_GENERATED_PROMPTS
            print('Applying schedule:', schedule_key, '...')
            for prompt_key in prompts[PROMPT_ID]:
                bb = Blackboard(prompts[PROMPT_ID][prompt_key],
                                samples, schedule_key, iteration, QUATRAIN_LENGTH, NUM_QUATRAINS, random_seed)
                lines, samples = bb.run()
                experiment.write_poem(
                    prompt_key, lines, schedule_key, QUATRAIN_LENGTH, NUM_QUATRAINS, PROMPT_ID, iteration)
                bb.root.mainloop()

if EVALUATE_OUTPUT_DIRECTORY:
    experiment.evaluate_all_poems()
