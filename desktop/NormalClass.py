from tkinter import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

from NormalVA import pseudo_normal

class NormalClass:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(master, text="mu", height=4)
        self.input1 = Entry(master)
        self.label2 = Label(master, text="sigma", height=4)
        self.input2 = Entry(master)
        self.label3 = Label(master, text="V.A.", height=1)
        self.input3 = Entry(master)
        self.canvas_FDP = None
        self.canvas_FPA = None
        self.figure = None
        self.name="Normal"
        

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
        mu = float(self.input1.get())
        sigma = float(self.input2.get())
        va = str(pseudo_normal(mu,sigma))

        self.input3.delete(0, 'end')
        self.input3.insert(END,va)

        

    def removeVA(self):
        self.label3.grid_remove()
        self.input3.grid_remove()


    def renderGraph(self):
        self.renderFDP()
        self.renderFPA()

    def renderFDP(self):

        #np.random.seed(seed) # replicar random

        # Graficando histograma
        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma

        mu = float(self.input1.get())
        sigma = float(self.input2.get())

        #datos = np.random.normal(mu,sigma , 1000) #creando muestra de datos

        self.figure = Figure(figsize=(5, 4), dpi=100)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        self.figure.add_subplot(111).plot(x, stats.norm.pdf(x, mu, sigma))

        
        self.canvas_FDP = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas_FDP.draw()
        self.canvas_FDP.get_tk_widget().grid(column=1,row=4)

    def renderFPA(self):

        #np.random.seed(seed) # replicar random

        # Graficando histograma
        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma
        mu = float(self.input1.get())
        sigma = float(self.input2.get())

        normal = stats.norm()
        x = np.linspace(normal.ppf(0.01),normal.ppf(0.99), 100)

        fpa = normal.cdf(x,mu,sigma)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.figure.add_subplot(111).plot(x, fpa)

        
        self.canvas_FPA = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas_FPA.draw()
        self.canvas_FPA.get_tk_widget().grid(column=3,row=4)




    def clearGraph(self):
        self.canvas_FDP.get_tk_widget().grid_remove()
        self.canvas_FPA.get_tk_widget().grid_remove()


        
