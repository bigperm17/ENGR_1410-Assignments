#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

eps = np.finfo(np.float32).eps

## Linear Polyfit

# Adam Parler  ENGR 1410-013   February 6, 2014
# Problem Statement: Create different types of graphs and add trendlines 
# to them.

#Variables
#T=Temperature Change (T) [K]
#Q=Heat applied (Q) [J]
#M=Mass (M) [g]
#C_P=Specific Heat

#Data
T=np.array([1.5, 2.0, 3.25, 5, 6.25, 7])
Q=np.array([12, 17, 25, 40, 50, 58])

#Graph
plt.figure()
plt.plot(Q,T,'ok',fillstyle='none')
plt.xlabel('Heat Applied (Q) [J]')
plt.ylabel('Temp Change ${\Delta}T$ [K]')
plt.title('Heat Applied vs Temp')
plt.grid()
plt.axis([10,60,1,8])
plt.draw()

#Polyfit Parameters
C = np.polyfit(Q,T,1)
m = C[0]
b = C[1]

# Create theoretical data series
Qpf = range(12,61)
Tpf = m*Qpf+b

plt.plot(Qpf,Tpf,':b')

# Place Trendline Equation on Graph
TE = '${\Delta}T$ = ' + f'{m:.3f} Q + {b:.3f}'
plt.text(40,4,TE, backgroundcolor = 'white')

plt.show()

###################################################

## Power Polyfit

#Variables
#r=Radius (r) [cm]
#h=Height (H) [cm]

#Data
r = np.array([0.01, 0.05, 0.10, 0.20, 0.40, 0.50])
h = np.array([14.0, 3.0, 1.5, 0.8, 0.4, 0.2])

#Create Plot
plt.figure()
plt.loglog(r,h,'^r',fillstyle='none')
plt.axis([0.01, 1, 0.1, 100])
plt.xlabel('Radius (r) [cm]')
plt.ylabel('Height (H) [cm]')
plt.title('Capillary Action Graph')
plt.grid()
plt.draw()

# Polyfit Parameters
C = np.polyfit(np.log10(r),np.log10(h),1)
m = C[0]
b = 10**C[1]

#Crete Trendline
Rpf = np.arange(0.01,0.5+eps, 0.01)
Hpf = b*Rpf**m

plt.plot(Rpf,Hpf,'--r')

#Put Trendline on graph
TE = f'H={b:.2f}*R^{m:.3f}'
plt.text(0.02,1,TE,backgroundcolor = 'white')

plt.show()

####################################################

## Exponential Polyfit

#Variables
#y=Years from 1967
#Q=Minumum gear size [mm]

#Data
y = np.array([0, 5, 7, 16, 25, 31, 37])
Q = np.array([0.8, 0.4, 0.2, 0.09, 0.007, 0.0002, 0.000008])

#Create Plot
plt.figure()
plt.semilogy(y,Q,'db',fillstyle='none')
plt.axis([0,40,0.000001,1])
plt.xlabel('Years from 1967')
plt.ylabel('Minimum Gear Size')
plt.title('Size of Working Gear')
plt.grid()
plt.draw()

#Polyfit Parameters
C = np.polyfit(y,np.log(Q),1)
m = C[0]
b = np.exp(C[1])

#Crete Trendline
ypf = np.arange(0.01,40+eps, 1)
Qpf = b*np.exp(ypf*m)
plt.plot(ypf,Qpf,'-.b',fillstyle='none')

#Put Trendline Equation on Graph
TE = f'Min={b:.4f}*e^(y*{m:.4f})'
plt.text(10,0.0001,TE, backgroundcolor = 'white')

plt.show()





