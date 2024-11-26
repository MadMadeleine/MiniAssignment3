import random as rd
import matplotlib.pyplot as pp

def step(b):
	return(b + rd.uniform(-1,1))

iterations = int(input("How many iterations? "))
walkers = int(input("How many walkers? "))

x = [0]
y = [0]

for i in range (walkers):
	y=[0]
	x=[0]
	for j in range (iterations):
		x.append(step(x[-1]))
		y.append(step(y[-1]))

	pp.plot(x[iterations],y[iterations],'o')
	

pp.axis((-75,75,-75,75))
pp.show()