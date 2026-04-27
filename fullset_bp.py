# ---------------------------------------------------------------------
#
# Blueprints per Full Set Simulation
#  - Determines the average number of blueprints needed to assemble a
#    full set of 9 unique BP
#  - Graphs the distribution of required blueprints
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

# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

t = 0
total_bp = 0
n_values = []

while t < trials:
    bp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    n = 0

    while 0 in bp:
        x = random.randint(3)
        y = random.randint(3)

        bp[x, y] = bp[x, y] + 1
        n = n + 1

    total_bp = total_bp + n
    n_values.append(n)

    t = t + 1
print(t)
avg_n = total_bp / t
print(avg_n)

min_n = min(n_values)
max_n = max(n_values)
bins = np.arange(min_n - 0.5, max_n + 1.5, 1)

avg_n = total_bp / t

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(n_values, bins=bins, density=True)
ax1.axvline(avg_n, linestyle='dashed', color='red', label=f'Average = {avg_n:.3f}')
ax1.set_xlabel("Number of Blueprints Collected")
ax1.set_ylabel("Probability")
ax1.set_title("Distribution of Blueprints Collected per Full Set")
ax1.legend()

sorted_n = np.sort(n_values)
cdf = np.arange(1, len(sorted_n) + 1) / len(sorted_n)

ax2.plot(sorted_n, cdf)
ax2.set_xlabel("Number of Blueprints collected")
ax2.set_ylabel("Cumulative Probability")
ax2.set_title("Cumulative Distribution")
ax2.axvline(avg_n, linestyle='dashed', color='red', label=f'Average = {avg_n:.3f}')
ax2.legend()

plt.show()