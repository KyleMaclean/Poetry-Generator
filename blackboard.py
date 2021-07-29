# maintains the state of the poem's lines and draws a visualisation of how the agents successively transform the poem.
# when the poem is still being populated, the

import time
import tkinter
from copy import deepcopy

import allocator

Y_SPACING = 20
X_OFFSET = 15
SLEEP_TIME = 1
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 1000
FONT = 'Times'


class Blackboard:

    def __init__(self, lines, samples, schedule_key, max_iterations, quatrain_length, num_quatrains, random_seed=42):
        self.stats = []
        self.lines = lines
        self.changed_lines = []
        self.quatrain_length = quatrain_length
        self.num_quatrains = num_quatrains
        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()
        self.allocator = allocator.Allocator(samples, schedule_key, max_iterations, quatrain_length, num_quatrains,
                                             random_seed=random_seed)

    def run(self):
        while self.allocator.iterations < self.allocator.max_iterations:
            # continually transforms the lines using the schedule of agents until the number of iterations is reached
            self.compute_stats()
            self.populate()
            self.root.update_idletasks()
            self.root.update()
            copy_of_lines = deepcopy(self.lines)
            # either fills the poem with lines to complete it or transforms the lines of a completed poem
            self.allocator.iterate(copy_of_lines)
            if len(copy_of_lines) == len(self.lines):
                self.changed_lines = []
                for i in range(len(copy_of_lines)):
                    if copy_of_lines[i] != self.lines[i]:
                        self.changed_lines.append((i, self.lines[i]))
            self.lines = copy_of_lines
            time.sleep(SLEEP_TIME)

        # all iterations have finished, so the lines are returned for writing to file
        self.root.destroy()
        for i in range(len(self.lines)):
            if not self.lines[i]:
                self.lines[i] = '...'  # if the line was emptied by an agent, then use an ellipsis to denote it
        return self.lines, self.allocator.samples

    def compute_stats(self):
        self.stats = [' '] * 4
        if len(self.lines) < self.quatrain_length * self.num_quatrains:
            # if the poem is not yet complete, the stats show the progress to completion
            self.stats = ['Waiting for prompt ...', 'Waiting for quatrain 2 ...',
                          'Waiting for quatrain 3 ...', 'Waiting for quatrain 4 ...']
            if len(self.lines) >= self.quatrain_length * (self.num_quatrains - 3):
                self.stats[0] = 'Received prompt!'
            if len(self.lines) >= self.quatrain_length * (self.num_quatrains - 2):
                self.stats[1] = 'Received quatrain 2!'
            if len(self.lines) >= self.quatrain_length * (self.num_quatrains - 1):
                self.stats[2] = 'Received quatrain 3!'
        else:
            # if the poem is full with the requisite number of lines, current schedule/iteration progress is displayed
            schedule = allocator.schedules[self.allocator.schedule_key]
            self.stats[0] = 'schedule: ' + str(self.allocator.schedule_key)
            self.stats[1] = 'iteration: ' + str(self.allocator.iterations) + ' / ' + str(self.allocator.max_iterations)
            self.stats[2] = 'agent position: ' + str(self.allocator.schedule_position) + ' / ' + str(len(schedule) - 1)
            self.stats[3] = 'agent name: ' + str(schedule[self.allocator.schedule_position][1].__module__).split('.')[1]

    def populate(self):
        # sequentially writes each component of the GUI including the statistics and visualisations for the user
        self.canvas.delete('all')

        y_offset = Y_SPACING
        for stat in self.stats:
            self.canvas.create_text(X_OFFSET, y_offset, font=FONT, text=stat, anchor=tkinter.W, fill='blue')
            y_offset += Y_SPACING
        y_offset += Y_SPACING
        for i in range(self.quatrain_length * self.num_quatrains):
            text = str(i + 1)
            fill = 'black'  # all poem lines which have not been altered are black
            if i < len(self.lines):
                text += '\t' + self.lines[i]
                for pair in self.changed_lines:
                    if pair[0] == i:
                        fill = 'green'  # a line which the last agent successfully transformed will be green
            self.canvas.create_text(X_OFFSET, y_offset, font=FONT, text=text, anchor=tkinter.W, fill=fill)
            y_offset += Y_SPACING
            if (i + 1) % self.quatrain_length == 0:  # separate quatrains with an extra line space
                y_offset += Y_SPACING
        if self.changed_lines:
            # the previous state of all the lines which were transformed by the last agent are shown in red
            self.canvas.create_text(X_OFFSET, y_offset, font=FONT, text='Replaced:', anchor=tkinter.W, fill='red')
            for pair in self.changed_lines:
                y_offset += Y_SPACING
                stats = str(pair[0] + 1) + '\t' + pair[1]
                self.canvas.create_text(X_OFFSET, y_offset, font=FONT, text=stats, anchor=tkinter.W, fill='red')
