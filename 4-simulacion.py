from 2_Particula_masa import * as pm
from random import random
from math import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
pausa = 0.02

class Silumacion:
    def __init__(self, Num_particulas, tiempoTot):
        self.Num = Num_particulas
        self.tiempo = tiempoTot
        self.particulas = []
        particulas.append(pm.particulaMasa())
        self.pos()  
        self.vel() 
        self.masa()
        self.delta = 0.1
        self.tiempo =0.0

        for i in range(3,self.Num):
            self.particulas[i].pos =np.array([random(), random(), random()])

        for i in range(3,self.Num):
            self.particulas[i].vel =np.array([1,1,1])

        self.particulas[0].masa = 10000000
        for i in range(1,self.Num):
            self.particulas[i].masa = 1.0e5

    def prepara_grafico(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection='3d')

        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.set_zlim(-2.5,2.5)

        self.grafico = self.ax.scatter([],[],[],c='r',marker='o')
        plt.draw() 

    def refresca_particulas(self):
       
        self.grafico.remove()
        col=['g']
        for _ in range (1,self.Num):
             col.append('r')
        x,y,z = self.vectoriza()    
        self.grafico = self.ax.scatter(x,y,z,c=col,marker='o')
        plt.draw()
        plt.pause(pausa)
        

    def Muestaparticulas(self):
        for i in range(0,self.Num):
            self.particulas[i].muestra()

    def avanza(self):
        for i in range (0,self.Num):
            self.particulas[i].aceleracion_cero()
            for j in range (0, self.Num):
                    if (i!=j):
                        self.particulas[i].aceleracion_gravitatoria(self.particulas[j])
        
        for i in range (0,self.N):
                self.particulas[i].actualiza_velocidad_y_posicion(self.delta)        

     while self.tiempo <= self.TiempoTot: 
            print ("Timepo:", self.tiempo)
            self.Muestaparticulas()
            self.avanza()
            self.tiempo += self.delta

   print "fin"