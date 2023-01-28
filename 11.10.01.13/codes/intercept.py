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

#Points
A = np.array([[2.0],[3.0]])
B = np.array([[5.0],[0.0]])
C = np.array([[0.0],[5.0]])

L = line_gen(B,C)
plt.plot(A[0][0], A[1][0], 'k.')
plt.plot(B[0][0], B[1][0], 'k.')
plt.plot(C[0][0], C[1][0], 'k.')
plt.plot(L[0], L[1], 'b')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/intercept.png')
os.system('termux-open ../figs/intercept.png')
