import numpy as np
import time
from RandomGenerator import  pseudo_uniforme_discreta
#REVISARR
def pseudo_poisson(alpha=2, size=1):
    return np.random.poisson(lam=2, size=1)[0]


print (pseudo_poisson())