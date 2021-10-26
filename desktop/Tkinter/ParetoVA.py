import numpy as np
import time
from RandomGenerator import pseudo_uniforme_continua

def pseudo_pareto(alpha=1, xm=1, size=1):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudo_uniforme_continua(size=size, seed=seed)
    X = xm/(1-U)**(1/alpha)

    return X
