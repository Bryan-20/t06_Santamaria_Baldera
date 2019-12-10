# programa numero 04
#Se desea escribir un algoritmo que solicite la altura de una persona expresada en cm,
#si la altura es mayor a 160 cm escriba el mensaje “Persona de estatura promedio

import os
# declaracion de variables
nombre,AltaObaja,alt_en_cm="","",0

# INPUT via OS
nombre=os.sys.argv[1]
alt_en_cm=int(os.sys.argv[2])

# PROCESSING
#Si el nro mostrado es > 160
# mostrar "Persona estatura promedio!"
if (alt_en_cm > 160):
    print(nombre,"Persona de estatura promedio!")

#fin_if


