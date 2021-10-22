
from RandomGenerator import pseudo_uniform
import time
def random_triangular(low, high, mode):
    low = 0
    high = 1
    t = time.perf_counter()
    seed1 = int(10**9*float(str(t-int(t))[0:]))
    seed2 = int(10**9*float(str(t-int(t))[0:]))

    while True:
        proposal = pseudo_uniform(low, high,seed1,1)
        if proposal < mode:
            acceptance_prob = (proposal - low) / (mode - low)
        else:
            acceptance_prob = (high - proposal) / (high - mode)
        if pseudo_uniform(low,high,seed2,1) < acceptance_prob: break
    return proposal


print("Triangular is: ")
print(random_triangular(0,1,0.4))