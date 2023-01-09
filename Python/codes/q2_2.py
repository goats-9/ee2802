import numpy as np

n1 = np.array([[np.sqrt(3.0)],[1.0]])
n2 = np.array([[1.0],[np.sqrt(3.0)]])
N = n1.T@n2
D = np.linalg.norm(n1)*np.linalg.norm(n2)
A = np.degrees(np.arccos(N/D)[0][0])
print(A)
