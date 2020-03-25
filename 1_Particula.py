from random import random
from math import sqrt
import numpy as np
class particula:
    __cuantas=0
    def __init__(self):
        self.pos = np.array([0.0, 0.0, 0.0 ])
        self.vel= np.zeros(3)
        self.acc=np.zeros(3)
       
        particula.__cuantas += 1
    def set_valores(self, pPos, pVel, pAcc):
        self.pos=pPos
        self.vel=pVel
        self.acc=pAcc
    def init_random(self):
           self.set_valores( np.array([random(), random(), random() ]),
                             np.array([random(), random(), random()]),
                             np.array( [random(), random(), random()])),    
    def muestra(self):
        print("La posición es: ", self.pos)
        print("La velocidad es: ", self.vel)
        print("La acc es: ", self.acc)
    def distancia (self, otra):
        delta=self.pos - otra.pos
        res= sqrt (delta[0]**2 + delta[1]**2 + delta[2]**2 )
        return res
    @classmethod
    def cuantas(cls):
        print("se han definido:", cls.__cuantas)

   