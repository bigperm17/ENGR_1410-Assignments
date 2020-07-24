# !/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Adam Parler    ENGR 1410-013    March 27, 2014
#Problem Statement: This program classifies plasma and displays the result
#on a graph.

#Test Case 1
D = -8;
T = 2.5;
# Expected outcome: Phase=Molecular Fluid

#Test Case 2
# D=-6;
# T=5;
# Expected outcome: Phase=Plasma

#Test Case 3
# D=1.5;
# T=3;
# Expected outcome: Phase=Metallic Fluid

#Variables
# D=Density (g/cc)
# T=temperature (K)
# CLASS=phase classification
# DATA=all division data
# X=x values for phase division
# Y=y values for phase division
# temp=temporary polyfit values
# Div=values of polyfitted lines

DATA = np.array([[-10, 0, 3.3, 3.9], [0, 2, 3.9, 5.6], [0, 0, 2, 3.9]])

[r,c] = DATA.shape;

Div = np.empty([r-1,2])
X = np.empty(2)
Y = np.empty(2)
for i in range(r-1):
    X[0] = DATA[i,0]
    X[1] = DATA[i,1]
    Y[0] = DATA[i,2]
    Y[1] = DATA[i,3]
    temp = np.polyfit(X,Y,1)
    Div[i,:] = temp


# D=input('Enter log of density (g/cc):  ');
# T=input('Enter log of temperature (K):   ');

if D <= DATA[r-1,0]:
    if T <= Div[0,0]*D+Div[0,1]:
        CLASS='Molecular Fluid'
    else:
        CLASS='Plasma';

else:
    if T <= Div[1,0]*D+Div[1,1]:
        CLASS='Metallic Fluid'
    else:
        CLASS='Plasma'



print(f'For the log density {D:.1f} and log temperature {T:.1f}, the phase is {CLASS}.')

plt.figure()
plt.axis([-10, 2, 2, 6])
plt.plot(D,T,'.r', markersize=10)
plt.text(-6,2.8, 'Molecular Fluid')
plt.text(-6, 4.5, 'Plasma')
plt.text(.3,2.3, 'Metallic Fluid')
plt.text(D+0.125, T-0.05, '<--Your point')

for i in range(r):
    X[0] = DATA[i,0];
    X[1] = DATA[i,1];
    Y[0] = DATA[i,2];
    Y[1] = DATA[i,3];
    plt.plot(X,Y,'-k')
    
plt.xlabel('Log Density ($\\rho$) [g/cc]')
plt.ylabel('Log Temperature (T) [K]')
plt.xticks(range(-10,3,2))
plt.yticks(range(2,7))

plt.show()

    
