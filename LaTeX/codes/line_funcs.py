import numpy as np
from params import *

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@(B-A)

#Intersection of two lines
#given normal form
def line_intersect_norm(n1,c1,n2,c2):
  N=np.vstack((n1.T,n2.T))
  p=np.vstack((c1,c2))
  #Intersection
  return np.linalg.inv(N)@p

#Intersection of two lines
#given two points on each line
def line_intersect_pt(A,B,C,D):
    n1=norm_vec(A,B)
    c1=n1.T@A
    n2=norm_vec(C,D)
    c2=n2.T@C
    return line_intersect_norm(n1,c1,n2,c2)

#Foot of the perpendicular
#given the line in normal form
#and a point not on the line
def perp_foot_norm(n,c,P):
  m=omat@n
  cm=m.T@P
  return line_intersect_norm(n,c,m,cm)

#Foot of the prependicular
#given two points that lie on the line
#and a point not on the line
def perp_foot_pt(A,B,P):
    n=norm_vec(A,B)
    c=n.T@A
    return perp_foot_norm(n,c,P)
