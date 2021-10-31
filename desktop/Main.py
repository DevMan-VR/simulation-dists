from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk

from numpy import ubyte
from NormalClass import NormalClass
from PoissonClass import PoissonClass
from ExponentialClass import ExponentialClass
from NormalSTClass import NormalSTClass
from BernoulliClass import BernoulliClass
from BinomialClass import BinomialClass
from GeometricClass import GeometricClass
from UniformClass import UniformClass
from ParetoClass import ParetoClass
from ChiCuadradoClass import ChiCuadradoClass
from TStudentClass import TStudentClass
from ErlangClass import ErlangClass
from TriangularClass import TriangularClass
from WeibullClass import WeibullClass


OPTIONS = [
"Uniforme Continua",
"Bernoulli",
"Exponencial",
"Normal",
"Normal Estandar",
"Binomial",
"Poisson",
"Geometrica",
"Erlang",
"Triangular",
"Weibull",
"Pareto",
"T-Student",
"Chi-Cuadrado"


] #etc


class MainClass:

    def __init__(self):
        self.master = Tk()
        self.master.geometry("1280x800")
        self.master.title("Tarea 1 Simulación")

        self.distSelectText = StringVar(self.master)
        self.distSelectText.set(OPTIONS[0]) # default value
        self.distSelect = OptionMenu(self.master, self.distSelectText, *OPTIONS)
        self.distSelect.grid(column=1,row=0)

        #Instanciando clases de distribución
        self.Normal = NormalClass(self.master)
        self.Poisson = PoissonClass(self.master)
        self.Exponential = ExponentialClass(self.master)
        self.NormalST = NormalSTClass(self.master)
        self.Bernoulli = BernoulliClass(self.master)
        self.Binomial = BinomialClass(self.master)
        self.Geometric = GeometricClass(self.master)
        self.Uniform = UniformClass(self.master)
        self.Pareto = ParetoClass(self.master)
        self.Chicuadrado = ChiCuadradoClass(self.master)
        self.TStudent = TStudentClass(self.master)
        self.Erlang = ErlangClass(self.master)
        self.Triangular = TriangularClass(self.master)
        self.Weibull = WeibullClass(self.master)

        self.currentDistribution = None

        self.selectDistBtn =  Button(self.master,text="SELECT", command=lambda:self.render_dist_options(self.distSelectText.get()))
        self.selectDistBtn.grid(column=2,row=0)

        self.vaBtn = Button(self.master,text="Random V.A.", command=lambda:self.random_va(self.distSelectText.get()))
        self.vaBtn.grid(column=2,row=6)

        self.selectDistBtn = Button(self.master,text="CALCULAR", command=lambda:self.render_dist_graph(self.distSelectText.get()))
        self.selectDistBtn.grid(column=1,row=6)

        mainloop()
        


        


    def render_dist_options(self,dist):

            #Si ya hay definido un current distribution entonces se le remueven sus componentes (clean up)
            if self.currentDistribution != None and self.currentDistribution.name != dist:
                print("Now we are cleaning")
                print(self.currentDistribution)
                self.currentDistribution.removeWidgets()
                self.currentDistribution.removeVA()
                self.currentDistribution.clearGraph()
                self.currentDistribution = None

                


            if dist == "Normal":
                self.Normal.renderWidgets()
                self.currentDistribution = self.Normal
                print("Entro en caso de Normal!")

            elif dist == "Poisson":
                self.Poisson.renderWidgets()
                self.currentDistribution = self.Poisson
                print("Entro en caso de la Poisson!")

            elif dist == "Exponencial":
                self.Exponential.renderWidgets()
                self.currentDistribution = self.Exponential
                print("Entro en caso de la Exponencial!")

            elif dist == "Normal Estandar":
                self.NormalST.renderWidgets()
                self.currentDistribution = self.NormalST
                print("Entro en caso de la Normal Estandar!")

            elif dist == "Bernoulli":
                self.Bernoulli.renderWidgets()
                self.currentDistribution = self.Bernoulli
                print("Entro en caso de la Bernoulli!")
                
            elif dist == "Binomial":
                self.Binomial.renderWidgets()
                self.currentDistribution = self.Binomial
                print("Entro en caso de la Binomial!")

            elif dist == "Geometrica":
                self.Geometric.renderWidgets()
                self.currentDistribution = self.Geometric
                print("Entro en caso de la Geometrica!")

            elif dist == "Uniforme Continua":
                self.Uniform.renderWidgets()
                self.currentDistribution = self.Uniform
                print("Entro en caso de la Uniforme!")

            elif dist == "Pareto":
                self.Pareto.renderWidgets()
                self.currentDistribution = self.Pareto
                print("Entro en caso de la Pareto!")

            elif dist == "Chi-Cuadrado":
                self.Chicuadrado.renderWidgets()
                self.currentDistribution = self.Chicuadrado
                print("Entro en caso de la Chi-Cuadrado!")

            elif dist == "T-Student":
                self.TStudent.renderWidgets()
                self.currentDistribution = self.TStudent
                print("Entro en caso de la T-Student!")

            elif dist == "Erlang":
                self.Erlang.renderWidgets()
                self.currentDistribution = self.Erlang
                print("Entro en caso de la Erlang!")

            elif dist == "Triangular":
                self.Triangular.renderWidgets()
                self.currentDistribution = self.Triangular
                print("Entro en caso de la Triangular!")

            elif dist == "Weibull":
                self.Weibull.renderWidgets()
                self.currentDistribution = self.Weibull
                print("Entro en caso de la Weibull!")
            

    def random_va(self,dist):
        if dist == "Normal":
            self.Normal.renderVA()
            print("Entro en caso de Normal VA")
        elif dist == "Poisson":
            self.Poisson.renderVA()
            print("Entro en caso de Poisson VA")
        elif dist == "Exponencial":
            self.Exponential.renderVA()
            
            print("Entro en caso de Exponential VA")
        elif dist == "Normal Estandar":
            self.NormalST.renderVA()

        elif dist == "Bernoulli":
            self.Bernoulli.renderVA()

        elif dist == "Binomial":
            self.Binomial.renderVA()

        elif dist == "Geometrica":
            self.Geometric.renderVA()
        
        elif dist == "Uniforme Continua":
            self.Uniform.renderVA()
        
        elif dist == "Pareto":
            self.Pareto.renderVA()

        elif dist == "Chi-Cuadrado":
            self.Chicuadrado.renderVA()

        elif dist == "T-Student":
            self.TStudent.renderVA()

        elif dist == "Erlang":
            self.Erlang.renderVA()

        elif dist == "Triangular":
            self.Triangular.renderVA()

        elif dist == "Weibull":
            self.Weibull.renderVA()
        

        


    def render_dist_graph(self,dist):
        if dist == "Normal":
            self.Normal.renderGraph()
            print("Se va a graficar la normal!")
        elif dist == "Exponencial":
            self.Exponential.renderGraph()

        elif dist == "Poisson":
            self.Poisson.renderGraph()

        elif dist == "Normal Estandar":
            self.NormalST.renderGraph()

        elif dist == "Bernoulli":
            self.Bernoulli.renderGraph()

        elif dist == "Binomial":
            self.Binomial.renderGraph()

        elif dist == "Geometrica":
            self.Geometric.renderGraph()
        
        elif dist == "Uniforme Continua":
            self.Uniform.renderGraph()
        
        elif dist == "Pareto":
            self.Pareto.renderGraph()

        elif dist == "Chi-Cuadrado":
            self.Chicuadrado.renderGraph()

        elif dist == "T-Student":
            self.TStudent.renderGraph()

        elif dist == "Erlang":
            self.Erlang.renderGraph()

        elif dist == "Triangular":
            self.Triangular.renderGraph()

        elif dist == "Weibull":
            self.Weibull.renderGraph()
        

       

    



#Init Program

main = MainClass()






    