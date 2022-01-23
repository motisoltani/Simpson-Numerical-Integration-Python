'''
Numerical Integration 
Simpson's rule

language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

import numpy as np

def simps(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

print(simps(lambda x : 3*x**2,0,1,10))
print(simps(np.sin,0,np.pi/2,100))
