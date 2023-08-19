import numpy as np
import random
samplespace= np.array([0,1])
outcome=random.choice([0,1])
count_head=0
count_tail=0
print(outcome)
if(outcome==0):
	count_head=count_head+1
	pr_head= float(count_head/len(samplespace))
	pr_tail= 1-pr_head
else:
	count_tail=count_tail+1
	pr_tail= float(count_tail/len(samplespace))
	pr_head= 1-pr_tail
print("the probability of getting head is ",pr_head)
print("the probability of getting tail is ",pr_tail)
print("Hence the probabilty is equally likely to be head or tail.")
