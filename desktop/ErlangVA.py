import time
import math
from RandomGenerator import pseudo_uniforme_continua, pseudorandom_generator

def pseudo_erlang(k=100, lamb=5):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudorandom_generator(size=k, seed=seed)
    sum=0
    for i in range(1,k):
        sum += math.log(U[i])
    
    sum = -(1/lamb)*sum
    

    return sum
