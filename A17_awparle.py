#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Adam Parler    ENGR 1410-013       February 28, 2014
# Problem Statement: Calculates the phase the compound will be according to
# the percent A and B and the temperature.

# Variables
# MP=mass percent of beta
# T=Temerature in Celcius
# A_p1=X values for pure alpha
# A_p2=increasing y values for pure alpha 
# A_n2=decreasing y values for pure alpha
# ELineX=Eutectic line x values
# ELineY=Eutectic line y values
# EPointAX=x values for higher percentage of alpha 
# EPointAY=y values for higher percentage of alpha
# EpointBX=x values for higher percentage of beta
# EpointBY=y values for higher percentage of beta
# B_n1=x values for pure beta
# B_n2=decreasing y values for pure beta
# B_p2=increasing y values for pure beta
# AN=Slope of negative alpha
# AP=Slope of positive alpha
# ABP=slope of positive alpha and beta combination
# ABN=slope of negitive alpha and beta combination
# BP=slope of positive beta
# BN=slope of negative beta
# A=percent mass of Alpha

# Input data
# MP=input('Enter mass percent of B for the compound (# ):  ');
# T=input('Enter temperature of compound in deg C:  ');

# I cannot use the first two outcomes because they will produce an error.
# Therefore, I used my third condition, which will cause a warning, but
# still run.

## Test Case #1
# MP=120;
# T=500;
## Expected outcome: Data is not physically possible.
 
## Test Case #2
# MP=87;
# T=-300;
## Expected outcome: Data is not physically possible.
 
# Test Case #3
MP=43;
T=760;
# Expected outcome: Tempereture entered is greater than the maximum value.
# Temperature was set to 710. Phase = Liquid.
 
## Test Case #4
# MP=67;
# T=874;
## Expected outcome: Tempereture entered is greater than the maximum value.
## Temperature was set to 810. Phase = Liquid.
 
## Test Case #5
# MP=37;
# T=272;
## Expected outcome: Phase= Alpha + Beta
 
## Test Case #6
# MP=12;
# T=100;
## Expected outcome: Phase= Alpha + Beta.
 
## Test Case #7
# MP=2;
# T=500;
## Expected outcome: Phase = Alpha.
 
## Test Case #8
# MP=12;
# T=550;
## Expected outcome: Phase = Alpha + Liquid.
 
## Test Case #9
# MP=37;
# T=350;
## Expected outcome: Phase = Alpha + Liquid.
 
## Test Case #10
# MP=80;
# T=375;
## Expected outcome: Phase = Beta + Liquid.
 
## Test Case #11
# MP=87;
# T=50;
## Expected outcome: Phase = Alpha + Beta.
 
## Test Case #12
# MP=90;
# T=46;
## Expected outcome: Phase = Beta.
 
## Test Case #13
# MP=88;
# T=350;
## Expected outcome: Phase= Beta + Liquid.
 
## Test Case #14
# MP=50;
# T=300;
## Expected outcome: Material is at the eutectic point.
 
## Test Case #15
# MP=47;
# T=300;
## Expected outcome: Material is on the eutectic line.

## Test Case #16
# MP=50;
# T=450;
## Expected outcome: Phase= Liquid.


#Melting Point of Alpha
A_p1=[0, 15];
A_p2=[0, 300];
A_n2=[700, 300];

#Eutectic Line
ELineX=[15, 85];
ELineY=[300, 300];

#Eutectic Divider
EPointAX=[0, 50];
EPointAY=[700, 300];
EPointBX=[50, 100];
EPointBY=[300, 800];

#Melting Point of Beta
B_n1=[85, 100];
B_n2=[300, 0];
B_p2=[300, 800];

#Error messages
if MP> 100 or MP<0:
	raise ValueError
elif T < -273:
	raise ValueError

if MP <= 50 and T > 700:
	print('Temperature entered is greater than the maximum value.')
	print('Temperature was set to 710')
	T = 710
elif MP >= 50 and T > 800:
	print('Temperature entered is greater than the maximum value.')
	print('Temperature was set to 810')
	T = 810

#Graph
plt.figure()
plt.plot(A_p1, A_p2, '-b', A_p1, A_n2, '-b', EPointAX, EPointAY, '-b', EPointBX, EPointBY, '-b',fillstyle='none')
plt.plot(ELineX, ELineY, '-k', B_n1, B_n2, '-b', B_n1, B_p2, '-b',MP, T, 'sr', markersize=4,fillstyle='none')
plt.draw()
plt.axis([0, 100, 0, 850])
plt.xlabel('Composition of Beta (B) [%]')
plt.ylabel('Temperature (T) [deg C]')

plt.text(6.5, 300,r'$\alpha$')
plt.text(45, 150,r'$\alpha$+$\beta}$')
plt.text(45, 650,'Liquid')
plt.text(16, 400,r'$\alpha$+Liquid')
plt.text(65, 400,r'$\beta$+Liquid')
plt.text(90, 300,r'$\beta$')
plt.text(2, 702, u'700\N{DEGREE SIGN}C')
plt.text(16, 270,'15%')
plt.text(49, 270,'50%, 300\N{DEGREE SIGN}C')
plt.text(79, 270,'85%')
plt.text(95, 802,'800\N{DEGREE SIGN}C')
plt.show()

# Phase Calculations
AN = np.polyfit(A_p1,A_n2,1)
AP = np.polyfit(A_p1,A_p2,1)
ABN = np.polyfit(EPointAX,EPointAY,1)
ABP = np.polyfit(EPointBX,EPointBY,1)
BP = np.polyfit(B_n1, B_p2,1)
BN = np.polyfit(B_n1, B_n2,1)

# Determines what phase compound is in 
if T < 300 and MP > 15 and MP < 85:
	Phase = r'$\alpha+\beta$'
elif MP<15 and T<AP[0]*MP+AP[1]:
    Phase=r'$\alpha+\beta$';
elif MP<15 and T<AN[0]*MP+AN[1]:
    Phase=r'$\alpha$';
elif MP<15 and T>ABN[0]*MP+ABN[1]:
    Phase=r'$\alpha$+Liquid';
elif MP>15 and MP<50 and T<ABN[0]*MP+ABN[1]:
    Phase=r'$\alpha$+Liquid';
elif MP>50 and MP<85 and T<ABP[0]*MP+ABP[1]:
    Phase=r'$\beta$+Liquid';
elif MP>85 and T<BN[0]*MP+BN[1]:
    Phase=r'$\alpha+\beta$';
elif MP>85 and T<BP[0]*MP+BP[1]:
    Phase=r'$\beta$';
elif MP>85 and T<ABP[0]*MP+ABP[1]:
    Phase=r'$\beta$+Liquid';
elif MP==50 and T==300:
    Phase='Material is at the eutectic point'
elif T==300 and MP<85 and MP>15:
    Phase='Material is on the eutectic line'
else:
    Phase='Liquid';

# Output Statement
A = 100-MP
print(f'\nFor the composition of {A:.1f}% A, {MP:.1f}% B and a temperature of')
print(f'{T:.0f} degrees Celcius, the phase is {Phase}.\n')














