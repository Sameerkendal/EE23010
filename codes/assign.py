import math
import numpy as np

#Given points
A= np.array([[1],[-1]])
B= np.array([[-4],[6]])
C=np.array([[-3],[-5]])
# finding  the direction vector for the lines BC AND CA
m1= C-B
m2= A-C
# finding the n(transpose) vector such that nT*m =0
n2T= np.array([-m1[1][0],m1[0][0]])
n3T=np.array([int(m2[1][0]/4),int(-m2[0][0]/4)])
# finding the constant value in normal form of eqaution
c2= np.dot(n2T,B)
c3= np.dot(n3T,C)
n2= np.transpose(n2T)
n3 = np.transpose(n3T)
#norm of n2 and n3
norm2=math.sqrt(np.dot(n2,n2T))
norm3=math.sqrt(np.dot(n3,n3T))
# angle bisector equation
nfT= (n2T/norm2)-(n3T/norm3)
cfT= (c2/norm2)-(c3/norm3)
print("The Equation of angular bisector of angle C is ",nfT,"X = ",cfT)

