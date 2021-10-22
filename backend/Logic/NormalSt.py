import numpy as np
import time
from RandomGenerator import pseudo_uniform


def pseudo_normal_st(mu=0, sigma=1, size=1):
    t = time.perf_counter()
    seed1 = int(10**9*float(str(t-int(t))[0:]))
    U1 = pseudo_uniform(seed=seed1,size=size)
    t = time.perf_counter()
    seed2 = int(10**9*float(str(t-int(t))[0:]))
    U2 = pseudo_uniform(seed=seed2, size=size)

    print(U1)
    print(U2)

    Z0 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    Z1 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)

    standard = (Z0-mu)/sigma

    print(Z0)
    print(Z1)

#Z0 = Z0*sigma+mu

    return standard

print("Normal Standard is: ")
print(pseudo_normal_st())