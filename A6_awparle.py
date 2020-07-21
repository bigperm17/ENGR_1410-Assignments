#!/usr/bin/env python3

#Adam Parler  ENGR 1410-013  January 21, 2014
#Problem Statement:  Store matrices into MATLAB and perform calcuations

import numpy as np


#Input Variables:
A=[[4, 6], [-3, 8]];
B=[[3, 5], [ 5, 5]];
C=[0, 1];
D=[[1], [1]];
E=[[3, 6, 5], [ 7, 1, 5]];
F=[[2, 8], [ 4, 3], [ 1, 5]];
G=np.arange(1,301);
h=[200,-300,-1];
H=h[::-1]
J=[[20,200,20], [ 10,100,10]];
# k=[5:5:50; 50:-5:-50];
# K=k'
#This matrix will not work because there are more rows for one operation
#than the other.

#Calculations
A = np.array(A)
B = np.array(B)
L=A @ B
m=A+B
# n=A+C
#To be added, the matrix demensions must be the same
# p=C-E
#To be subtracted, the maxrix demensions must be the same
F = np.array(F)
E = np.array(E)
q=F @ E
r=B^2
s=A*30
u=F.T+E
J = np.array(J)
v=J.T+30
# w=E^2 +50
#Maxrix E is not a scalar or a square matrix.  The number of columns and
#rows are not equal, so the matrix cannot be multiplied.
