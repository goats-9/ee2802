import numpy as np

def dot_prod(A,B,C):
    return (B-A).T@(C-A)

A = np.array([[3.0],[-4.0],[-4.0]])
B = np.array([[2.0],[-1.0],[1.0]])
C = np.array([[1.0],[-3.0],[-5.0]])

p = dot_prod(A,B,C)
q = dot_prod(B,C,A)
r = dot_prod(C,A,B)

#Check and print output
print("Triangle ABC is", end=" ")
if p == 0:
    print("right angled at A.")
elif q == 0:
    print("right angled at B.")
elif r == 0:
    print("right angled at C.")
else:
    print("not right angled.")
