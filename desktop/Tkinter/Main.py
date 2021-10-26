from tkinter import *

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

def main():

    master = Tk()

    master.title("Tarea 1 Simulación")

    distSelectText = StringVar(master)
    distSelectText.set(OPTIONS[0]) # default value

    distSelect = OptionMenu(master, distSelectText, *OPTIONS)
    distSelect.grid(column=1,row=0)

    
    #Instanciando clases de distribución
    Normal = NormalClass(master)
    Poisson = PoissonClass(master)
    Exponential = ExponentialClass(master)
    NormalST = NormalSTClass(master)
    Bernoulli = BernoulliClass(master)
    Binomial = BinomialClass(master)
    Geometric = GeometricClass(master)
    Uniform = UniformClass(master)
    Pareto = ParetoClass(master)
    Chicuadrado = ChiCuadradoClass(master)
    TStudent = TStudentClass(master)



    def render_dist_options(dist):
        if dist == "Normal":
            Normal.renderWidgets()
            print("Entro en caso de Normal!")
        elif dist == "Poisson":
            Poisson.renderWidgets()
            print("Entro en caso de la Poisson!")
        elif dist == "Exponencial":
            Exponential.renderWidgets()
        elif dist == "Normal Estandar":
            NormalST.renderWidgets()
        elif dist == "Bernoulli":
            Bernoulli.renderWidgets()
            
        elif dist == "Binomial":
            Binomial.renderWidgets()

        elif dist == "Geometrica":
            Geometric.renderWidgets()

        elif dist == "Uniforme Continua":
            Uniform.renderWidgets()

        elif dist == "Pareto":
            Pareto.renderWidgets()

        elif dist == "Chi-Cuadrado":
            Chicuadrado.renderWidgets()

        elif dist == "T-Student":
            TStudent.renderWidgets()

        
        else:
            Normal.removeWidgets()
            Normal.removeVA()
            Normal.clearGraph()

            Poisson.removeWidgets()
            Poisson.clearGraph()
            Poisson.removeVA()

            NormalST.removeWidgets()
            NormalST.removeVA()
            NormalST.removeGraph()

            Bernoulli.removeWidgets()
            Bernoulli.removeVA()
            Bernoulli.removeGraph()

            Binomial.removeWidgets()
            Binomial.removeVA()
            Binomial.removeGraph()

            Geometric.removeWidgets()
            Geometric.removeVA()
            Geometric.removeGraph()

            Uniform.removeWidgets()
            Uniform.removeVA()
            Uniform.removeGraph()

            Pareto.removeWidgets()
            Pareto.removeVA()
            Pareto.removeGraph()

            Chicuadrado.removeWidgets()
            Chicuadrado.removeVA()
            Chicuadrado.removeGraph()

            TStudent.removeWidgets()
            TStudent.removeVA()
            TStudent.removeGraph()


            print("Deberia remover el grafico de la normal!")
            print("Deberia remover los widgets del UI!")

    selectDistBtn = Button(master,text="SELECT", command=lambda:render_dist_options(distSelectText.get()))
    selectDistBtn.grid(column=2,row=0)


    def random_va(dist):
        if dist == "Normal":
            Normal.renderVA()
            print("Entro en caso de Normal VA")
        elif dist == "Poisson":
            Poisson.renderVA()
            print("Entro en caso de Poisson VA")
        elif dist == "Exponencial":
            Exponential.renderVA()
            print("Entro en caso de Exponential VA")
        elif dist == "Normal Estandar":
            NormalST.renderVA()

        elif dist == "Bernoulli":
            Bernoulli.renderVA()

        elif dist == "Binomial":
            Binomial.renderVA()

        elif dist == "Geometrica":
            Geometric.renderVA()
        
        elif dist == "Uniforme Continua":
            Uniform.renderVA()
        
        elif dist == "Pareto":
            Pareto.renderVA()

        elif dist == "Chi-Cuadrado":
            Chicuadrado.renderVA()

        elif dist == "T-Student":
            TStudent.renderVA()
        

        else:
            Normal.removeVA()
            print("Entro en el caso de remover la VA Exponential")

    vaBtn = Button(master,text="Random V.A.", command=lambda:random_va(distSelectText.get()))
    vaBtn.grid(column=2,row=6)


    def render_dist_graph(dist):
        if dist == "Normal":
            Normal.renderGraph()
            print("Se va a graficar la normal!")
        elif dist == "Exponencial":
            Exponential.renderGraph()

        elif dist == "Poisson":
            Poisson.renderGraph()

        elif dist == "Normal Estandar":
            NormalST.renderGraph()

        elif dist == "Bernoulli":
            Bernoulli.renderGraph()

        elif dist == "Binomial":
            Binomial.renderGraph()

        elif dist == "Geometrica":
            Geometric.renderGraph()
        
        elif dist == "Uniforme Continua":
            Uniform.renderGraph()
        
        elif dist == "Pareto":
            Pareto.renderGraph()

        elif dist == "Chi-Cuadrado":
            Chicuadrado.renderGraph()

        elif dist == "T-Student":
            TStudent.renderGraph()
        


        else:
            Poisson.clearGraph()
            Exponential.clearGraph()
            Normal.clearGraph()
            Bernoulli.clearGraph()
            print("Deberia remover el grafico de la normal!")

    selectDistBtn = Button(master,text="CALCULAR", command=lambda:render_dist_graph(distSelectText.get()))
    selectDistBtn.grid(column=1,row=6)

    
    








main()






mainloop()