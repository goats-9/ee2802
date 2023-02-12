# Import packages.
import cvxpy as cp
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

#Generate the required parabola
def parab_gen(x,a):
    return x**2/a

V = np.array([[0,0],[0,1]])
u = np.array([[-2],[0]])
f = 0

def qp_solve(m):
    # Define and solve the CVXPY problem.
    x = cp.Variable((2,1))
    b = 1+m*m
    V1 = np.array([[m*m,-m],[-m,1]])/b
    c = 1.0/b
    u1 = np.array([[m],[-1]])/b
    constraints = [cp.quad_form(x,V) + (2*u.T)@x + f <= 0]
    prob = cp.Problem(cp.Minimize(cp.quad_form(x,V1) + (2*u1.T)@x + c), constraints)
    prob.solve()
    return prob.value

qp_solve_vec = np.vectorize(qp_solve, otypes=['double'])
m = np.linspace(0,10,101)
M = qp_solve_vec(m)
xt = np.linspace(0,10,11)
plt.plot(m,M)
plt.xticks(xt)
plt.xlabel('m')
plt.ylabel('Cost')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/qp.png')
os.system('termux-open ../figs/qp.png')
