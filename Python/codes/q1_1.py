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

A = np.array([[1.0],[2.0]])
B = np.array([[7.0],[0.0]])
C = line_gen(A,B)
plt.plot(C[0], C[1])
plt.grid()
plt.tight_layout()
plt.savefig('../figs/q1_1.png')
os.system('termux-open ../figs/q1_1.png')
