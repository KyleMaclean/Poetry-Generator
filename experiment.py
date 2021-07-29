# this module is a wrapper which handles outputting to the filesystem in a structured way to enable many experimental
# parameters to be evaluated in a single run and easily navigate the results. applies the `evaluate` module's policies
# and tags each poem's file name with its metadata.

import os
from datetime import datetime

import evaluate

OUTPUT_DIR = 'output/'
POEM_DIR = OUTPUT_DIR + 'poems/'


# noinspection PyUnresolvedReferences,PyTypeChecker
def evaluate_all_poems():
    for poem_dir_item in os.scandir(POEM_DIR):
        if poem_dir_item.is_dir():
            for iteration_dir_item in os.scandir(poem_dir_item):
                if iteration_dir_item.is_dir():
                    iterations_schedule = iteration_dir_item.path.split('/')[-1].split('\\')  # for Windows
                    print('Evaluating:', iterations_schedule[0], iterations_schedule[1], '...')
                    evaluated = 0
                    for file_name in os.listdir(iteration_dir_item.path):
                        full_file_name = os.path.join(iteration_dir_item.path, file_name)
                        if os.path.isfile(full_file_name):
                            iterations = iterations_schedule[0][len('iterations='):]
                            schedule = iterations_schedule[1][len('schedule='):]
                            write_evaluation(iterations, schedule, full_file_name)
                            print(str(evaluated), end=' ')
                            evaluated += 1
                    print('\n')


def write_evaluation(iterations, schedule, file):
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    component_results_path = OUTPUT_DIR + 'component-results.csv'
    overall_results_path = OUTPUT_DIR + 'overall-results.csv'

    if not os.path.isfile(component_results_path):
        with open(component_results_path, 'w', encoding='utf8') as component_file:
            component_file.write(evaluate.COMPONENT_SCHEMA)

    if not os.path.isfile(overall_results_path):
        with open(overall_results_path, 'a', encoding='utf8') as overall_file:
            overall_file.write(evaluate.OVERALL_SCHEMA)

    with open(file, encoding='utf8') as poem_file:
        lines = poem_file.readlines()
        filename, _ = os.path.splitext(file)
        component_results, overall_results = evaluate.get_poeticity(lines, filename, iterations, schedule)

        with open(component_results_path, 'a', encoding='utf8') as component_file:
            component_file.write(component_results)
        with open(overall_results_path, 'a', encoding='utf8') as overall_file:
            overall_file.write(overall_results)


def write_poem(emotion, lines, schedule_key, quatrain_length, num_quatrains, prompt_id, iterations):
    if not os.path.isdir('output/'):
        os.mkdir('output/')
    if len(lines) != num_quatrains * quatrain_length:
        raise ValueError('poems must be', num_quatrains, '*', quatrain_length, 'lines long')
    if not os.path.isdir(POEM_DIR):
        os.mkdir(POEM_DIR)
    poem_iterations_dir = POEM_DIR + 'iterations=' + str(iterations) + '/'
    if not os.path.isdir(poem_iterations_dir):
        os.mkdir(poem_iterations_dir)
    schedule_dir = poem_iterations_dir + 'schedule=' + schedule_key + '/'
    if not os.path.isdir(schedule_dir):
        os.mkdir(schedule_dir)
    with open(schedule_dir + 'prompt=' + str(prompt_id) + '_poem=' +
              datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_emotion=' + emotion + '.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(lines)[:-1])
