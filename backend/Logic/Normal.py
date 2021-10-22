import numpy as np
import time
from RandomGenerator import pseudo_uniform


def pseudo_normal(mu=0.0, sigma=1.0, size=1):
    t = time.perf_counter()
    seed1 = int(10**9*float(str(t-int(t))[0:]))
    U1 = pseudo_uniform(seed=seed1,size=size)
    t = time.perf_counter()
    seed2 = int(10**9*float(str(t-int(t))[0:]))
    U2 = pseudo_uniform(seed=seed2, size=size)


    X2 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    X1 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)

    Z = (X1 - mu)/sigma



#Z0 = Z0*sigma+mu

    return Z

print("Normal is: ")
print(pseudo_normal(0,1,1))