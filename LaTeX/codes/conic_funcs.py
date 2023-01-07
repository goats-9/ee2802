import numpy as np
from params import *

#Generating points on a circle
def circ_gen(O,r):
	theta = np.linspace(0,2*np.pi,num)
	x_circ = np.zeros((2,num))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generating points on an ellipse
def ellipse_gen(a,b):
	theta = np.linspace(0,2*np.pi,num)
	x_ellipse = np.zeros((2,num))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#Generating points on a parabola
def parab_gen(y,a):
	x = y**2/a
	return x

#Generating points on a standard hyperbola 
def hyper_gen(y):
	x = np.sqrt(1+y**2)
	return x
