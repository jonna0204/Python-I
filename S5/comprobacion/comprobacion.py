#import math

#n = 4

#factorial = math.factorial(n)
#print(f"El factorial de {n} es {factorial}")




numero = int(input("Ingresa un número entero para calcular el factorial: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}")

    
    
