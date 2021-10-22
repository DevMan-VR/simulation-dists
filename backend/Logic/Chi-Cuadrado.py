import numpy as np
import time
import math

import scipy
from RandomGenerator import pseudo_uniform
from Normal import pseudo_normal
from scipy import special

def pseudo_chiCuadrado(k=1, size=100):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = abs(pseudo_normal(0,1,1))
    print("U IS ")
    print(U)
    #U = pseudo_uniform(size=size, seed=seed)
    X = special.gammainc(k/2,U/2)/math.gamma(k/2)
    

    return X

print("Chi-Cuadrado is: ")
print(pseudo_chiCuadrado(6))