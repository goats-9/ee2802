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

A = np.array([[0.0],[1.0]])
B = np.array([[5.0],[6.0]])
O = np.array([[0.0],[0.0]])
C = np.array([[5.0],[5.0]])
L1 = line_gen(A,B)
L2 = line_gen(O,C)
L3 = line_gen(A,O)
plt.plot(L1[0],L1[1])
plt.plot(L2[0],L2[1])
plt.plot(L3[0],L3[1])
plt.fill_between(L1[0],L1[1],6)
plt.fill_between(L2[0],L2[1],0)
plt.legend(['$x - y \leq 1$', '$-x + y \leq 0$'])
plt.grid()
plt.tight_layout()
plt.savefig('../figs/lp.png')
os.system('termux-open ../figs/lp.png')
