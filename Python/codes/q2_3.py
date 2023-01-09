import numpy as np
omat = np.array([[0.0,-1.0],[1.0,0.0]])

#Intersection of two lines
def perp_foot(n,cn,P):
  m = omat@n
  N=np.block([[n],[m]])
  p = np.zeros(2)
  p[0] = cn
  p[1] = m@P
  #Intersection
  x_0=np.linalg.inv(N)@p
  return x_0

n = np.array([3.0,-4.0])
cn = 16
P = np.array([-1.0,3.0])
print(perp_foot(n,cn,P))
