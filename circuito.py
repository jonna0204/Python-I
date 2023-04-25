import time

"""
    La resistencia dentro de un circuito paralelo se calcula como: 
RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))
Donde: 
● RT es la resistencia total. 
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.
 
Realizar el código en Python para calcular la resistencia total del circuito.


r1 = float(input("Ingresa el valor de la resistencia 1: "))
r2 = float(input("Ingresa el valor de la resistencia 2: "))
r3 = float(input("Ingresa el valor de la resistencia 3: "))

rt = 1/((1 /r1)+(1/r2)+(1/r3))


print("La resistancia total es: {:.3f}".format(rT))




hipotenusa = (a**2 + b**2)**(1/2) 


catetoa = float(input("Ingresa el valor del primer cateto: "))
catetob = float(input("Ingresa el valor del cateto b: "))

cateto_a = catetoa**catetoa
cateto_b = catetob**catetob

cateto = cateto_a + cateto_b

cat = cateto ** (1/2)
print(cat)

"""
"""
Pedir el ingreso de dos textos al usuario por consola 
y comparar si son iguales o del mismo tamaño


ingreso1 = input("Ingresa cualquier texto: ")
ingreso2 = input("Ingresa otro texto: ")


if len(ingreso1) == len(ingreso2):
    if ingreso1 == ingreso2:
        print("Los textos son iguales.")    
    else:
        print("Los textos no son iguales.")




    
Simulación de una bomba de tiempo.
Irá el tiempo desde el 5 al 1 en decremento.
Al ejecutar el programa, se imprimirá el mensaje "Booom"


i = int(input("Ingresa algun valor: "))
while i >= 1:
    i -=1
    time.sleep(1)
    if i == 0:
        break
    print(i)
print("KBOOOOOOOOOOOOOOOOOOOOM!")

"""
import re #se importa libreria de patrones
patron = re.compile("(?<!\\S)\\d(?!\\S)")

print("Bienvenido: ")
print("Seleccione una de las siguientes opciones: \n1.-Ver Saldo\n1.-Depositar\n3.-Girar\n4.-Salir")

opcion = ""

while opcion != "5":
    opcion = input("Selecciona una opcion: ")
    if re.match(patron,opcion):
        if opcion == "1":
            print("Se realiza la opcion 1.")
        elif opcion == "2":
            print("Se realiza la opcion 2.")
        elif opcion == "3":
            print("Se realiza la opcion 3.")
        elif opcion == "4":
            print("Saliendo.")
            break
        else: 
            print("Ha ingresado una opcion incorrecta, porfavor vuelva a ingresar.")
            
    