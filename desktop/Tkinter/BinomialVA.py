import numpy as np
import time
from RandomGenerator import pseudo_uniforme_continua

def pseudo_binomial(n=100,p=0.5, size=15):
    binom = []
    for _ in range(size):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudo_uniforme_continua(size=n,seed=seed)
        Y = (U <= p).astype(int)
        binom.append(np.sum(Y))

    return binom[0]
