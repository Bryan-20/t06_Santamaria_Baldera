# Programa 01
# Escriba un programa que pregunte al usuario su edad y muestre si es mayor o menor de edad.
import os

# declaracion de variables
usuario,mayor_O_menor,edad="","",0

# INPUT via OS
usuario=os.sys.argv[1]
edad=int(os.sys.argv[2])

# PROCESSINGc
#Si el nro mostrado es > 18
# mostrar "Eres mayor de edad!"
if (edad > 18):
    print (usuario,"Eres mayor de edad!")
else:
    print(usuario,"Eres menor de edad!")
#fin_if





# programa  02
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
