#%%
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    res=x*np.sin(3*x)
    return res
x=np.linspace(-2*np.pi,2*np.pi,num=200)
y=f(x)
plt.figure(figsize=(6,6))
plt.plot(x,y,label='x sin(3x)')

# %%
