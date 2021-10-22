1. Módulo que genere números pseudo-aleatorios usando el Método Congruencial 
Multiplicativo, de acuerdo a la palabra del computador que utilice. El lenguaje a 
usar puede ser  C, o Python. 

--CHECK


2.  Módulo que genere variables aleatorias discretas y continuas, usando el módulo de 
números pseudo-aleatorios. Las distribuciones obligatorias que deben programar 
son:  (tutorial: https://towardsdatascience.com/how-to-generate-random-variables-from-scratch-no-library-used-4b71eb3c8dc7)  

    Exponencial - OK
    Erlang OK
    Normal(0,1) - PENDING (PROBLEM) Esta es clave para las demas, me falta normalizarla...
    Normal  - OK
    Uniforme continua - OK
    Chi-cuadrado - OK
    t-student - OK
    Pareto - OK
    Weibull  - OK
    Triangular - DOING  ##Revisar
    Uniforme discreta - PENDING
    Bernoulli - OK
    Poisson - OK
    Binomial - OK
    Geométrica - OK

    ***Hay que revisar por que la normal(0,1) está arrojando valores malos (negativos y no entre 0 y 1)
    
    Estas distribuciones pueden calcularse usando el método más  adecuado (que Ud. deberá investigar).  


3. Programar una Interfaz debe ser amigable e interactiva,  que permita el  ingreso de 
los parámetros característicos de las  distribuciones, y muestre como salida la 
Función de distribución acumulada, función de densidad de probabilidad o función 
de masa de probabilidad  (según corresponda). Además la Interfaz debe permitir 
escoger entre las distintas distribuciones programadas. Puede usar cualquier 
lenguaje para programar la interfaz. 


4. Se debe entregar una presentación en .ppt que contenga: 
1. Descripción del Problema  
2. Descripción de cada una de las distribuciones de probabilidad y el método 
usado para generarla  
3. Arquitectura de su programa 
4. Implementación. 
5. Conclusiones 
Obs: Esta presentación es la base para su interrogación 