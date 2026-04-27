# ---------------------------------------------------------------------
#
# Blueprint Range Distribution Simulation (per specific set)
#  - Determines the average range of blueprints (slot with most - slot with min)
#    for a given number of sets of blueprints
#  - Graphs the distribution of blueprint ranges
# 
# ---------------------------------------------------------------------
#
# Code written by UBERnerd14. See https://www.youtube.com/@UBERnerd14
# Join my Discord server: https://ubernerd14.com/join
#
# ---------------------------------------------------------------------
#
# Change these options to build a custom simulation!

trials = 10000  # Number of simulations to run
sets = 100      # The number of sets of blueprints you want to simulate to

# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

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
print(t)
avg_n = total_range / t
print(avg_n)

min_n = min(range_values)
max_n = max(range_values)
bins = np.arange(min_n - 0.5, max_n + 1.5, 1)

avg_n = total_range / t

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(range_values, bins=bins, density=True)
ax1.axvline(avg_n, linestyle='dashed', color='red', label=f'Average = {avg_n:.3f}')
ax1.set_xlabel("Range of highest BP to lowest BP count")
ax1.set_ylabel("Probability")
ax1.set_title(f"Distribution of BP Range for {sets} sets of BP")
ax1.legend()

sorted_n = np.sort(range_values)
cdf = np.arange(1, len(sorted_n) + 1) / len(sorted_n)

ax2.plot(sorted_n, cdf)
ax2.set_xlabel("Range of highest BP to lowest BP count")
ax2.set_ylabel("Cumulative Probability")
ax2.set_title("Cumulative Distribution")
ax2.axvline(avg_n, linestyle='dashed', color='red', label=f'Average = {avg_n:.3f}')
ax2.legend()

plt.show()