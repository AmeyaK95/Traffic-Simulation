# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 11:19:30 2016

@author: Ameya
"""

import numpy as np
from scipy.integrate import odeint #Import the ODE Solving function
import matplotlib.pyplot as plt

guess=350  # define guess value outside function definition
list_of_n = [10.0 ,11.0,12.0,15.0, 20.0 ,25.0,30.0,40.0, 50.0,63.0 ,75.0,88.0, 100.0]
list_of_error = []

for n in list_of_n:
    
    L=10.0
    dx=L/(n)
    def ameyak(T,x):
        L=10  
        P=10
        U=100
        Ma=1
        Mb=2
        Cpa=4000+0.1*T[0]+10**-2*T[0]**2
        Cpb=3000+0.2*T[1]+5*10**-2*T[1]**2
        w=(-P*U*(T[0]-T[1]))/Ma/Cpa
        v=(-P*U*(T[0]-T[1]))/Mb/Cpb
        return [w,v]
    
    x=np.arange(0,10,dx)
    y=[400,guess]
    z=odeint(ameyak,y,x)
    #print(x)
    #print(z)
    #print(z[n-1,1])

    while(z[n-1,1]>300):
        guess=guess-0.001
        y=[400,guess]
        z=odeint(ameyak,y,x)

    #print(guess)
    #print(z)

    from scipy.integrate import quad
    def integrand1(u):
        return (4000+0.1*u+u**2/100)
    def integrand2(p):
        return (3000+0.2*p+5*p**2/100)

    result1, err1 = quad(integrand1, 400, z[n-1,0] )
    result2, err2 = quad(integrand2, guess , z[n-1,1] )

    #print(result1)
    #print(result2)
    
    error=(result1-2*result2)*100/result1
    #print(error)
    list_of_error += [error]
    print n, error
    
    plt.plot([n], [error], 'ro')
plt.show()