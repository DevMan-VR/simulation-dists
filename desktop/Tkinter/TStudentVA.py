import numpy as np
import time
import math
from NormalVA import pseudo_normal

def pseudo_tstudent(v=6, size=100):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudo_normal(5,1,1)
    #U = pseudo_uniform(size=size, seed=seed)
    X = (2*U - 1)/(2*math.gamma((v+1)/2))

    return X
