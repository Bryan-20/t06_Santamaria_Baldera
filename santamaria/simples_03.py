# Programa 03
# Escriba un programa que pregunte al cliente su compra y muestre si es mayor o menor a 1000.
import os
# declaracion de variables
cliente,mayor_O_menor,compra="","",0

# INPUT via OS
cliente=os.sys.argv[1]
compra=float(os.sys.argv[2])

# PROCESSINGc
#Si el nro mostrado es < 1000
# mostrar "Pago con tarjeta debito!"


if (compra > 1000):
    print (cliente,"Pago con tarjeta debito!")

#Fin_if
