# ---------------------------------------------------------------------
#
# Guild Battlegrounds Attrition Simulation
#  - Determines average fights for a given max attrition
#  - Graphs distributions of fight number probabilities
#  - Graphs fight increase lines
#
# ---------------------------------------------------------------------
#
# Code written by UBERnerd14. See https://www.youtube.com/@UBERnerd14
# Join my Discord server: https://ubernerd14.com/join
#
# ---------------------------------------------------------------------
#
# Change these options to build a custom simulation!

max_att = 150       # What attrition value you want the sim to stop at
att_chance = .2     # Attrition increase chance (0.2 is the minimum)
trials = 1000       # How many simulations of attrition to run

# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from numpy import random

t = 0
total_fights = 0
fight_vals = []

fig, ax = plt.subplots()

while t < trials:
    x = []
    y = []

    att = 0
    while att < max_att:
        if random.randint(int(1/att_chance)) == 0:
            att = att + 1
        x.append(len(x)+1)
        y.append(att)

    plt.plot(x, y, alpha=.025, linewidth=1.5, color="tab:blue")
    t = t + 1
    fight_vals.append(len(x))
    total_fights = total_fights + len(x)

plt.xlabel("Fights")
plt.ylabel("Attrition")
plt.title(f"Attrition Gain to {max_att}")

fights_avg = total_fights / trials
print(fights_avg)

x = np.linspace(1, fights_avg)
y = np.linspace(0, max_att)
plt.plot(x, y, color="red", linestyle="--", label=f'Average = {fights_avg:.3f}')
plt.legend()


# the next graph set thingy!

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(fight_vals, bins=30, density=True)
ax1.axvline(fights_avg, linestyle='dashed', color='red', label=f'Average = {fights_avg:.3f}')
ax1.set_xlabel("Number of Fights")
ax1.set_ylabel("Probability")
ax1.set_title(f"Distribution of Fights Required to Reach {max_att} Attrition")
ax1.legend()

sorted_n = np.sort(fight_vals)
cdf = np.arange(1, len(sorted_n) + 1) / len(sorted_n)

ax2.plot(sorted_n, cdf)
ax2.set_xlabel("Number of Fights")
ax2.set_ylabel("Cumulative Probability")
ax2.set_title("Cumulative Distribution")
ax2.axvline(fights_avg, linestyle='dashed', color='red', label=f'Average = {fights_avg:.3f}')
ax2.legend()



plt.show()

