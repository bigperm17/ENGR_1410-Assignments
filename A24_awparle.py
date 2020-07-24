# !/usr/bin/env python3

import numpy as np

## A24_Question 1

# Adam Parler    ENGR 1410-013    March 26, 2014
#Problem Statement: Create a matrix of minimum values based on a users
#input.

#Test Case 1
y = np.array([[-2, 3, 5, 4],[7, 2, -10, 6],[18, 4, -2, 6], [3, 7, 5, -3]])
# Expected outcome: Min values Row 1: -2 Row 2: -10 Row 3: -2 Row 4: 3
                   #Max values Row 1: 5 Row 2: 6 Row 3: 18 Row 4: 7

# Test Case 2
# y=[1; 2; 3; 4]
#Expected outcome: This matrix does not have more than two columns.

# Variables
# y=user inputed matrix
# r=number of rows in y
# c=number of columns in y
# p=counter
# MIN=matrix of numbers in odd numbered columns
# MAX=matrix of numbers in even numbered columns
# M=matrix of minimum and maximum values in each row
# a=number of rows in M
# b=number of columns in M

#Prompts user to input matrix
#y=input('Input a matrix with at least two colums:   ');
[r,c]=y.shape

#checks to make sure it has 2 columns
if c < 2:
    print('This matrix does not have more than two columns')
    sys.exit()

M = np.empty([r,2])
#loops through each row
for i in range(r):
    MIN = []
    MAX = []

    #loops through the odd columns
    for j in range(0,c,2):
        MIN.append(y[i,j])


    #loops through the even columns
    for j in range(1,c,2):
        MAX.append(y[i,j])

    #finds the minimun and maximum values
    M[i,0] = min(MIN)
    M[i,1] = max(MAX)


[a,b]=M.shape
#displays the output information
print('The smallest value found when comparing the odd-numbered columns:')
for k in range(a):
    print(f'Row {k+1:d} = {M[k,0]:.0f}')

print('The largest value found when comparing the even-numbered columns:')
for h in range(a):
    print(f'Row {h+1:d} = {M[h,1]:.0f}')


#####################################################################################

## A24_Question 2
#Problem Statement: Allows a user to either select a previously entered
#material or add a new one.

#Test Case 1
c = 1
#Expected outcome: The specific heat of Gold is 0.031 cal/(g deg c)=0.031 BTU/(lb_m deg F)

#Test Case 2
# c=6
# p=Uranium
# Q=2.34
#Expected outcome: The specific heat of Uranium is 2.340 cal/(g deg c)=2.332 BTU/(lb_m deg F)

#Assumptions
# 1 joule=9.48x10^-4 BTU
# 1 joule=.239 cal
# 1 kg=2.205 lb_m
# 1 kg=1000 grams
# change of 1 degree C=change of 1.8 deg F
#Converts BTU's to calories
E = 1/.239*(9.48*10**-4)/1; #cal*J/cal*BTU/J [BTU-->J-->cal]

#Converts grams to pound-mass
M = 1/1000*2.205/1;   #g*kg/g*lb_m/kg [g-->kg-->lb_m]

#Convets change in deg C to change in deg F
T = 1.8/1; #deg C*(change in deg F)/(change in deg C)  [(deg C)*(deg F)/(deg C)

#Cell array of pre-determined data
MAT = [['Aluminum', 0.22], ['Calcium', 0.22],['Gold', 0.031], ['Silicon', 0.17], ['Zinc', 0.093]]
#c=menu('Choose a metal',MAT{:,1},'Enter a new metal');

#Checks to see if the user selected new metal
if c >= len(MAT):
    pass
    #input new metal information
    #p=input('Enter material name:  ','s');
    #q=input('Enter specific heat: (cal/(g deg c)   ');
else:
    #Pulles previously stored values
    p = MAT[c][0]
    q = MAT[c][1]


#converts cal/(g deg C) to BTU/(lb_m deg F)
g=q*E/(M*T);

#prints the results on the screen
print(f'The specific heat of {p} is {q:.3f} cal/(g deg C) = {g:.3f} BTU/(lb_m deg F).')

