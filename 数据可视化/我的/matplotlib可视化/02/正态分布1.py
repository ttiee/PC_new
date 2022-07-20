import matplotlib.pyplot as plt
import numpy as np

mu = 75
sigma = 10
x1 = np.random.normal(mu, sigma, 100000)


ax = plt.gca()
ax.hist(x1, bins=400, color='red')

plt.xlim(0, 100)

ax.set_xlabel('math-achievement')
ax.set_ylabel('math-people')

ax.set_title(f'Histogram: μ={mu},σ={sigma}')

x2 = np.random.normal(mu, sigma, 10000)
ax.hist(x2, bins=400, color='blue')

plt.show()


