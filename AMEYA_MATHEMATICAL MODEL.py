import numpy as np
import scipy
import matplotlib.pyplot as plt
L=50
T=180
vmax=60
Rmax=250
dx=10
dt=0.1
n1=(L/dx)
n2=(T/dt)
R=np.zeros((n1+1,n2+1))
Q=np.zeros((n1+1,n2+1))

for q in range(n2+1):
    R[0,q]=21
    
for s in range(1,(n1+1)/3):
    R[s,0]=25
for s in range((n1+1)/3,2*(n1+1)/3),:
    R[s,0]=10
for s in range(2*(n1+1)/3,(n1+1)):
    R[s,0]=5
    
for j in range(n2+1):
    for i in range(n1+1):  
        Q[i,j] = R[i,j]*vmax*(1-(R[i,j]/Rmax)**2)
#print Q        
for j in range(n2):
    for i in range(1,n1+1):
        
        R[i,j+1] = R[i,j]-(dt/dx)*(Q[i,j]-Q[i-1,j])
print R
list_of_d = []
list_of_x = []
p=0
pos=0
list_of_R =[]
T1 = input("What Time1? ")
max=R[0,T1]
for i in range(n1+1):
    
    if R[i,T1] <0:
        R[i,T1]=R[i,T1]*-1
    if R[i,T1]>max:
        max=R[i,T1]
    pos=pos+dx
    
for h in range(n1+1):
    
    d=R[h,T1]/max
    #print d
    p=p+dx
    #print R[i,T1]
    list_of_x += [p]
    list_of_d += [d] 
    list_of_R += [R[h,T1]]
    plt.plot(list_of_x,list_of_d,'r')
    plt.hold(True)
plt.show()




