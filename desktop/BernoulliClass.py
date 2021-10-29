from tkinter import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import time
from scipy.stats.stats import sigmaclip
import seaborn as sns 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from RandomGenerator import pseudorandom_generator, pseudo_uniforme_continua


class BernoulliClass:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(master, text="p", height=4)
        self.input1 = Entry(master)
        self.label3 = Label(master, text="V.A.", height=1)
        self.input3 = Entry(master)
        self.canvas = None
        self.figure = None
        

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

        


    def renderVA(self):
        #Call VA from Normal Distribution and save as string
        self.p = float(self.input1.get())

        va = str(self.va_pseudo_bernoulli_generate())

        self.input3.delete(0, 'end')
        self.input3.insert(END,va)

        

    def removeVA(self):
        self.label3.grid_remove()
        self.input3.grid_remove()


    def renderGraph2(self):
        


    
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1,row=4)


    def renderVA(self):
        #Call VA from Normal Distribution and save as string
        self.p = float(self.input1.get())
        print("P is: ", self.p)
        va = str(self.va_pseudo_bernoulli_generate())

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
        
        self.p = float(self.input1.get())


        bernoulli = stats.bernoulli(self.p)
        x = np.arange(-1, 3)
        fmp = bernoulli.pmf(x)
 

        self.figure_FDP = Figure(figsize=(5, 4), dpi=100)
        self.canvas_FDP = FigureCanvasTkAgg(self.figure_FDP, master=self.master)  # A tk.DrawingArea.
       # x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        self.figure_FDP.add_subplot(111).plot(x, fmp, 'bo')
        self.figure_FDP.add_subplot(111).vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)

        self.canvas_FDP.draw()
        self.canvas_FDP.get_tk_widget().grid(column=1,row=5)

    def renderFPA(self):
        self.p = float(self.input1.get())
        

        bernoulli = stats.bernoulli(self.p)
        x = np.arange(-1, 3)
        fpa = bernoulli.cdf(x)

        
        self.figure_FPA = Figure(figsize=(5, 4), dpi=100)
        self.canvas_FPA = FigureCanvasTkAgg(self.figure_FPA, master=self.master)  # A tk.DrawingArea.

        self.figure_FPA.add_subplot(111).plot(x, fpa, 'bo')
        self.figure_FPA.add_subplot(111).vlines(x, 0, fpa, colors='b', lw=5, alpha=0.5)

        
        
        self.canvas_FPA.draw()
        self.canvas_FPA.get_tk_widget().grid(column=3,row=5)


    def va_pseudo_bernoulli_generate(self,size=100):

        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        B = pseudorandom_generator(seed=seed)[0]
        B = (B<=self.p).astype(int)

        return B


    #Funcion de probabilidad de densidad
    def va_pseudo_bernoulli_fpd(self,array): 

        X = np.zeros(array.size)
        for i in range(0,array.size-1):
            X[i] = (self.p)**array[i] * (1-self.p)**1-array[i]

        return X

    def va_pseudo_bernoulli_fpa(self,array): 

        si=0
        no=0
        for i in range(0,array.size-1):
            if(array[i]==1):
                si+=1
            elif(array[i]==0):
                no+=1
        return [si,no]

    #Funcion de probabilidad acumulada
    def va_pseudo_bernoulli_fpa_inverse(self,u): 

        if(u > 0 and u < self.p):
            return 0
        elif (u >= self.p and u < 1):
            return 1






        
