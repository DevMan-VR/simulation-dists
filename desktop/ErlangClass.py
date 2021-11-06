#
# En la teoría de la probabilidad y estadística, la distribución Erlang, 
# es una distribución de probabilidad continua con dos parámetros dados por
#
#    n = n es el factor de forma de la distribución.
#    λ = lambda es el factor de proporción de la distribución.
#
#
#

from tkinter import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import time
import math

from RandomGenerator import pseudo_uniforme_continua, pseudorandom_generator

class ErlangClass:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(master, text="Factor de forma (n)", height=4)
        self.input1 = Entry(master)
        self.label2 = Label(master, text="Factor de proporción (\u03BB)", height=4)
        self.input2 = Entry(master)
        self.label3 = Label(master, text="V.A.", height=1)
        self.input3 = Entry(master)
        self.canvas_FDP = None
        self.canvas_FPA = None
        self.figure = None
        self.name="Erlang"
        

        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma
        #Input3 = VARIABLE ALEATORIA


    def renderWidgets(self):
        self.label1.grid(column=0,row=1)
        self.input1.grid(column=1,row=1)

        self.label2.grid(column=0,row=2)
        self.input2.grid(column=1,row=2)

        self.label3.grid(column=0,row=3)
        self.input3.grid(column=1,row=3)



          



    def removeWidgets(self):
        self.label1.grid_remove()
        self.input1.grid_remove()

        self.label2.grid_remove()
        self.input2.grid_remove()

        self.label3.grid_remove()
        self.input3.grid_remove()

        


    def renderVA(self):
        #Call VA from Normal Distribution and save as string

        va = str(self.funcion_densidad_acumulada_inversa())

        self.input3.delete(0, 'end')
        self.input3.insert(END,va)

        

    def removeVA(self):
        self.label3.grid_remove()
        self.input3.grid_remove()


    def renderGraph(self):
        self.renderFDP()
        self.renderFPA()


    def renderGraph(self):
        self.renderFDP()
        self.renderFPA()


    def renderFDP(self):


        n = int(self.input1.get())
        lamb = float(self.input2.get())

        x = np.arange(self.funcion_densidad_acumulada_inversa2(0.01),
                    self.funcion_densidad_acumulada_inversa2(0.99))
        fdp = self.funcion_densidad(x)  # Función de densidad de Probabilidad




        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.figure.add_subplot(111).plot(x, fdp)

        
        self.canvas_FDP = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas_FDP.draw()
        self.canvas_FDP.get_tk_widget().grid(column=1,row=5)


    def renderFPA(self):

        n = int(self.input1.get())
        lamb = float(self.input2.get())
        x = np.arange(self.funcion_densidad_acumulada_inversa2(0.01),
                    self.funcion_densidad_acumulada_inversa2(0.99))
        fpa = self.funcion_densidad_acumulada(x) # Función de densidad de Probabilidad




        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.figure.add_subplot(111).plot(x, fpa)

        
        self.canvas_FPA = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas_FPA.draw()
        self.canvas_FPA.get_tk_widget().grid(column=3,row=5)




    def clearGraph(self):
        self.canvas_FDP.get_tk_widget().grid_remove()
        self.canvas_FPA.get_tk_widget().grid_remove()


        

    def funcion_densidad(self,x):

        n = int(self.input1.get())
        lamb = float(self.input2.get())

        upperFn = ((lamb*(lamb*x)**(n-1))* np.exp(-lamb*x))

        lowerFn = np.math.factorial(n-1)

        fn = upperFn/lowerFn

        return fn


    def funcion_densidad_acumulada(self):

        n = int(self.input1.get())
        lamb = float(self.input2.get())
        res = 1

        for i in range(0,n-1):
            fn = (((lamb*x)**i)*np.exp(-lamb*x)) / np.math.factorial(i)

        res = 1 - fn

        return res

    def funcion_densidad_acumulada_inversa(self,x):

        n = int(self.input1.get())
        lamb = float(self.input2.get())

        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(size=n, seed=seed)
        sum=0
        for i in range(1,k):
            sum += math.log(U[i])
        
        sum = -(1/lamb)*sum
        

        return sum


    def funcion_densidad_acumulada_inversa2(self,x):

        n = int(self.input1.get())
        lamb = float(self.input2.get())

        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        sum=0
        for i in range(1,n):
            sum += math.log(x)
        
        sum = -(1/lamb)*sum
        

        return sum








