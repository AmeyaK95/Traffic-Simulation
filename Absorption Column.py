# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:48:57 2016

@author: Ameya
"""
import numpy as np;import matplotlib.pyplot as plt;from scipy.optimize import fmin

#KL1a=7.48 ----------------Mass transfer coefficient for CO2 in (1/hr) units ;(7.48/3600 in 1/sec units)
#reference no. 1
KL1a=0.00194444#-----------Mass transfer coefficient for CH4 SIUnits(1/s)
#KL2a=0.09-----------------Mass transfer coefficient for CH4 in (1/hr) units ;(0.09/3600 in 1/sec units)
#reference no. 2
KL2a=0.000025
KGa=0.000002452 #----------Mass transfer coefficient for H2O SIUnits(1/s)
W=5 #----------------------Unit width of column SIUnits(m)
H=5.0 #--------------------Column Height SIUnits(m)
n=10 #---------------------Grid Divisions SIUnits(-)
dz=H/(n-1) #---------------differential grid length SIUnits(m)
A=W*dz #-------------------differential area for transfer SIUnits(m^2)
P=101325 #-----------------Column operating pressure SIUnits(Pa)
Psat=4245.5 #--------------Saturation Pressure for H20 SIUnits(Pa)
#reference no. 3
H1=2941.176471 #-----------Henry's Constant for CO2 SIUnits(Pa.m^3/mol)
H2=71428.57143 #-----------Henry's Constant for CH4 SIUnits(Pa.m^3/mol)
xstart1=0.5 #--------------Mole frac of CO2(gas side) at bottom SIUnits(-)
xstart2=0.5 #--------------Mole frac of CH4(gas side) at bottom SIUnits(-)
Gtotal=1000 #--------------Total molar flow rate(gas side) at bottom SIUnits(mol/hr))
Lend=1000 #----------------Required molar flow rate of H2O at column top SIUnits(mol/hr)
T=np.zeros((n,6)) #--------Define array of Molar flow rates of all components across a cross-section
J=[10,10,10] #-------------Guessed Values of molar flow rates(liquid side) at the bottom
    
def ameya(J):
    T[0,0]=50;T[0,1]=50;T[0,2]=0;T[0,3]=J[0];T[0,4]=J[1];T[0,5]=J[2]
    for i in range(n-1):
        T[i+1,0] = T[i,0]-KL1a*A*dz*((T[i,0]/(T[i,0]+T[i,1]+T[i,2]))*P/H1)
        T[i+1,3] = T[i,3]-KL1a*A*dz*((T[i,0]/(T[i,0]+T[i,1]+T[i,2]))*P/H1)
        T[i+1,1] = T[i,1]-KL2a*A*dz*((T[i,1]/(T[i,0]+T[i,1]+T[i,2]))*P/H2)
        T[i+1,4] = T[i,4]-KL2a*A*dz*((T[i,1]/(T[i,0]+T[i,1]+T[i,2]))*P/H2)
        T[i+1,2] = T[i,2]+KGa*A*dz*(P-Psat)
        T[i+1,5] = T[i,5]+KGa*A*dz*(P-Psat)
        error=T[n-1,3]*T[n-1,3]+T[n-1,4]*T[n-1,4]+(Lend-T[n-1,5])*(Lend-T[n-1,5])
    return error 
J= [40,40,600]   
J = fmin(ameya, J) #-------Least square error minimizer
x=np.zeros((n,6)) #--------Define array of mol frac of all components
x[0,0]=xstart1;x[0,1]=xstart2;x[0,2]=0;x[0,3]=J[0]/(J[0]+J[1]+J[2]);x[0,4]=J[1]/(J[0]+J[1]+J[2]);x[0,5]=J[2]/(J[0]+J[1]+J[2])
T[0,0]=x[0,0]*Gtotal;T[0,1]=x[0,1]*Gtotal;T[0,2]=0;T[0,3]=J[0];T[0,4]=J[1];T[0,5]=J[2]
x[0,0]=T[0,0]/(T[0,0]+T[0,1]+T[0,2]);x[0,1]=T[0,1]/(T[0,0]+T[0,1]+T[0,2])
x[0,2]=T[0,2]/(T[0,0]+T[0,1]+T[0,2]);x[0,3]=T[0,3]/(T[0,3]+T[0,4]+T[0,5])
x[0,4]=T[0,4]/(T[0,3]+T[0,4]+T[0,5]);x[0,5]=T[0,5]/(T[0,3]+T[0,4]+T[0,5])
z=np.linspace(0,H,n)
for i in range(n-1):
    z[i+1]=0+dz*i
    T[i+1,0] = T[i,0]-KL1a*A*dz*((T[i,0]/(T[i,0]+T[i,1]+T[i,2]))*P/H1)
    T[i+1,3] = T[i,3]-KL1a*A*dz*((T[i,0]/(T[i,0]+T[i,1]+T[i,2]))*P/H1)
    T[i+1,1] = T[i,1]-KL2a*A*dz*((T[i,1]/(T[i,0]+T[i,1]+T[i,2]))*P/H2)
    T[i+1,4] = T[i,4]-KL2a*A*dz*((T[i,1]/(T[i,0]+T[i,1]+T[i,2]))*P/H2)
    T[i+1,2] = T[i,2]+KGa*A*dz*(P-Psat)
    T[i+1,5] = T[i,5]+KGa*A*dz*(P-Psat)
    x[i+1,0]=T[i+1,0]/(T[i+1,0]+T[i+1,1]+T[i+1,2])
    x[i+1,1]=T[i+1,1]/(T[i+1,0]+T[i+1,1]+T[i+1,2])
    x[i+1,2]=T[i+1,2]/(T[i+1,0]+T[i+1,1]+T[i+1,2])
    x[i+1,3]=T[i+1,3]/(T[i+1,3]+T[i+1,4]+T[i+1,5])
    x[i+1,4]=T[i+1,4]/(T[i+1,3]+T[i+1,4]+T[i+1,5])
    x[i+1,5]=T[i+1,5]/(T[i+1,3]+T[i+1,4]+T[i+1,5])
    plt.plot(z[i+1],x[i+1,0],'ro')
    plt.plot(z[i+1],x[i+1,1],'bo')
plt.xlabel('Column Height')
plt.ylabel('Gas Phase Mole Fractions')
plt.title('x-mol frac vs H-height-(BLUE-CO2;RED-CH4)')

print ('Initial Values of Gas Molar flow Rate - CO2 , CH4 , H2O');print (T[0,0],T[0,1],T[0,2])
print ('Final Values of Gas Molar flow Rate - CO2 , CH4 , H2O');print (T[n-1,0],T[n-1,1],T[n-1,2])
print ('Initial Values of Liquid Molar flow Rate - CO2 , CH4 , H2O');print J
print ('Final Values of Liquid Molar flow Rate - CO2 , CH4 , H2O');print (T[n-1,3],T[n-1,4],T[n-1,5])
print ('Initial Values of Gas Mole Fractions - CO2 , CH4 , H2O');print (x[0,0],x[0,1],x[0,2])
print ('Final Values of Gas Mole Fractions - CO2 , CH4 , H2O');print (x[n-1,0],x[n-1,1],x[n-1,2])
print ('Initial Values of Liquid Mole Fractions Rate - CO2 , CH4 , H2O');print (x[0,3],x[0,4],x[0,5])
print ('Final Values of Liquid Mole Fractions - CO2 , CH4 , H2O');print (x[n-1,3],x[n-1,4],x[n-1,5])
plt.show()

#print T
#print ('')
#print x

    