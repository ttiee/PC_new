import matplotlib.pyplot as plt
import numpy as np

mu = 75
sigma = 10
x = np.random.normal(mu, sigma, 100000)

ax = plt.gca()
ax.hist(x, bins=400, color='red')

plt.xlim(0, 100)

ax.set_xlabel('math-achievement')
ax.set_ylabel('math-people')

ax.set_title(f'Histogram: μ={mu},σ={sigma}')

# plt.text(30, 20, "shenqi", size=30, rotation=20, alpha=0.4, color="red")
plt.show()
