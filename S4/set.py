#Set = coleccion de elementos y son unicos
nombre_set = set({1,2,3,4,5,6,7,8,9,0})
set1 = {1,1,2,3}

print(nombre_set)
print(set1)

#metodos de set

#Añadir
set1.add(4)
print(set1)

#remover
set1.remove(1)
print(set1)


#convertir una lista en un  set

lista = [1,1,1,1,2,3,4]
print(lista)

lista = set(lista)
print(lista)

