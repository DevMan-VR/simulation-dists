# importando modulos necesarios
#%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 

def NormalGraph(mu=0, sigma=0.2, size=1000,seed=2021):

    np.random.seed(seed) # replicar random

    # parametros esteticos de seaborn
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})
    # Graficando histograma
    #mu, sigma = 0, 0.2 # media y desvio estandar
    datos = np.random.normal(mu, sigma, size) #creando muestra de datos

    # histograma de distribución normal.
    cuenta, cajas, ignorar = plt.hist(datos, 20)
    plt.ylabel('frequencia')
    plt.xlabel('valores')
    plt.title('Histograma')
    plt.show()


NormalGraph(5,0.5,2000,721331)