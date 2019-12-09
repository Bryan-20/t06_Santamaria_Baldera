# ejercicio 2
# Escriba un programa donde el peaton vea el semaforo de color verde, pueda cruzar la calle
# y si esta rojo le permita esperar

import os

# declaracion de variables
peaton,semaforo="",""

# INPUT via OS
nombre=os.sys.argv[1]
semaforo=str(os.sys.argv[2])

# PROCESSING
#Si el semaforo marca Rojo
# mostrar "Esperar!"
# si el semafora muestra Verde
# mostrar "Cruzar la calle!"
if(semaforo=="Rojo"):
    print(nombre,"Esperar")
else:
    print(nombre,"Cruzar la calle!")
#Fin_if
