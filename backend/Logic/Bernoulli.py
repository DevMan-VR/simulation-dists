import time
from RandomGenerator import pseudo_uniform

def pseudo_bernoulli(p=0.5, size=1):
    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    B = pseudo_uniform(seed=seed,size=size)
    B = (B<=p).astype(int)

    return B


print("Bernoulli is: ")
print(pseudo_bernoulli()[0])