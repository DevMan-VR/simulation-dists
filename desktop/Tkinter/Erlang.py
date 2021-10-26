import time
import math
from RandomGenerator import pseudo_uniforme_continua

def pseudo_erlang(k=100, lamb=5):

    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudo_uniforme_continua(size=k, seed=seed)
    array = [1,2,3,4,5]
    sum=0
    for i in range(k):
        sum += math.log(U[i])
    
    sum = -(1/lamb)*sum
    

    return sum
