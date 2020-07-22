import numpy as np

#Adam Parler  ENGR 1410-013    March 25,2014
#This is the function to go along with program A23

#Assumptions
# calculations done on earth
# Density of water is 1 g/mL
# SG*1000 kg/m^3= Density [kg/m^3]
# Specific gravity of water is 1.

#Variables
# SG=Specific Gravity [-]
# W=Weight [lb_f]
# N=Number of Pills
# D=Medicine Density
# g=gravitational acceleration on earth
# DW=Density of water (kg/m^3)
# SG=specific gravity [-]
# SGW=specific gravity of water


def A23_awparle_F (M,W):
	g = 9.8
	DW = 1000
	SGW = 1

	SG = M[1]/M[0]/SGW 	#(g/mL)/(g/mL) 

	D = SG*DW 			#mass(g)/volume(mL)*Density of water in 

	#Converts patient weight in pound force to kilograms
	W = W*1/0.225/g		#converts lb_f-->kg by lb_f*Newtons/lb_f/gravity

	#Determines the dosage size
	N = W*1.25/(2.5*SG)/M[0]; #mass(kg)*1.25(ml/kg)/(2.5*SG)*1 (Tablet)/Volume(mL)

	#Rounds the dosage to the next highest tablet.
	N=np.ceil(N);

	return D, N

	