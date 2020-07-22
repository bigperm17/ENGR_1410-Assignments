#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from A16_awparle import menu

# Adam Parler   ENGR 1410-013   March 7, 2014
# Problem Statement: This program proves that a proposed matrix is a magic
# square.

# Variables
# MS=proposed magic square
# r=number of rows
# c=number of columns
# D=value of a specific number in matrix MS
# N=value of first row to be compared
# P=value of second row to be compared
# Q=value of first column to be compared
# R=value of second column to be compared
# W=program ending variable
# K=menu selection
# x=variable to repeat program
# V=Answer to is it a Semi-Magic Square?
# Y=Answer to is it a Normal Magic Square?
# Z=Answer to is it a Perfect Magic Square?
# S=Rotated MS matrix

# Test Case 1: Random magic square
# MS=[80 15 10 65; 25 50 55 40; 45 30 35 60; 20 75 70 5];
# Expected Outcome:
#      The Magic Constant for your magic square is 34.
#      The classification of your magic square:
#          Semi-Magic      Normal      Perfect
#          yes             yes         no

# Test Case 2: Albrecht Durer magic square
#  MS=[16 3 2 13; 5 10 11 8; 9 6 7 12; 4 15 14 1];
# Expected Outcome:
#      The Magic Constant for your magic square is 34.
#      The classification of your magic square:
#          Semi-Magic      Normal      Perfect
#          yes             yes         yes

# Test Case 3: Harry's magic square
#  MS=[7 12 5 6; 11 1 17 2; 9 4 14 3; 8 6 12 4];
# Expected Outcome:
#      The Magic Constant for your magic square is 34.
#      The classification of your magic square:
#          Semi-Magic      Normal      Perfect
#          yes             no          no

# Test Case 4: Exciting magic square
#  MS=[80 15 10 65; 25 -50 55 40; 45 30 35 60; 20 75 70 5];
# Expected Outcome:
#      The values you entered are not more than zero, try again.
#      Enter proposed 4x4 Magic square

# Test Case 5: Kelsey's magic square
#  MS=[1 2 3 4 5; 6 7 8 9 10; 11 12 13 14 15; 16 17 18 19 20; 21 22 23 24
# 25];
# Expected Outcome:
#      The matrix you entered is not a 4x4 matrix, please enter a 4x4
#      matrix. 
#      Enter proposed 4x4 Magic square:   

# Test Case 6: Ralph's magic square
# MS=[1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16];
# Expected Outcome:
#      This is not a magic square. Would you like to try another square?


x=1
t=1
while x==1:
	W=1
	while W != 0:
		print('Enter proposed 4x4 Magic Square:   ')
		MS = list(map(int, input().split()))
		MS = np.array(MS).reshape(4, 4) 
		r,c = MS.shape
		for i in range(r):
			for j in range(c):
				D = MS[i,j]
				if D < 0:
					print('Values entered are not more than zero, try again.')
					MS = input('Enter proposed 4x4 Magic Square:   ')

		while t == 1:
			if r != 4 or c != 4:
				print('The matrix you entered is not a 4x4. Please enter a 4x4 matrix.')
				MS = input('Enter proposed 4x4 Magic Square:   ')
				r,c = MS.shape
				t = 1
			else:
				t = 0

			


		for i in range(3):
			N = MS[i,:]
			P = MS[i+1,:]
			if sum(N) == sum(P):
				for j in range(3):
					Q = MS[:,j]
					R = MS[:,j+1]
					if sum(Q) == sum(R):
						Q = Q.T
						if sum(Q) == sum(N):
							V = 'yes'
							U = MS.copy()
							for k in range(4):
								if sum(np.diag(U)) == sum(Q):
									Y = 'yes'
									U = U.T
									if np.amax(MS) == 16:
										Z = 'yes'
									else:
										Z = 'no'

								else:
									Y = 'no'
						

						else:
							V = 'no'



			else:
				V = 'no'
				W = 0



		
		if W == 0:
			K = menu('This is a Magic Square. Would you like to try another square?','Yes','No')
			if K == 1:
				W = 1
			else:
				W = 0

		else:
			print(f'The magic constant for your magic square is {np.amax(R):.0f}.')
			print('The classification for your magic square:\n\t',end='')
			print(f'Semi-Magic\t\t Normal\t\t Perfect\n\t {V}\t\t\t   {Y}\t\t   {Z}')
			K = menu('This is a Magic Square. Would you like to try another square?','Yes','No')
			if K == 1:
				W = 1
			else:
				W = 0


				
	if K == 1:
		x = 1
	else:
		x = 0
































