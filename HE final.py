# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 21:03:36 2016

@author: Ameya
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

class heatexchanger:
    L=10
    P=10
    U=100
    Ma=1
    Mb=2
    n=110.0
    guess=350  # define guess value outside function definition    
    dx=L/(n)
    T = np.zeros((n,2)) #creating a n by 2 matrix i.e. array
    
    def code(self):
        L=self.L  
        P=self.P
        U=self.U
        Ma=self.Ma
        Mb=self.Mb
        n=self.n
        guess=self.guess  
        dx=self.dx
        T=self.T
        
        L=10.0
    	P=10
    	U=100
    	dx=L/(n-1)
    	Ma=1
    	Mb=2
    	T = np.zeros((n,2)) #creating a n by 2 matrix i.e. array
    	#print(T)
    	T[0,0] = 400
    	T[0,1] = 350
    	T[n-1,1]=390 # Random value to start the while loop

    	while(T[n-1,1]>300.0):
        	T[0,0] = 400
        	T[0,1] = T[0,1]-0.01 # Changing guess everytime
        	for i in range(n-1):
            		Cpa=4000+0.1*T[i,0]+T[i,0]*T[i,0]/100
            		Cpb=3000+0.2*T[i,1]+5*T[i,1]*T[i,1]/100
                	k1=(-P*U*(T[i,0]-T[i,1]))*(1/(Ma*Cpa))
                	k2=(-P*U*((T[i,0]+k1*dx/2)-T[i,1]))*(1/(Ma*(4000+0.1*(T[i,0]+k1*dx/2)+(T[i,0]+k1*dx/2)*(T[i,0]+k1*dx/2)/100)))
                	k3=(-P*U*((T[i,0]+k2*dx/2)-T[i,1]))*(1/(Ma*(4000+0.1*(T[i,0]+k2*dx/2)+(T[i,0]+k2*dx/2)*(T[i,0]+k2*dx/2)/100)))
                	k4=(-P*U*((T[i,0]+k3*dx)-T[i,1]))*(1/(Ma*(4000+0.1*(T[i,0]+k3*dx)+(T[i,0]+k3*dx)*(T[i,0]+k3*dx)/100)))
                	f1=(-P*U*(T[i,0]-T[i,1]))*(1/(Mb*Cpb))
                	f2=(-P*U*(T[i,0]-T[i,1]-f1*dx/2))*(1/(Mb*(3000+0.2*(T[i,1]+f1*dx/2)+5*(T[i,1]+f1*dx/2)*(T[i,1]+f1*dx/2)/100)))
                	f3=(-P*U*(T[i,0]-T[i,1]-f2*dx/2))*(1/(Mb*(3000+0.2*(T[i,1]+f2*dx/2)+5*(T[i,1]+f2*dx/2)*(T[i,1]+f2*dx/2)/100)))
                	f4=(-P*U*(T[i,0]-T[i,1]-f3*dx))*(1/(Mb*(3000+0.2*(T[i,1]+f3*dx)+5*(T[i,1]+f3*dx)*(T[i,1]+f3*dx)/100)))
            		T[i+1,0] = T[i,0] + (dx/6)*(k1+2*k2+2*k3+k4)
            		T[i+1,1] = T[i,1] + (dx/6)*(f1+2*f2+2*f3+f4)
            
        for i in range(n):
            print(T[i,0],T[i,1])
    		

        from scipy.integrate import quad # import the integration function
        def integrand1(u):
        	return (4000+0.1*u+u**2/100)
        def integrand2(p):
        	return (3000+0.2*p+5*p**2/100)
        #print(T[n-1,0])
        #print(T[0,1])
        result1, err1 = quad(integrand1, 400, T[n-1,0] )
        result2, err2 = quad(integrand2, T[0,1] , 300 )

        #print(result1)
        #print(result2)
    
        error=(2*result2-result1)*100/result1
        return error
        
he1=heatexchanger()
#he1.n=90.0
#he1.code()
#he2=heatexchanger()
#he3=heatexchanger()
list_of_n = [10,20,30,40,50,75,100]
list_of_c = [] #empty
list_of_error = [] #empty
for n in list_of_n:
    he1.n = n
    error = he1.code()
    print n, error
    list_of_c += [n]
    list_of_error += [error]
    
plt.plot(list_of_c,list_of_error)
plt.xlabel('grid divisions')
plt.ylabel('error %')
plt.title('Graph')
plt.show()