import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 2  # Number of trials
p = 0.5  # Probability of success

# Parameters for the normal distribution (approximation to binomial)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Generate values for x (number of successes in binomial)
x = np.arange(0, 3)

# Compute the PMF of the binomial distribution
binomial_pmf = binom.pmf(x, n, p)



# Plot the binomial PMF
plt.stem(x, binomial_pmf, basefmt=" ", markerfmt="bo", linefmt="b-", label='Binomial PMF')



# Add labels and legend
plt.xlabel('Number of Successes')
plt.ylabel('Probability / Probability Density')
plt.legend()

# Show the plot
plt.title('Binomial PMF')
plt.grid(True)
plt.savefig("/home/sameer/65/figs/fig.png")



