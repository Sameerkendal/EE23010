import math
import numpy as np
A= np.array([[1],[-1]])
B= np.array([[-4],[6]])
C=np.array([[-3],[-5]])
# finding  the direction vector for the lines BC AND CA
m1= C-B
m2= A-C
# finding the n(transpose) vector such that nT*m =0
n2T= np.array([-m1[1][0],m1[0][0]])
n3T=np.array([m2[1][0],-m2[0][0]])
# finding the constant value in normal form of eqaution
c2= n2T@B
c3= n3T@C
n2r= np.transpose(n2T)
n3r= np.transpose(n3T)
#norm of n2 and n3
norm2=math.sqrt(n2r@n2T)
norm3=math.sqrt(n3r@n3T)
# angle bisector equation
nfT= (n2T/norm2)-(n3T/norm3)
cfT= (c2/norm2)-(c3/norm3)
print("The Equation of angular bisector of angle C is ",nfT,"X = ",cfT)

import sys
sys.path.insert(0, "/home/sameer/Assignment1/CoordGeo")

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

A=np.array([1, -1])
B=np.array([-4, 6])
C=np.array([-3, -5])

x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)
x_CI = line_gen(C ,I)



plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CI[0,:],x_CI[1,:],label='$CI$')


tri_coords = np.vstack((A,B,C,I)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center') 


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('/home/sameer/Assignment1/figs/angularbisector.png')

