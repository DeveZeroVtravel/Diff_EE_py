import numpy as np
a=np.arange(0,12.2,1.1,)
print('v=',a)
b=a[::-1]
print('\nvi=',b)
print('\nv1=',a[::2])
print('v2=',a[1::2])
print('\nv1=',a[::3])
print('v2=',a[1::3])
print('v3=',a[2::3])
print('\nv1=',a[::4])
print('v2=',a[1::4])
print('v3=',a[2::4])
print('v4=',a[3::4])