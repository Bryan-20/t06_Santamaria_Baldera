# Programa 10
# Escriba un programa donde el usuario vea el sistema infocor si esta en deuda o no
# si esta en rojo mostrar "Deuda pendiente"

import os

# declaracion de variables
usuario,semaforo="",""

# INPUT via OS
usuario=os.sys.argv[1]
sistema=str(os.sys.argv[2])

# PROCESSING
#Si el sistema marca Rojo
# mostrar "Deuda pendiente!"

if(sistema=="Rojo"):
    print(usuario,"Deuda pendiente!")

#Fin_if
