

#numero = int(input("Ingrese un numero entero: "))

print("Ingresa un numero entero:")
numero = input()
numero = int(numero) #se convierte string a int


#if(condicion), donde condicion siempre es True
#a menos que cambie la condicion

if(numero > 0):
    print(f"El numero {numero} es mayor a 0")
elif(numero == 0):
    print(f"El numero {numero} es igual a 0")
else:
    print(f"El numero {numero} es menor a 0")
    
    