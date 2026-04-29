import numpy as np

M1= np.array([[1,2], [3,4]])
M2= np.array([[5,6], [7,8]])
print ("Addision of M1 and M2 is: \n", M1 + M2)
print ("Subtraction of M1 and M2 is: \n", M1 - M2)
print ("scalar multiplication of M1 and 2 is: \n", 2 * M1)
print("matrix multiplication \n", np.dot(M1, M2))

I = np.eye(2)
print("Identity matrix: \n", I)

Z = np.zeros((2,2))
print("Zero matrix: \n", Z)

D = np.diag([1,2])
print("Diagonal matrix: \n", D)
V= np.array([5,6])
print("Vector: \n", V)