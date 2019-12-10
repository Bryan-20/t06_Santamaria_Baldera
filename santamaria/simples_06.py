#programa 06
# Escriba un programa que pregunte al Alumno si aprobo el examen de lepII
# si la nota aprobatoria es de 11

import os

# declaracion de variables
Alumno,nta_aprobatoria="",0

#input via os
nombre=os.sys.argv[1]
nta_aprobatoria=int(os.sys.argv[2])

#processing

#si la nota aprobatoria supera el 11
#mostrar Aprobo el examen!
if (nta_aprobatoria>11):
    print(nombre,"Aprobo el examen! ")

#finif
