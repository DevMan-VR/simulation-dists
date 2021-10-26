import time
from RandomGenerator import pseudo_uniforme_continua, pseudo_uniforme_discreta

def pseudo_bernoulli(p=0.5, size=1):
    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    B = pseudo_uniforme_continua(seed=seed,size=size,low=0,high=1)
    B = (B<=p).astype(int)

    return B

