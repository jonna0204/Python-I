def hacer_grandioso(magos):
    mago = []  #Se crea una lista vacia
    for i in magos: #Se recorre lista "MAGOS"
        i = ("El gran " + i) #A cada iterador se le añade "El Gran"
        mago.append(i) #El iterador se agrega a la lista vacia "mago"
    print(mago) #Se imprime lista mago

def imprimir_nombres(nombres):
    print(nombres) #Se imprimen nombres sin modificar

nombres = ["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]

indice_magos = [0,2,5] #Se selecciona el indice de ubicacion de magos
indice_cientificos = [1,3,6] #Se selecciona el indice de ubicacion de cientificos
indice_otros = [4,7,8] #Se selecciona el indice de otros


magos = [nombres[i] for i in indice_magos] #A la lista magos se agregan los indices de indice_magos
cientificos = [nombres[i] for i in indice_cientificos]#A la lista cientificos se agregan los indices de indice_cientificos
otros = [nombres[i] for i in indice_otros] #A la lista otros se agregan los indices de indice_otros

#Se invoca la funcion imprimir_nombres imprimiendo la lista sin modificar
print("Nombres sin modificar: ")
nombre = imprimir_nombres(nombres)

print("---------------------------------------")

#Se invoca la funcion hacer_grandioso imprimiendo los nombres de magos modificados
print("Listado de magos: ")
mago = hacer_grandioso(magos)

print("---------------------------------------")

#Se imprime la lista de cientificos
print("Listado de cientificos: ")
print(cientificos)

print("---------------------------------------")

#Se imprime lista de otros
print("Listado de otros: ")
print(otros)


