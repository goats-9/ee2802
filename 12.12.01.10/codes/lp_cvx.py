import cvxpy as cp
import numpy as np

#Variables
x = cp.Variable()
y = cp.Variable()

#Problem
prob = cp.Problem(cp.Maximize(x+y), [x-y<=-1, -x+y<=0, x>=0, y>=0])

#Solution and status
prob.solve()
print(prob.status)
