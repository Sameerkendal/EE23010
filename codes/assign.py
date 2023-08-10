import math
import numpy as np
A= np.array([1,-1])
B= np.array([-4,6])
C=np.array([-3,-5])
# finding  the direction vector for the lines BC AND CA
m1= C-B
m2= A-C
#finding the unit vectors
u_m1= m1/(np.linalg.norm(m1))
u_m2=m2/np.linalg.norm(m2)
# generating the normal equation of angular bisector using parallelogram theorm
X= u_m1 +u_m2
# nfT= normal vector of final equation whereas cf depicts c final in the equation
nfT= np.array([X[1],(X[0]*(-1))])
cf= nfT@(C.T)
print("The Equation of angular bisector of angle C is ",nfT,"X = ",cf)


import sys                                          
sys.path.insert(0, '/home/sameer/Assignment1/CoordGeo')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *

from triangle.funcs import *
from conics.funcs import circ_gen
#if using termux
import subprocess
import shlex
A=np.array([1, -1])
B=np.array([-4, 6])
C=np.array([-3, -5])

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Generating the circumcircle
#[O,R] = ccircle(A,B,C)
#x_circ= circ_gen(O,R)

#Generating the incircle
[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)
x_CI = line_gen(C ,I)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CI[0,:],x_CI[1,:],label='$CI$')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)

I = I.reshape(-1,1)
tri_coords = np.block([[A,B,C,I]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig('/home/sameer/Assignment1/figs/angularbisector.png')

plt.show()





