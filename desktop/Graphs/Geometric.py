import time
from RandomGenerator import pseudo_uniform

def pseudo_geometric(p=0.5, k=10,size=1):
    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    P = pseudo_uniform(seed=seed,size=size)
    P = (P<=p).astype(int)

    prob = ((1-p)**(k-1)) * P

    return prob


print("Geometric is: ")#Deberia retornar la probabilidad de exito en la cantidad de veces definidas
print(pseudo_geometric())

#The geometric distribution gives the probability 
# that the first occurrence of success requires k
#  independent trials, each with success probability p. 
# If the probability of success on each trial
#  is p, then the probability that the kth trial 
# (out of k trials) is the first success is