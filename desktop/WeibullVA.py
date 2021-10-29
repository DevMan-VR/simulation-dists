import numpy as np
import time
from RandomGenerator import pseudo_uniforme_continua

def pseudo_weibull(alpha=1, lamb=1, size=1):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudo_uniforme_continua(size=size, seed=seed)
    X = -(np.log(1-U)**(1/alpha))/lamb

    return X

print("Weibull is: ")
print(pseudo_weibull(1,1))