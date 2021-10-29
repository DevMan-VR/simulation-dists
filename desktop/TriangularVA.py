
from RandomGenerator import pseudo_uniforme_continua
import time
def pseudo_triangular(low=0, high=1, mode=3):

    t = time.perf_counter()
    seed1 = int(10**9*float(str(t-int(t))[0:]))
    seed2 = int(10**9*float(str(t-int(t))[0:]))

    while True:
        proposal = pseudo_uniforme_continua(low, high,seed1,1)
        if proposal < mode:
            acceptance_prob = (proposal - low) / (mode - low)
        else:
            acceptance_prob = (high - proposal) / (high - mode)
        if pseudo_uniforme_continua(low,high,seed2,1) < acceptance_prob: break
    return proposal

