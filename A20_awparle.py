#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

#Adam Parler   ENGR 1410-013   March 6, 2014
#Problem Statement: Determine the efficiency of the engines.

def load(name):
	if not name.lower().endswith(('.npy', '.npz')):
		name = name+'.npz'

	try:
		temp = np.load(name)
	except FileNotFoundError:
		print('File location does not exist, please try again.')
		tmp = os.getcwd()
		print('Filepath: '+tmp+'/'+name)
		raise FileNotFoundError
		# sys.exit()
	return temp

# j=repeat counter
# r=number of rows
# c=number of columns
# TE=Total energy row vector
# KE=Total Kinetic energy row vector
# i=counter

#Loads code and creates a figure
temp = load('Spacecraft.npz')
D = temp['D']

r,c = D.shape
j = 1
plt.figure()
plt.axis([0, 12, 0, 10])
plt.grid()
plt.title('Energy Analysis of Spacecraft Energies')
plt.xlabel('Energy Input (E$_I$) [MJ]')
plt.ylabel('Kinetic Energy (E$_o$) [MJ]')
plt.xticks(range(0,13,2))
plt.yticks(range(0,11,2))

# Loop to test input and output energies to calculate efficiency
for i in range(1,r,2):
	TE = D[i-1,:]
	KE = D[i,:]

	E = np.polyfit(TE,KE,1)
	m = E[0]
	b = E[1]
	R = max(TE)
	S = max(KE)

	# Tests to see if efficiency is 80% or above
	if m >= 0.8:
		Texp = np.arange(1,R+1)
		Kexp = m*Texp+b
		plt.plot(Texp,Kexp,'-r',TE,KE,'dr')
		TEX = f'E{j:.0f}$_O$={m:.3f}E{j:.0f}$_I$+{b:.2f}'
		plt.text(R+0.2,S-0.6,TEX,backgroundcolor='white')
	# Test to see if efficiency is 50% or above
	elif m >= 0.5:
		Texp = np.arange(1,R+1)
		Kexp = m*Texp+b
		plt.plot(Texp,Kexp,'-.b',TE,KE,'ob')
		TEX = f'E{j:.0f}$_O$={m:.3f}E{j:.0f}$_I$+{b:.2f}'
		plt.text(R+0.2,S-0.6,TEX,backgroundcolor='white')
	# All other efficiencies
	else:
		plt.plot(TE,KE,'xk')

	plt.draw()

	j += 1
plt.show()










