import numpy as np

#using np.append
a=np.array([1,2,3])
b=np.append(0,a[::-1])
b=b[::-1]
b=np.append(0,b)
print("1.\nb=",b)

#using slicing
b=np.full(5,0)
b[1:4]=a[::1]
print("1.\nb=",b)

#using concatenate
c=np.array([0])
b=np.concatenate((c,a,c),axis=None)
print("1.\nb=",b)
