# ---------------------------------------------------------------------
#
# Seed Vault Diamond Collection Simulation
#  - Determines average days between diamond productions from a level 100 SV
#  - Graphs distribution probabilities
#
# ---------------------------------------------------------------------
#
# Code written by UBERnerd14. See https://www.youtube.com/@UBERnerd14
# Join my Discord server: https://ubernerd14.com/join
#
# ---------------------------------------------------------------------
#
# Change these options to build a custom simulation!

trials = 10000          # How many simulations of SV aids to run
successful_aids = 250   # How many aids

# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

t = 0
total_hits = 0
n_values = []

while t < trials:
    n = 1

    while random.randint(1000000) > 1598:
        n = n + 1

    total_hits = total_hits + n
    n_values.append(n)

    t = t + 1
# print(t)
avg_n = total_hits / t
print(avg_n)
print(avg_n / successful_aids)

min_n = min(n_values)
max_n = max(n_values)
bins = np.arange(min_n - 0.5, max_n + 1.5, 1)

avg_n = total_hits / t

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(n_values, bins=bins, density=True)
ax1.axvline(avg_n, linestyle='dashed', color='red', label=f'Average = {avg_n:.3f}')
ax1.set_xlabel("Number of Collections")
ax1.set_ylabel("Probability")
ax1.set_title("Collections Between Diamonds")
ax1.legend()

sorted_n = np.sort(n_values)
cdf = np.arange(1, len(sorted_n) + 1) / len(sorted_n)

ax2.plot(sorted_n, cdf)
ax2.set_xlabel("Number of Collections")
ax2.set_ylabel("Cumulative Probability")
ax2.set_title("Cumulative Distribution")
ax2.axvline(avg_n, linestyle='dashed', color='red', label=f'Average = {avg_n:.3f}')
ax2.legend()

plt.show()
