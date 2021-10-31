from tkinter import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

import time
from RandomGenerator import pseudorandom_generator

class ExponentialClass:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(master, text="lambda", height=4)
        self.input1 = Entry(master)
        self.label3 = Label(master, text="V.A.", height=1)
        self.input3 = Entry(master)
        self.canvas_FDP = None
        self.canvas_FPA = None
        self.figure = None
        self.lamb = None
        self.name = "Exponencial"
        

        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma
        #Input3 = VARIABLE ALEATORIA


    def renderWidgets(self):
        self.label1.grid(column=0,row=1)
        self.input1.grid(column=1,row=1)

        self.label3.grid(column=0,row=3)
        self.input3.grid(column=1,row=3)





    def removeWidgets(self):
        self.label1.grid_remove()
        self.input1.grid_remove()


        self.label3.grid_remove()
        self.input3.grid_remove()

    def removeVA(self):
        self.label3.grid_remove()
        self.input3.grid_remove()

    def clearGraph(self):
        self.canvas_FDP.get_tk_widget().grid_remove()
        self.canvas_FPA.get_tk_widget().grid_remove()

    def renderVA(self):
        #Call VA from Normal Distribution and save as string
        self.lamb = float(self.input1.get())
        print("Self Lamb is: ", self.lamb)
        va = str(self.va_pseudo_exp_generate())

        self.input3.delete(0, 'end')
        self.input3.insert(END,va)


    def renderGraph(self):

        #np.random.seed(seed) # replicar random

        # Graficando histograma
        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma

        self.renderFDP()
        self.renderFPA()

        


    def renderFDP(self):
        self.lamb = float(self.input1.get())
        
        x = np.linspace(self.va_pseudo_exp_fpa_inverse(0.01),
                        self.va_pseudo_exp_fpa_inverse(0.99), 100)

        print("x is ::: ", x)
        #fp = exponencial.pdf(x) # Función de Probabilidad
        fp = self.va_pseudo_exp_fpd(x)



        self.figure_FDP = Figure(figsize=(5, 4), dpi=100)
        self.figure_FDP.add_subplot(111).plot(x, fp)

        
        self.canvas_FDP = FigureCanvasTkAgg(self.figure_FDP, master=self.master)  # A tk.DrawingArea.
        self.canvas_FDP.draw()
        self.canvas_FDP.get_tk_widget().grid(column=1,row=5)

    def renderFPA(self):
        self.lamb = float(self.input1.get())
        

        # Graficando Exponencial
        x = np.linspace(self.va_pseudo_exp_fpa_inverse(0.01),
                        self.va_pseudo_exp_fpa_inverse(0.99), 100)



        fp = self.va_pseudo_exp_fpa(x)
        print("Funcion de Probabilidad 2 is :::", fp)

        
        self.figure_FPA = Figure(figsize=(5, 4), dpi=100)
        self.figure_FPA.add_subplot(111).plot(x, fp)

        
        self.canvas_FPA = FigureCanvasTkAgg(self.figure_FPA, master=self.master)  # A tk.DrawingArea.
        self.canvas_FPA.draw()
        self.canvas_FPA.get_tk_widget().grid(column=3,row=5)




    


        
    def va_pseudo_exp_generate(self,size=100):

        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = -(1/self.lamb)*(np.log(1-U))
        print("U in exp is ")
        #print(U)

        return X


    #Funcion de probabilidad de densidad
    def va_pseudo_exp_fpd(self,array): 

        X = np.zeros(array.size)
        for i in range(0,array.size-1):
            X[i] = (self.lamb) * np.exp((-self.lamb)*array[i])

        return X

    def va_pseudo_exp_fpa(self,x): 

        X = 1 - np.exp(-self.lamb*x)

        return X

    #Funcion de probabilidad acumulada
    def va_pseudo_exp_fpa_inverse(self,u): 

        X = -(1/self.lamb)*(np.log(1-u))

        return X

