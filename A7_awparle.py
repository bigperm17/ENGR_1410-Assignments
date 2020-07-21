#!/usr/bin/env python3

#Adam Parler    ENGR 1410-013   January 22, 2014
#Problem Statement:Write statements that will accomplish the stated purpose

import numpy as np

#Input Variables
V1= [125, 367, 498, 24, 63, 0.25, 543, 89];
V2= [75, 32, 0.67, 34];
V3= [98, 56, 56, 1, 98, 56, 87, 98];
V4= [5, 10, 100, 0.5, 67, 87];

# Calculations
A=max(V1)
B=np.argmax(V1)
BigVal=[A, B]
C=len(V1);
D=len(V2);
E=len(V3);
F=len(V4);
H=[C, D, E, F];
MinL=min(H)

UV=np.unique(V3)

r100=np.random.randint(-5, 5, size=(1, 10))

V=75*np.ones(12);
L=np.diag(V);
p75=np.rot90(L)

Ma = []
Ma.append(V1)
Ma.append(V3)
temp = [x + 5 for x in V1]
Ma.append(temp)
temp = [x*3 for x in V3]
Ma.append(temp)
print(Ma)

MaRows, MaCols=np.array(Ma).shape
print(MaRows, MaCols)

X=min(min(Ma));
Y=np.argmin(V1)
MaxMa= [X, Y]

V1.sort(reverse=True)
print(V1)


## Adam Parler    ENGR 1410-013   January 22, 2014
#Problem Statement: Evaluates the mathmatical equation
#clear
#clc

#Input Variables
x=0;
u=0;
rho= np.array([1, 2, 5]);

# Calculation
L=(-(x-u)**2)/(2*rho**2);
P=(1/(rho*np.sqrt(2*np.pi)))*np.exp(L)
print(P)
