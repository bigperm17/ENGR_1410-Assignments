#!/usr/bin/env python3

##Problem 1
#Adam Parler   ENGR 1410-013   January 24, 2014
#Problem Statement: Convert Kelvin to other common unit systems

#Variables
    #k=Kelvin
    #c=Degrees Celcius
    #f=Degrees Fahrenheit
    #r=Degrees Rankine

#Assumptions
    #273 k=0 c
    #0 c=32 f
    #400 r=60 f
    #(f-32)/180=c/100
    
#Calculations
k=float(input('Enter Temperature [K]:   ')) #[K]
c=k-273  #[K-->C]
f=(1.8*c)+32  #[C-->F]
r=f+460  #[F-->R]
print(f'The temperatrue of {k:.2f} K = {c:.2f} deg C = {f:.2f} deg F',end='')
print(f' = {r:.2f} deg R\n\n\n')

## Problem 2
    #Adam Parler   ENGR 1410-013   January 24, 2014
    #Problem Statement: Converts between calories per gram degree Celsius and 
    #British Thermal Units per pound-mass degree Farenheit  
 
#Variables
    #cal/(g*degC)=calories per gram degree Celsius
    #BTU/lb_m*deg F)=British Thermal Units per pound-mass degree Farenheit
      
#Assumptions
    #239 calories?0.948 British Thermal Unit
    #1000 grams=2.205 pound-mass
    #change in 1 deg Celsius=change in 1.8 deg Farenheit
      
#Defined Units
cal=239
BTU=0.948
g=1000
lb_m=2.205
deg_C=1
deg_F=1.8
     
#Variable Calculations
i=float(input('Enter specific heat [cal/(g deg C)]:   '))  #[cal/g deg C]
a=i*(BTU/cal)*(g/lb_m)*(deg_C/deg_F) 

#[cal/(g*degC)--> BTU/(lb_m*deg F)]
print(f'The specific heat is {i:.1f} cal/(g deg C) =',end='')
print(f' {a:.4f} BTU/(lb_m deg F)\n\n\n')
     
## Sample Output
# 
# <<A8_awparle1.PNG>>
# 
