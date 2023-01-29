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

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating points on a parabola
def parab_gen(x,a):
	y = np.sqrt(a*x)
	return y

X = np.linspace(0,4,10000)
a = 6
r = 4
O = np.array([0.0,0.0])
C = circ_gen(O,r)
S = parab_gen(X,a)
P = np.array([[2.0],[2*np.sqrt(3)]])
Q = np.array([[2.0],[-2*np.sqrt(3)]])
plt.plot(X,S,'r')
plt.plot(X,-S,'r')
plt.plot(C[0],C[1])
plt.plot(O[0],O[1],'k.')
plt.text(O[0],O[1]-0.3,'O')
plt.plot(P[0],P[1],'k.')
plt.text(P[0],P[1]-0.3,'P')
plt.plot(Q[0],Q[1],'k.')
plt.text(Q[0],Q[1]-0.3,'Q')
plt.grid()
plt.tight_layout()
ax = plt.gca()
ax.set_aspect('equal', 'box')
plt.savefig('../figs/parab_circ.png')
os.system('termux-open ../figs/parab_circ.png')
