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




