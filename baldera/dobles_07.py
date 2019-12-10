# Programa 07
# Escriba un programa donde el pescador vea la bandera azul pueda ingresar al mar
# y si esta rojo le diga no ingresar

import os

# declaracion de variables
nombre,bandera="",""

# INPUT via OS
nombre=os.sys.argv[1]
bandera=str(os.sys.argv[2])

# PROCESSING
#Si la bandera esta  Azul
# mostrar "Puede Ingresar al Mar!"
# si la bandera muestra Rojo
# mostrar "No ingresar!"

if(bandera=="Azul"):
    print(nombre,"Puede Ingresar al Mar")
else:
    print(nombre,"No ingresar!")
#Fin_if
