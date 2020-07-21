#!/usr/bin/env python3

## Problem Review 15-1
#Adam Parler    ENGR 1410-013   January 17, 2014
# Problem Statement: Determine the weight of a rod in pound-force.

#Variables:
    #V-Volume of rod [m^3]
    #SG-Specific Gravity of rod [-]
    #g-Gravitaty [9.8 m/s^2]
    #D_r-density of rod [kg/m^3]
    #D_w-density of water [kg/m^3]
    #W-Weight of rod [lb_force]
    #N-Newton [kg*m/s^2]
    #lb_f-pound-force
    
 #Assumptions:
    # 1 N=1 [kg*m/s^2]
    #SG=4.7 [-]
    #g=1.25 [m/s^2]
    #W=D_r*V*g
    #1 N=.225 [lb_force]
    #D_w=1000 [kg/m^3]

#Set inputs and constants
V=.3;
SG=4.7;
D_w=1000;
g=1.25;
 
 #Calculate weight
W=SG*D_w*V*g;
 
 #Convert to pound-force
lb_f=W*.225


## Problem Review 15-3
 #Adam Parler     ENGR 1410-013  January 17, 2014
 #Problem Statement: Determine the density of tribromoethylene in kilograms
 #per cubic meter
 
 #Variables:
      #H-height of cylinder [ft]
      #P_s-surface Pressure [atm]
      #P_t-total Pressure [atm]
      #g=gravity [9.8 m/s^2]
      #rho-Density [kg/m^3]
    
 #Assumptions:
    #P_t=P_s+rho*g*h
    #g=9.8 [m/s^2]
    #1 atm=101325 Pa
    #1 Pa= 1 kg/m*s^2
    #1 m=3.28 ft

 #set input variables
H=25;
P_t=5;
P_s=3;
g=9.8;
 
 #convert to SI units
H=H/3.28;   #[ft]-->[m]
 
 #calculate density of tribromoethylene
rho=((P_t*101325)-(P_s*101325))/(g*H)

