#!/usr/bin/env python3

import numpy as np
from A10_awparle_P2F import A10_awparle_P2F

#Adam Parler  ENGR 1410-013    January 31, 2014
#Problem Statement: Convert all of the spring data to the same units and
#create a program to allow user inputs.

#Assumptions
#This takes place on earth
#g=-9.8 m/s^2

# Spring 1 Data (Mass [g], Time [min])
Mass1=np.array([40,60,90,110])
Time1=np.array([0.187,0.255,0.293,0.323])

# Spring 2 Data (Mass [lbm], Time [s])
Mass2=np.array([0.24,0.31,0.35,0.46])
Time2=np.array([16.5,18.4,20.3,22.5])

# Spring 3 Data (Mass [kg], Time [s])
Mass3=np.array([0.51,0.66,0.81,1.01])
Time3=np.array([12.3,13.6,14.8,16.3])

# Number of oscillations
N=25

#Conversion Factors
kg=2.205 #2.205lb_mass-->1kg
g=1000  #1kg-->1000g
s=60   #1min-->60s

#Conversions
M1=Mass1            #g-->g
M2=g/kg*Mass2     #lb_mass-->g
M3=Mass3*g          #kg-->g
T1=s*Time1          #min-->s
T2=Time2            #s-->s
T3=Time3            #s-->s

M = [M1,M2,M3]
M = np.array(M).reshape(1,-1)

T = [T1,T2,T3]
T = np.array(T).reshape(1,-1)

M=np.rot90(M)
T=np.rot90(T)

[MAT1,MAT2] = A10_awparle_P2F(M,T,N)

print(MAT1)
print(MAT2)


