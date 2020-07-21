#Adam Parler  ENGR 1410-013    January 31, 2014
#Problem Statement: Convert all of the spring data to the same units and
#create a program to allow user inputs.

import numpy as np

def A10_awparle_P2F (M,T,N):

	H=1000 #g-->kg
	g=9.81 #gravitational acceleration

	MAT1 = [M/H, T/N]
	MAT2 = [M*g/H, N/T]

	MAT1 = np.array(MAT1)[:,:,0]
	MAT2 = np.array(MAT2)[:,:,0]

	return MAT1.T, MAT2.T


