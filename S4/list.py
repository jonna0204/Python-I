#listas en python
#estructura para almacenar datos con un orden especifico de inseccion

lista = [1,2,3,4]
listas_difentes_valores = [1,"2",3,"4",1.5,True,False,lista]

print(listas_difentes_valores)  

#para acceder a un elemto del arreglo se utilizan los indices
#0 a n-1, pero tambien pueden ser negativos
print(lista[0])
print(listas_difentes_valores[7])
print(listas_difentes_valores[7][1])

#algunos metodos de la lista
#agregar, anexar valor
lista.append(5)
print(lista)

#remove
lista.remove(2)
print(lista)
lista.remove(1)
print(lista)

#pop elimina por indice
lista.pop(1)
print(lista)

#inserccion por indice
lista.insert(1,2)
print(lista)

#indice por elemento
indice = lista.index(2)
print(indice)

#ordenar elementos dentro de la lista
lista.sort()