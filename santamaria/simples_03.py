# Programa 01
# Escriba un programa que pregunte al usuario su compra y muestre si es mayor o menor a 100.
import os
# declaracion de variables
cliente,mayor_O_menor,compra="","",0

# INPUT via OS
cliente=os.sys.argv[1]
compra=float(os.sys.argv[2])

# PROCESSINGc
#Si el nro mostrado es < 1000
# mostrar "Pago con tarjeta debito!"
#Si el nro mostrado es > 1000
# mostrar "Pago en efectivo!"

if (compra > 1000):
    print (cliente,"Pago con tarjeta debito!")
else:
    print(cliente,"Pago en efectivo!")

#Fin_if
