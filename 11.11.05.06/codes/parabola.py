import numpy as np
import matplotlib.pyplot as plt
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

#Generating points on a parabola
def parab_gen(x,a):
	y = x**2/a
	return y

X = np.linspace(-8,8,10000)
a = 12
P = np.array([[0.0],[0.0]])
A = np.array([[-6.0],[3.0]])
B = np.array([[6.0],[3.0]])
L1=line_gen(A,B)
L2=line_gen(B,P)
L3=line_gen(P,A)
plt.plot(X,parab_gen(X,a))
plt.plot(L1[0],L1[1],'b')
plt.plot(L2[0],L2[1],'b')
plt.plot(L3[0],L3[1],'b')
plt.plot(P[0],P[1],'k.')
plt.text(P[0],P[1]-2e-1,'P')
plt.plot(A[0],A[1],'k.')
plt.text(A[0]+1e-2,A[1]+1e-2,'A')
plt.plot(B[0],B[1],'k.')
plt.text(B[0]+1e-2,B[1]+1e-2,'B')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/parabola.png')
os.system('termux-open ../figs/parabola.png')
