import numpy as np
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

omat = np.array([[0.0,1.0],[-1.0,0.0]])
n = np.array([[3.0],[-4.0]])
p = omat@n
A = np.array([[-2.0],[3.0]])
B = A+p
C = line_gen(A,B)
plt.plot(C[0],C[1])
plt.plot(A[0][0],A[1][0],'k.')
plt.text(A[0][0],A[1][0],'A')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/q2_1.png')
os.system('termux-open ../figs/q2_1.png')
