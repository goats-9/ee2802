import numpy as np
from scipy.linalg import norm
from matplotlib import pyplot as plt
import os

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

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

r = 5.0
theta = np.radians(60.0)
d = r/np.sin(theta/2.0)
A = np.array([[0.0],[0.0]])
u = np.array([[-d],[0.0]])
f = u.T@u - r**2
sig = (A+u)@(A+u).T - (A.T@A + 2*(u.T@A) + f)*np.eye(2)
w, v = np.linalg.eig(sig)
n1 = np.array([[np.sqrt(abs(w[0]))], [np.sqrt(abs(w[1]))]])
n2 = np.array([[np.sqrt(abs(w[0]))], [-np.sqrt(abs(w[1]))]])
q11 = r*n1/norm(n1) - u
q12 = r*n2/norm(n2) - u
q21 = -r*n1/norm(n1) - u
q22 = -r*n2/norm(n2) - u
C = circ_gen(-u.T, r)
L1 = line_gen(A,q21)
L2 = line_gen(A,q22)
L3 = line_gen(A,-u)
plt.plot(C[0],C[1])
plt.plot(L1[0],L1[1])
plt.plot(L2[0],L2[1])
plt.plot(L3[0],L3[1])
plt.plot(A[0][0], A[1][0], 'k.')
plt.plot(-u[0][0], -u[1][0], 'k.')
plt.plot(q11[0][0], q11[1][0], 'k.')
plt.plot(q12[0][0], q12[1][0], 'k.')
plt.plot(q21[0][0], q21[1][0], 'k.')
plt.plot(q22[0][0], q22[1][0], 'k.')
plt.text(A[0][0], A[1][0], 'A')
plt.text(-u[0][0], -u[1][0], 'O')
plt.text(q11[0][0], q11[1][0], 'P')
plt.text(q12[0][0], q12[1][0], 'Q')
plt.text(q21[0][0], q21[1][0], 'R')
plt.text(q22[0][0], q22[1][0], 'S')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/q3_2.png')
os.system('termux-open ../figs/q3_2.png')
