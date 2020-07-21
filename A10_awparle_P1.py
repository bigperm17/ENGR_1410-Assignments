#!/usr/bin/env python3

## Problem 13
#Adam Parler   ENGR 1410-013    January 31, 2014
#Problem Statement: Calculate the weight of a metal rod

from A10_awparle_P1F import A10_awparle_P1F

V=input('User Input: \n Volume =    ')
V = float(V)
print('cubic meters');
SG=input('Specific Gravity =   ')
SG = float(SG)

Weight = A10_awparle_P1F(V,SG)
print('With these values, a rod on Callisto would weigh',end='')
print(f' {Weight:.4f} pounds-force. \n')

## Sample Output

##
# 
# <<A10_awparle1.PNG>>
# 

