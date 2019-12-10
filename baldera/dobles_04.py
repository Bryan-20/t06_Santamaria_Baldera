# programa numero 04
#Se desea escribir un algoritmo que solicite la altura de una persona expresada en cm,
# si la altura es menor a 150 cm muestre el mensaje “Persona de altura baja”
# y si la altura es mayor a 171 cm escriba el mensaje “Persona alta”

import os
# declaracion de variables
nombre,AltaObaja,alt_en_cm="","",0

# INPUT via OS
nombre=os.sys.argv[1]
alt_en_cm=int(os.sys.argv[2])

# PROCESSINGc
#Si el nro mostrado es < 150
# mostrar "Persona baja!"
#Si el nro mostrado es > 150
# mostrar "Persona Alta!"
if (alt_en_cm <  150):
    print(nombre,"Persona baja!")
else:
    print(nombre,"Persona Alta!")
#fin_if
