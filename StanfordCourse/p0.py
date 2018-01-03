import numpy as np
M = np.array([[1,2,3],[4,5,6],[7,8,9],[0,2,2]])
a = np.array([1,1,0]).reshape(3,1)
b = np.array([-1,2,5]).reshape(3,1)
c = np.array([0,2,3,2]).reshape(4,1)
g = np.arange(0,15).reshape(3,5)
aDotb = np.dot(a[:,0],b[:,0])#dot product, [:,n] gives ith column (0-indexed)
print(aDotb)
print(np.multiply(a,b))#element wise multiplication
print((aDotb*(np.dot(M,a))))
temp=(np.multiply(M,a.reshape(1,3)))
print(temp)
print(np.sort(temp,axis=None).reshape(4,3))
