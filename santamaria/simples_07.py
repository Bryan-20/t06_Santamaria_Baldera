# Programa 07
# Escriba un programa donde el pescador vea la bandera azul pueda ingresar al mar


import os

# declaracion de variables
nombre,bandera="",""

# INPUT via OS
nombre=os.sys.argv[1]
bandera=str(os.sys.argv[2])

# PROCESSING
#Si la bandera esta  Azul
# mostrar "Puede Ingresar al Mar!"

if(bandera=="Azul"):
    print(nombre,"Puede Ingresar al Mar")

#Fin_if
