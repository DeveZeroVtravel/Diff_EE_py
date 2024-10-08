import numpy as np
import math
def f(x):
    res=x*pow(math.e,x)
    return res
print('f(2)=',f(2))
def g(z):
    res=z/(math.sin(z)*math.cos(z))
    return res 
print('g(pi/4)=',g(math.pi/4))
def h(x,y):
    res=x*y/(pow(x,2)+pow(y,2))
    return res
print('h(2,4)=',h(2,4))