# Programa 02
# Escriba un programa donde el peaton vea el semaforo de color rojo le permita esperar.

import os

# declaracion de variables
peaton,semaforo="",""

# INPUT via OS
nombre=os.sys.argv[1]
semaforo=str(os.sys.argv[2])

# PROCESSING
#Si el semaforo marca Rojo
# mostrar "Esperar!"
if(semaforo=="Rojo"):
    print(nombre,"Esperar")

#Fin_if
