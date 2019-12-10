# Programa 01
# Escriba un programa que X banco pregunte al cliente su edad y muestre si es mayor o menor de edad
# si es mayor prestamo aprobado, si es menor no accede al prestamo

import os

# declaracion de variables
cliente,mayor_O_menor,edad="","",0

# INPUT via OS
cliente=os.sys.argv[1]
edad=int(os.sys.argv[2])

# PROCESSINGc
#Si el nro mostrado es > 18
# mostrar "Prestamo aprobado!"
# si es < 18 no accede al prestamo

if (edad > 18):
    print (cliente,"Prestamo aprobado!")
else:
    print(cliente,"No accede al prestamo !")
#fin_if
