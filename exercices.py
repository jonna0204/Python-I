####################################################
"Crea una lista de numero donde cada numero"
"es la longitud de una palabra"


lista = ["gato","perro","elefante","jirafa","tigre"]
longitudes = []
for i in range(len(lista)):#recorre el largo de la lista
    longitudes.append(len(lista[i]))
    print(longitudes)


#segun la cantidad de caracteres se imprime el nombre
for j in lista:
    if len(j) >= 5:
        continue
    else:print(j)

print("---------------------------------------------")

#####################################################

"imprimir los nombres que tienen una longitud mayor a n caracteres"


nombre = ["juan","maria","pedro","ana","roberto","lucia","luisa"]


for largo in nombre:
    if len(largo) > 4:
        continue
    print(largo)
print("---------------------------------------------")
#######################################################
"solicita al usuario ingresar una contraseña"
"hasta que la contraseña coincida"

contraseña = "password"

intentos = 0

while intentos < 4:
    inicio = input("Ingresa una contraseña (son 4 intentos): ")
    if inicio == contraseña:
        print("Contraseña correcta.")
    elif inicio != contraseña:
        intentos += 1
        print("Contraseña incorrecta.")
else:
        print("Intentos acabados.")