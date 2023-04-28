mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
listaNueva = [] #se crea lista nueva para eliminar duplicados

for i in mi_lista: #se recorre mi_lista
    if i not in listaNueva: #si iterador no se encuentra en listaNueva 
        listaNueva.append(i) #lo agrega a listaNueva
print(listaNueva)

listaNueva.sort() #ordenar ascendentemente la lista
print(listaNueva)