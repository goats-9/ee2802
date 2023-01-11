import numpy as np

#Return direction vector of 
#the line given two points
def dir_vec(A,B): return B-A

#Tolerance
eps = 1e-6

#Points of the triangle
A = np.array([[1.0],[2.0],[7.0]])
B = np.array([[2.0],[6.0],[3.0]])
C = np.array([[3.0],[10.0],[-1.0]])

o = np.array([[1.0],[1.0],[1.0]])

#Direction vectors
d1 = dir_vec(A,B)
d2 = dir_vec(A,C)

#Compute determinant
D = np.linalg.det(np.hstack((o,d1,d2)))

#Check collinearity
print("Points are", end=" ")
if abs(D) < eps:
    print("collinear")
else:
    print("non-collinear")
