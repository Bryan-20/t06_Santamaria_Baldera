#programa 05
# Escriba un programa que pregunte al comprador si gano en una rifa un iphone7s
# si el numero de tickes comprados supera los 50

import os

# declaracion de variables
nombre,nro_de_ticks="",0

#input via os
nombre=os.sys.argv[1]
nro_ticks=int(os.sys.argv[2])

#processing

#si el numero de ticks supera 50
#mostrar ganaste un Iphone7s!
if (nro_ticks>50):
    print(nombre,"ganaste un Iphone7s! ")
else:
    print(nombre,",ganaste un premio sopresa!")
#finif
