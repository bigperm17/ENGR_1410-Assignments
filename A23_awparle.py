# !/usr/bin/env python3

import numpy as np
import tkinter as tk
from time import sleep as pause
from A23_awparle_F import A23_awparle_F

def quit_loop(master,num):
	#print("Selection:",num)
	global selection
	selection = num
	#master.quit()
	master.destroy()

def menu_main(master,quest, *args):
	listvar = []
	for i in range(len(args)):
		listvar.append([args[i],i+1])

	master.title(quest)
	master.attributes('-topmost', True)
	r = 1
	for b in listvar:
		tk.Button(master, text=b[0], bg="light goldenrod",
			command=lambda text=b: quit_loop(master,text[1])).grid(row=r, sticky='W')
		r += 1

	master.mainloop()

def menu(quest, *args):
	master = tk.Tk()
	temp = []
	for i in range(len(args)):
		temp.append(args[i])
	menu_main(master,quest,*args)
	global selection
	pause(1)
	try:
		select = selection
	except NameError:
		#del selection
		return None
	else:
		del selection
		return select

def main():
	##   Header and Test Cases

	# Adam Parler   ENGR 1410-013     March 25, 2014
	# Problem Statement: This program will suggest solutions to medical
	# problems.

	# Test Case # 1
	Name='John Doe';
	W=170;   # [pound-force]
	S=1;     # Menu choice:Cold
	# Expected outcome: Density of Achoo=2500 kg/m^3;Number of tablets=5

	# Test Case # 2
	# Name='John Doe'
	# W=170;   # [pound-force]
	# S=2;     # Menu choice: Flu
	# Expected outcome: Density of Chill=3200 kg/m^3; Number of tablets=3

	# Test Case # 3
	# Name='John Doe'
	# W=170;   # [pound-force]
	# S=3;     # Menu Choice:Migraine
	# Expected outcome: Density of HAche=2750 kg/m^3; Number of tablets=4

	# Test Case # 4
	# Name='John Doe'
	# W=170;   # [pound-force]
	# S=0;     # Menu was closed
	# Expected outcome: You incorrectly selected a symptom

	# Test Case # 5
	# Name='John Doe'
	# W=68;    # [pound-force]
	# S=2;     # Menu Choice: Flu
	# Expected outcome: Weight is too low, Asssumes weight is 75 
					  # Density of Chill=3200 kg/m^3; Number of tablets=2
					  
	# Variables
	# x=looping variable
	# Name=User's Name
	# W=weight [lb_f]
	# S=Ailment  [Menu Selection]
	# M=cell array of Medicine information {Symptoms; Medicine; Volume(mL); mass(g)}
	# Info=Medicine information for symptom
	# N=number of pills
	# D=Density [kg/m^3]

	##   Program

	# Cell array of medicine choices and specifications
	M = [['Cold','Flu','Migraine'],['Achoo', 'Chill', 'HAche'],[3.6, 5, 4], [9, 16, 11]]
	x = 0

	#Input data
	# Name = input('Enter your name:   ')
	# W = input('Enter your weight in pound-force:    ')

	# Determines if weight is correct
	if float(W) < 75.0:
		print('The entered weight is too low to correctly use this program')
		print('Program assumes that weight=75')
	'''
	while x == 0:
		S = menu('Select your symptoms',M[0][0],M[0][1],M[0][2])
		if S == 0 or S == None:
			x = 0
			print('You have incorrectly selected a symptom. Try again.')
		else:
			x = 1
	'''
	# Determines which medicine to use
	temp = []
	for x in M:
			temp.append(x[S-1])

	Med = temp[1]
	S = temp[0]

	print(temp[2:])

	[SG, N] = A23_awparle_F(temp[2:],int(W))

	# Output Statements
	print(f'\n\nThe density of {Med} is {SG:.3f} kg/m^3')
	print(f'{Name} your recommended dosage of {Med} to treat a {S}: {N:.0f} tablets.\n')


if __name__ == "__main__":
	main()











