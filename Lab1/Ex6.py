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
    reNum1=np.linspace(1,199,100)
    reNum2=np.linspace(2,200,100)
    # print(reNum2,'\n')
    sumSinh=float(0)
    sumCosh=float(1)
    i=1
    while i<100:
        if np.abs(np.pow(x,reNum1[i-1])/gt(reNum1[i-1])) <= 1.e-10:
            # print('approximation of e^(',x,')=',sumSinh)
            # print('number of interation= ',i)
            break
        # print('\n ',reNum[i-1],' ',gt(reNum[i-1]))
        sumSinh+=pow(x,reNum1[i-1])/gt(reNum1[i-1])
        i+=1
    i=1
    while i<100:
        if np.abs(np.pow(x,reNum2[i-1])/gt(reNum2[i-1])) <= 1.e-10:
            # print('approximation of e^(',x,')=',sumCosh)
            # print('number of interation= ',i)
            break
        # print('\n ',reNum2[i-1],' ',gt(reNum2[i-1]))
        sumCosh+=pow(x,reNum2[i-1])/gt(reNum2[i-1])
        i+=1
    return sumSinh/sumCosh

y=np.full(50,0,dtype=float)
y2=np.full(50,0,dtype=float)
x=np.linspace(-3,3,num=50)
i=0

# print(x[49],'\n')
while i < len(y):
    y[i]=np.tanh(x[i])
    y2[i]=app(x[i])
    i+=1
# print(y,'\n')
plt.plot(x,y,'y',linewidth=5)
plt.plot(x,y2,'b--')
# %%
