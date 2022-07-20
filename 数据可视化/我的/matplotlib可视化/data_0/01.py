import matplotlib.pyplot as plt
import get_earthqwake_data as ga
import numpy as np


x = np.arange(len(ga.time_list))

fig, ax = plt.subplots()

width = 1
rect = ax.bar(0, ga.mag_list, width, label='震级')

ax.set_xticks(x, ga.time_list)

plt.show()