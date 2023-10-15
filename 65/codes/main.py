import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Open the file in read mode
with open("des_dist.dat", "r") as file:
    # Read the lines from the file
    lines = file.readlines()

# Process the lines as needed
X = [float(line.strip()) for line in lines]
X = np.array(X)
with open("des_dist1.dat", "r") as file:
    # Read the lines from the file
    lines1 = file.readlines()

# Process the lines as needed
Y = [float(line.strip()) for line in lines1]
Y = np.array(Y)
sum=X+Y
num_sim = len(X)

desired = sum[(sum==0)]
desired1 = sum[(sum==1)]
desired2 = sum[(sum==2)]
sim_prob = len(desired)/len(X)
sim_prob1 = len(desired1)/len(X)
sim_prob2 = len(desired2)/len(X)
sim = [sim_prob, sim_prob1, sim_prob2]
p0 = binom.pmf(0, 2, 0.5)
p1 = binom.pmf(1, 2, 0.5)
p2 = binom.pmf(2, 2, 0.5)
act = [p0,p1,p2]
x = [0,1,2]

plt.stem(x, sim, basefmt=" ", markerfmt="bo", linefmt="b-", label='Simulation')
plt.stem(x, act, basefmt=" ", markerfmt="go", linefmt="g-", label='Actual')
plt.legend()
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Simulated vs Theoretical Analysis')
plt.savefig('/home/sameer/65/figs/fig.png')
plt.grid(True)
plt.show()


