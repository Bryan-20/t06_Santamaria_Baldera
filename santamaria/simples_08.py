# Programa 08
# Escriba un programa que pregunte al postulante si ingreso a la UNPRG, si su puntaje es mayor 70
import os

# declaracion de variables
postulante,ingreso_O_noingreso,puntaje="","",0

# INPUT via OS
postulante=os.sys.argv[1]
puntaje=float(os.sys.argv[2])

# PROCESSINGc
#Si el nro mostrado es < 70
# mostrar "Alcanso bacante!"

if (puntaje > 70):
    print (postulante,"Alcanso bacante!")


#Fin_if
