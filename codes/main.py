import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
#4 samples
slen=int(4)
#Probability of the event
prob = 0.5
#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=slen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
print(data_bern)
if(data_bern[3]==1):
  print("sushma got tail")
else:
  print("sushma got head")  

