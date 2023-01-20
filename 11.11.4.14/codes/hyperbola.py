import numpy as np
import matplotlib.pyplot as plt
import os

#Generating points on a hyperbola
def hyper_gen(a,b):
	len = 10000
	theta = np.linspace(0,np.pi/3,len)
	x_hyper = np.zeros((2,len))
	x_hyper[0,:] = a/np.cos(theta)
	x_hyper[1,:] = b*np.tan(theta)
	return x_hyper

a = np.sqrt(49)
b = np.sqrt(343/9)
H = hyper_gen(a,b)
plt.plot(H[0], H[1],'b')
plt.plot(H[0], -H[1],'b')
plt.plot(-H[0], H[1],'b')
plt.plot(-H[0], -H[1],'b')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/hyperbola.png')
os.system('termux-open ../figs/hyperbola.png')
