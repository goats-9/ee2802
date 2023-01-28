import numpy as np

#Points
A = np.array([[-4.0],[5.0]])
B = np.array([[0.0],[7.0]])
C = np.array([[5.0],[-5.0]])
D = np.array([[-4.0],[-2.0]])

#Create the matrix
M = np.hstack((C-A,D-B))

#Compute the area
ar = 0.5*np.linalg.det(M)
print(abs(ar))
