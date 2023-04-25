<<<<<<< HEAD
palabra = input("Agrega cualquier palabra donde quieras eliminar las vocales e imprimir las consonantes y su ubicacion: ")
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] not in "aeiouAEIOU":
        consonantes += palabra[i]
        print(f"Consonante '{palabra[i]}' encontrada en la posición {i}.")

print("Las consonantes restantes son:", consonantes)
=======
palabra = input("Agrega cualquier palabra donde quieras eliminar las vocales e imprimir las consonantes y su ubicacion: ")
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] not in "aeiouAEIOU":
        consonantes += palabra[i]
        print(f"Consonante '{palabra[i]}' encontrada en la posición {i}.")

print("Las consonantes restantes son:", consonantes)
>>>>>>> 24131b26d6ba339f7cd531228e099a3b151032b8
