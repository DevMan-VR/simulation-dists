import numpy as np
import time
from RandomGenerator import pseudo_uniform

def pseudo_exp(lamb, size=100):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudo_uniform(size=size, seed=seed)
    X = -(1/lamb)*(np.log(1-U))

    return X

print("Exponential is: ")
print(pseudo_exp(0.1))