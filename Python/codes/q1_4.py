import numpy as np
from scipy.linalg import det
A = np.array([[-5],[-1]])
B = np.array([[3],[-5]])
C = np.array([[5],[2]])
v1 = B - A
v2 = C - A
print(0.5*det(np.hstack((v1,v2))))
