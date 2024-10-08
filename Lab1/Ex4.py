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
    reNum=np.linspace(1,199,100)
    # print(reNum,'\n')
    adj=1 
    sum=float(0)
    i=1
    while i<100:
        if np.abs(np.pow(x,reNum[i-1])/gt(reNum[i-1])) <= 1.e-10:
            print('approximation of e^(',x,')=',sum)
            print('number of interation= ',i)
            break
        # print('\n ',reNum[i-1],' ',gt(reNum[i-1]))
        sum+=pow(x,reNum[i-1])/gt(reNum[i-1])*adj
        i+=1
        adj*=-1
    return sum

y=np.full(50,0,dtype=float)
y2=np.full(50,0,dtype=float)
x=np.linspace(-np.pi,np.pi,num=50)
i=0

# print(x[49],'\n')
while i < len(y):
    y[i]=np.sin(x[i])
    y2[i]=app(x[i])
    i+=1
# print(y,'\n')
plt.plot(x,y,'y',linewidth=5)
plt.plot(x,y2,'b--')
