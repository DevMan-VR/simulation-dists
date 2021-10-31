from tkinter import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

from RandomGenerator import pseudo_uniforme_continua

class UniformClass:
    def __init__(self, master):
        self.master = master
        self.label3 = Label(master, text="V.A.", height=1)
        self.input3 = Entry(master)
        self.canvas_FDP = None
        self.canvas_FPA = None
        self.figure = None
        self.name="Uniforme Continua"
        

        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma
        #Input3 = VARIABLE ALEATORIA


    def renderWidgets(self):

        self.label3.grid(column=0,row=3)
        self.input3.grid(column=1,row=3)



          
    def removeWidgets(self):

        self.label3.grid_remove()
        self.input3.grid_remove()

        


    def renderVA(self):
        #Call VA from Normal Distribution and save as string

        va = str(pseudo_uniforme_continua())

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

        uniforme = stats.uniform()
        x = np.linspace(uniforme.ppf(0.01),
                        uniforme.ppf(0.99), 100)
        fp = uniforme.pdf(x) # Función de Probabilidad




        self.figure = Figure(figsize=(5, 4), dpi=100)
       # x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        self.figure.add_subplot(111).plot(x, fp, '--')
        self.figure.add_subplot(111).vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)



    
        self.canvas_FDP = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas_FDP.draw()
        self.canvas_FDP.get_tk_widget().grid(column=1,row=4)


    def renderFPA(self):

        #np.random.seed(seed) # replicar random

        # Graficando histograma
        #mu, sigma = 0, 0.2 # media y desvio estandar
        #Input1 = mu
        #Input2 = sigma

        uniforme = stats.uniform()
        x = np.linspace(uniforme.ppf(0.01),
                        uniforme.ppf(0.99), 100)
        fp = uniforme.cdf(x) # Función de Probabilidad




        self.figure = Figure(figsize=(5, 4), dpi=100)
       # x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        self.figure.add_subplot(111).plot(x, fp, '--')
        self.figure.add_subplot(111).vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)



    
        self.canvas_FPA = FigureCanvasTkAgg(self.figure, master=self.master)  # A tk.DrawingArea.
        self.canvas_FPA.draw()
        self.canvas_FPA.get_tk_widget().grid(column=3,row=4)




    def clearGraph(self):
        self.canvas_FDP.get_tk_widget().grid_remove()
        self.canvas_FPA.get_tk_widget().grid_remove()


        
