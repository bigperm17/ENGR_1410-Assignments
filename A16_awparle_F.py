import numpy as np

#Adam Parler  ENGR 1410-013    February 27,2014
#This is the function to go along with program A16

#Variables
# SG=Specific Gravity [-]
# W=Weight [lb_f]
# N=Number of Pills
# M=Medicine information
# g=gravitational acceleration on earth

def A16_awparle_F(M,W):
	g = 9.8

	SG = M[3]/M[2] #mass(g)/volume(mL)
	# Converts patient weight in pound-force to kilograms
	W = W * 1/0.225/g # converts lb_f --> kg by lb_f*Newtons/lb_f/gravity

	#Determines the dosage size
	N = W*1.25/(2.5*SG) #mass(kg)*1.25(ml/kg)/(2.5*SG)*1 (Tablet)/Volume(mL)

	# Rounds the dosage to the next highest tablet
	N = np.ceil(N)

	return SG,N