import numpy as np
import matplotlib.pyplot as plt
import os

#Generating points on a circle
def circ_gen(O,r):
	len = 1000
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Plotting a polar point in cartesian coordinates
def polar_to_rect(r,theta,txt):
    plt.plot(r*np.cos(np.radians(theta)), r*np.sin(np.radians(theta)), 'k.')
    plt.text(r*np.cos(np.radians(theta))+0.1, r*np.sin(np.radians(theta)), txt)

O = np.array([0.0,0.0])
r = 1
C = circ_gen(O,r)
plt.plot(C[0],C[1])
polar_to_rect(r,30,'P$_1$')
polar_to_rect(r,150,'P$_2$')
polar_to_rect(r,210,'P$_3$')
polar_to_rect(r,330,'P$_4$')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/circle.png')
os.system('termux-open ../figs/circle.png')
