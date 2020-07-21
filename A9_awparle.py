#!/usr/bin/env python3

##  ICA 18-15
 #Adam Parler  ENGR 1410   January 29, 2014
 #Problem Statement:Create a proper plot for the Joule effect data. 

import numpy as np
import matplotlib.pyplot as plt

#Experimental Data
Current=[0.50,1.25,1.50,2.25,3.00,3.20,3.50]; #Current (I) [A]
Power=[1.20,7.50,11.25,25.00,45.00,50.00,65.00];  #Power (P) [W]
 
#plt.figure(color='w')
plt.figure()
plt.plot(Current, Power, '^b',fillstyle='none')
T = 'Joule Effect Graph'
plt.title(T,color='k',fontsize=12)
plt.xlabel('Current (I) [A]')
plt.ylabel('Power (P) [W]')
plt.grid()
plt.axis([0, 4, 0, 70])
plt.xticks(np.arange(0,4.5,0.5))
plt.yticks(np.arange(0,80,10))
plt.draw()

#############################################################################

## ICA 18-20
 # Adam Parler	ENGR 1410	January 29, 2014
 # Problem Statement: Create a proper plot of the theoretical voltage decay
 # of a resistor-capacitor circuit

#Variables
 # C=Capacitance Microfarads (C) [?F]
 # R=Resistance Ohms (R) [?]
 # V_0=Initial Voltage (V) [V]
 # V(t)=Volts after t seconds (V) [V]
 # t=time (t) [s]
 
#Assumptions
C = 500		# Microfarads (C) [?F]
R = 0.5		# Ohms (R) [?]
V_0 = 10	# Volts (V) [V]

# Calculations
t = np.arange(1,601)
V = V_0 * np.exp(-t/(R*C))

# Graph
plt.figure()
plt.plot(t,V,'sb',fillstyle = 'none')
T = 'Voltage Decay'
plt.title(T,color='k',fontsize=12)
plt.xlabel('Time (t) [s]')
plt.ylabel('Volts (V) [V]')
plt.grid()
plt.axis([0, 650, 0, 11])
plt.xticks(np.arange(0,700,50))
plt.yticks(np.arange(0,12,1))
plt.draw()

#############################################################################

## ICA 18-21
 #Adam Parler ENGR 1410 January 29, 2014
 #Problem Statement:
 
 #  Variables:
 #  C=angle (deg) [o]
 #  M=measure of angle (-) [-]

pi = np.pi

#Calculaions
C = np.arange(0,390,30)
M_1 = np.sin(C*pi/180);
M_2 = 3*np.sin(C*pi/180);
M_3 = np.sin(C*pi*3/180);
M_4 = 3*np.sin(2*C*pi/180)-2;

#fig = plt.figure()
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows = 2, ncols=2)
plt.tight_layout()

ax1.plot(C,M_1,'or', markerfacecolor='r')
ax1.set_xlabel('Angle (deg) [o]')
ax1.set_ylabel('Sine of X (sinx) [-]')
ax1.grid()
ax1.axis([0, 360, -1, 1])
ax1.set_xticks(np.arange(0,390,30))
ax1.set_yticks(np.arange(-1,1.25,0.25))
T = 'Graph A'
ax1.set_title(T,color='k',fontsize=12)

ax2.plot(C,M_2,'^g', markerfacecolor='g')
ax2.set_xlabel('Angle (deg) [o]')
ax2.set_ylabel('Sine of X (sinx) [-]')
ax2.grid()
ax2.axis([0, 360, -3, 3])
ax2.set_xticks(np.arange(0,390,30))
ax2.set_yticks(np.arange(-3,4,1))
T = 'Graph B'
ax2.set_title(T,color='k',fontsize=12)

ax3.plot(C,M_3,'sb', markerfacecolor='b')
ax3.set_xlabel('Angle (deg) [o]')
ax3.set_ylabel('Sine of X (sinx) [-]')
ax3.grid()
ax3.axis([0, 360, -1, 1])
ax3.set_xticks(np.arange(0,390,30))
ax3.set_yticks(np.arange(-1,1.25,0.25))
T = 'Graph C'
ax3.set_title(T,color='k',fontsize=12)

ax4.plot(C,M_4,'dk', markerfacecolor='k')
ax4.set_xlabel('Angle (deg) [o]')
ax4.set_ylabel('Sine of X (sinx) [-]')
ax4.grid()
ax4.axis([0, 360, -5, 1])
ax4.set_xticks(np.arange(0,390,30))
ax4.set_yticks(np.arange(-5,1.1,1))
T = 'Graph F'
ax4.set_title(T,color='k',fontsize=12)

plt.show()



