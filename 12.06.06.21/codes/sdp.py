# Import packages.
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import os

# Generate the SDP
n = 3
C = np.eye(n)
C[2][2] = 0
A = cp.Parameter((3,3))

def sdp_solve(mval):
    # Define and solve the CVXPY problem.
    # Create a symmetric matrix variable.
    X = cp.Variable((n,n), symmetric=True)
    # The operator >> denotes matrix inequality.
    constraints = [X >> 0, cp.trace(A@X) == 0]
    prob = cp.Problem(cp.Minimize(cp.trace(C@X)), constraints)
    A.value = np.array([[1,mval,-2],[mval,mval**2,-2*mval],[-2,-2*mval,0]])
    prob.solve()
    return abs(np.trace(C@X.value))

sdp_solve_vec = np.vectorize(sdp_solve, otypes=['double'])
m = np.linspace(-5,5,100)
xt = np.linspace(-5,5,11)
M = sdp_solve_vec(m)
plt.plot(m,M)
plt.grid()
plt.xticks(xt)
plt.plot([-1,1],[sdp_solve(-1),sdp_solve(1)],'k.')
plt.xlabel('$m$')
plt.ylabel('tr($CX$)')
plt.tight_layout()
plt.savefig('../figs/sdp.png')
os.system('termux-open ../figs/sdp.png')
