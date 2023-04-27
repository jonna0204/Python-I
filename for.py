##ciclo for
#se utiliza para recorrido de datos

lista = [1,2,3,4,5,6]

#recorriendo largo de la lista
for i in lista:
    print(i) 

#recorriendo el indice de la lista
#for item in range(len(lista)):
#    print(f"El valor esta en el indice {item}")#indice de la lista



#recorriendo indice de la lsita
for item in lista:
    print("Recorriendo el indice de la lista: ",lista.index(item))


#RECORRER DICCIONARIO


diccionario = {"a":1,"b":2,"c":3}

#obteniendo valor de una key
for index in diccionario:
    print("obteniendo el valor de la clave ",index)

#obteniendo el valor de una clave
for index in diccionario:
    print("Obteniendo el valor de la clave",diccionario,[index])

#obteniendo solo los valores
for index in diccionario.values():
    print("Obteniendo el valor", index)

#obteniendo solos keys o claves
for index in diccionario.items():
    print("Obteniendo el elemento con cbale:valor", index)
