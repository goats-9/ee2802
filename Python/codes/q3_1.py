import numpy as np
from scipy.linalg import norm, inv

p1 = np.array([4.0,1.0])
p2 = np.array([6.0,5.0])
n = np.array([4.0,1.0])
c = 16.0
p = np.array([1.0])
q = np.array([0.0])
A = np.vstack((np.hstack((p,p1)), np.hstack((p,p2)), np.hstack((n,q))))
B = np.array([[-norm(p1)],[-norm(p2)],[c]])
x = inv(A)@B
#Coordinates of center of circle
print(x[0][0], x[1][0])
