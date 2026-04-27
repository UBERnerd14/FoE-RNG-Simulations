# ---------------------------------------------------------------------
#
# Blueprint Range Distribution Simulation
#  - Determines the average range of blueprints (slot with most - slot with min)
#    for a given maximum number of sets of blueprints
#  - Graphs the average range for each number of sets of blueprints
# 
#  Note: Sets of blueprints are not the same as a given level of a great building.
#        The sets required for a given level are: 
#           1, for levels 0-10
#           level - 9, for levels >10
#
# ---------------------------------------------------------------------
#
# Code written by UBERnerd14. See https://www.youtube.com/@UBERnerd14
# Join my Discord server: https://ubernerd14.com/join
#
# ---------------------------------------------------------------------
#
# Change these options to build a custom simulation!

trials = 1000   # Number of trials to run for each amount of sets
                # Note: A large number here will result in long runtime
                #       I was lazy with implementation :D
max_set = 80    # Maximum number of sets of blueprints to simulate to

# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

ranges = []

sets = 0
while sets < max_set:

    t = 0

    total_range = 0
    range_values = []

    while t < trials:
        bp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        n = 0

        while np.any(bp < sets):
            x = random.randint(3)
            y = random.randint(3)
            # print(x, ",", y)

            bp[x, y] = bp[x, y] + 1
            n = n + 1
        # print(bp)
        # print(n)
        n_range = bp.max() - bp.min()

        total_range = total_range + n_range
        range_values.append(n_range)

        t = t + 1
    avg_range = total_range / t
    ranges.append(avg_range)

    sets = sets + 1

x = np.linspace(1, max_set, max_set)
# print(x)
# print(ranges)

fig, ax = plt.subplots()
plt.plot(x, ranges, "-o")
plt.xlabel("Unique Sets of BP")
plt.ylabel("Average Range of Max-Min BP")
plt.title("Range of BP per Unique Set")
plt.show()
