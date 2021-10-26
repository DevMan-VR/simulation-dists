from tkinter import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

from BinomialVA import pseudo_binomial

class BinomialClass:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(master, text="N", height=4)
        self.input1 = Entry(master)
        self.label2 = Label(master, text="p", height=4)
        self.input2 = Entry(master)
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

        va = str(pseudo_binomial())

        self.input3.delete(0, 'end')
        self.input3.insert(END,va)

        

    def removeVA(self):
        self.label3.grid_remove()
        self.input3.grid_remove()


    def renderGraph(self):

        #np.random.seed(seed) # replicar random

        # Graficando histograma
        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma
        N, p = 30, 0.4 # parametros de forma 
        binomial = stats.binom(N, p) # Distribución
        x = np.arange(binomial.ppf(0.01),
                    binomial.ppf(0.99))
        fmp = binomial.pmf(x) # Función de Masa de Probabilidad



        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.figure.add_subplot(111).plot(x, fmp, '--')
        self.figure.add_subplot(111).vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)

        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1,row=4)




    def clearGraph(self):
        self.canvas.get_tk_widget().grid_remove()


        
