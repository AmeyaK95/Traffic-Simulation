# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 18:44:39 2016

@author: Ameya
"""
# NAGEL SCHRECKENBERG MODEL
from random import uniform, shuffle
#getting a random car distribution for initializing
import matplotlib.pyplot as plt
import numpy as np
 
L = 500 
# number of cells in row
num_iters = 500 
# number of iterations
density = 0.35 
# how many positives
vmax = 5
#the maximum attainable speed in miles/hr
p = 0.3
#stochastic probability of braking of cars
# if p=0.3 then 30% of the cars will brake at every iteration

cars_num = int(density * L)
initial = [0] * cars_num + [-1] * (L - cars_num)
shuffle(initial)

iterations = [initial]

for i in range(num_iters):
	prev,curr = iterations[-1],[-1] * L

	for x in range(L):
		if prev[x] > -1:
			vi = prev[x]
			d = 1
			while prev[(x + d) % L] < 0:
				d += 1

			vtemp = min(vi+1, d - 1, vmax) # increse speed up to max speed, but don't move further than next car
			v = max(vtemp - 1, 0) if uniform(0,1) < p else vtemp # with probability p hit the brakes, otherwise sustain velocity
			curr[(x + v) % L] = v # perform the move
			#print(x,v)

	iterations.append(curr)


a = np.zeros(shape=(num_iters,L))
for i in range(L):
	for j in range(num_iters):
		a[j,i] = 1 if iterations[j][i] > -1 else 0
 
# showing image
plt.imshow(a, cmap="Greys", interpolation="nearest")
#converting the array into an image
plt.show() 


