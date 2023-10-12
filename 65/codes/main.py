import numpy as np
import matplotlib.pyplot as plt

# Open the file in read mode
with open("des_dist.dat", "r") as file:
    # Read the lines from the file
    lines = file.readlines()

# Process the lines as needed
X = [float(line.strip()) for line in lines]
X = np.array(X)

num_sim = len(X)

desired = X[(X==0)]
desired1 = X[(X==1)]
desired2 = X[(X==2)]
sim_prob = len(desired)/len(X)
sim_prob1 = len(desired1)/len(X)
sim_prob2 = len(desired2)/len(X)

sim = [sim_prob, sim_prob1, sim_prob2]
act = [0.25,0.5,0.25]
x = [0,1,2]

plt.stem(x, sim, basefmt=" ", markerfmt="bo", linefmt="b-", label='Simulation')
plt.stem(x, act, basefmt=" ", markerfmt="bo", linefmt="g-", label='Actual')
plt.legend()
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Simulated vs Theoretical Analysis')
plt.savefig('/home/sameer/65/figs/fig.png')
plt.grid(True)
plt.show()


