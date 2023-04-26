palabra = input("Agrega cualquier palabra donde quieras eliminar las vocales e imprimir las consonantes y su ubicacion: ")
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] not in "aeiouAEIOU":
        consonantes += palabra[i]
        print(f"Consonante '{palabra[i]}' encontrada en la posición {i}.")

print("Las consonantes restantes son:", consonantes)
