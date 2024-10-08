#%%
import numpy as np
import matplotlib.pyplot as plt
import time

def gt(n):
    y=1
    res=1
    while y<=n:
        res*=y
        y+=1
    return res
def app(x):
    sum=float(1)
    i=1
    while i<100:
        if np.abs(np.pow(x,i)/gt(i)) <= 1.e-10:
            # print('1\n')
            break
        # print('\n ',i,' ',gt(i))
        sum+=pow(x,i)/gt(i)
        i+=1
    return sum

y=np.full(50,0,dtype=float)
y2=np.full(50,0,dtype=float)
x=np.linspace(-1,1,num=50)
i=0

# print(x[49],'\n')
while i < len(y):
    y[i]=np.exp(x[i])
    y2[i]=app(x[i])
    i+=1
# print(y,'\n')
plt.plot(x,y,'y',linewidth=5)
plt.plot(x,y2,'b--')