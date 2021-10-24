import numpy as np
import time
from RandomGenerator import pseudo_uniform

def pseudo_poisson(alpha=5, size=1):
    poisson =  []
    for _ in range(size):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudo_uniform(seed=seed, size=5*alpha)
        X,P,i = 0,1,0
        while P>= np.exp(-alpha):
            P = U[i]*P
            X+=1
            i+=1
        poisson.append(X)
    return np.array(poisson)

print("Poisson is: ")
print(pseudo_poisson())