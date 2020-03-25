from 2_Particula_masa import *

p1= Particula_masa()
p2= Particula_masa()

delta = 0.1
p1.init__random()
p2.init__random()

p1.muestra()
p2.muestra()

p1.aceleracion_gravitatoria(p2)
p2.aceleracion_gravitatoria(p1)

p1.actualiza_vel_y_pos(delta)
p2.actualiza_vel_y_pos(delta)

p1.muestra()
p2.muestra()

