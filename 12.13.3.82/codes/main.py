import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
turns = int(10000)
possible=[1,2,3,4,5,6]
prob = [1/6,1/6,1/6,1/6,1/6,1/6]
random_A = np.random.choice(possible,turns,p=prob)
random_B = np.random.choice(possible,turns,p=prob)
sum = random_A + random_B
sumlt6=[]
for i in range(turns):
	if(sum[i] < 6):
		sumlt6.append(sum[i])
sumeq3=[]
for i in range(len(sumlt6)):
	if(sumlt6[i] == 3):
		sumeq3.append(sumlt6[i])
# probability of getting 3 as sum when given sum is lessss than 6
probability = len(sumeq3)/len(sumlt6)
print(probability)
