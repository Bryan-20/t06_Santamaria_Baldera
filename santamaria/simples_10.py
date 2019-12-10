# Programa 10
# Escriba un programa donde el usuario vea el sistema infocor si esta en deuda o no
# si esta azul mostrar " no esta en deuda" si esta en rojo mostrar "Deuda pendiente"

import os

# declaracion de variables
usuario,semaforo="",""

# INPUT via OS
usuario=os.sys.argv[1]
sistema=str(os.sys.argv[2])

# PROCESSING
#Si el sistema marca Rojo
# mostrar "Deuda pendiente!"
# si el sistema muestra Azul
# mostrar "No esta en deuda!"
if(sistema=="Rojo"):
    print(usuario,"Deuda pendiente!")
else:
    print(usuario,"No esta en deuda!")
#Fin_if
