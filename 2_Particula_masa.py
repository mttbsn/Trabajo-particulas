import numpy as np
from 1_Particula import *
G=6.67259**-11

class particulaMasa(particula):
    def __init__(self):
        super().__init__(self)
        self.masa=0.0

    def set_valores (self, pos, vel, acc, pmasa):
        super().__init__(pos, vel, acc)
        self.masa=pmasa

    def init__random(self):
        self.set_valores( np.array([random(), random(), random() ]), 
                            np.array([random(), random(), random()]),
                            np.array( [random(), random(), random()]),
                            random())            
    def muestra(self):
        super().muestra()
        print("La distancia es: ", self.masa)

    def aceleracion_cero(self):
        self.acc=np.zeros(3)

    def aceleracion_gravitatoria(self, otra):
        softening =1e-6
        distancia=self.distancia(otra)
        if distancia < softening:
            distancia=softening
        distanciaInv = 1.0/ distancia
        delta=otra.pos -self.pos
        self.acc += delta *G*otra.mas * distanciaInv **3

      def actualiza_velocidad_y_posicion (self, delta):
        self.vel += self.acc * delta
        self.pos += self.vel * delta

