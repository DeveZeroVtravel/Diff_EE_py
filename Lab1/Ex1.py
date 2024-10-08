import numpy as np
import matplotlib.pyplot as plt
import time
x= float(input('x='))
print('e^(',x,')=',np.exp(x))
sum=float(1)
i=1
def gt(n):
    y=1
    res=1
    while y<=n:
        res*=y
        y+=1
    return res

while i<100:
    if np.abs(np.pow(x,i)/gt(i)) <= 1.e-10:
        print('approximation of e^(',x,')=',sum)
        print('number of interation= ',i)
        break
    # print('\n ',i,' ',gt(i))
    sum+=pow(x,i)/gt(i)
    i+=1