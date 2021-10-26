import numpy as np
import time
from RandomGenerator import pseudo_uniforme_continua
from scipy import integrate

def normal_probability_density(x):
    constant = 1.0/np.sqrt(2*np.pi)
    return (constant * np.exp((-x**2)/2.0))

def pseudo_normal_st(mu=0, sigma=1, size=1):
    t = time.perf_counter()
    seed1 = int(10**9*float(str(t-int(t))[0:]))
    U1 = pseudo_uniforme_continua(seed=seed1,size=size)
    t = time.perf_counter()
    seed2 = int(10**9*float(str(t-int(t))[0:]))
    U2 = pseudo_uniforme_continua(seed=seed2, size=size)

    Z0 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    Z1 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)


    P,_ = integrate.quad(normal_probability_density,np.NINF,Z0)


    return P

print("Normal Standard is: ")
print(pseudo_normal_st(0,1))