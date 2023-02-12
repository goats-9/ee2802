# Import packages.
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import os

n = 3
A = np.array([[0,0,-2],[0,1,0],[-2,0,0]])

def sdp_solve(m):
    # Define and solve the CVXPY problem.
    X = cp.Variable((n,n), PSD=True)
    b = 1+m*m
    C = np.array([[m*m,-m,m],[-m,1,-1],[m,-1,1]])/b
    constraints = [cp.trace(A@X) <= 0]
    prob = cp.Problem(cp.Minimize(cp.trace(C@X)), constraints)
    prob.solve()
    return abs(prob.value)

sdp_solve_vec = np.vectorize(sdp_solve, otypes=['double'])
m = np.linspace(0,10,1001)
M = sdp_solve_vec(m)
print(M)
xt = np.linspace(0,10,11)
plt.xticks(xt)
plt.xlabel('m')
plt.ylabel('Cost')
plt.semilogy(m,M)
plt.grid()
plt.tight_layout()
plt.savefig('../figs/sdp.png')
os.system('termux-open ../figs/sdp.png')
