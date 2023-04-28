import time
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]


#Si el primer número de la sublista es cero, omitir la impresión de toda la sublista
for i in lista:
    if i[0] == 0: 
        continue
    print(i)
    time.sleep(0.5)
print("------------------")


# Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
for index in lista: 
    for j in index: 
        if j == 0: 
            index.remove(0) 
    print(index)
    time.sleep(0.5)
print("------------------")


#Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la 
#segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.

dic = ['A','B','C','D'] #Se crea una lista con las claves en donde se asignaran las sublistas.
diccionario = dict(zip(dic,lista)) #Se asignan las claves con los valores

# Finalmente, imprimiremos en pantalla el diccionario resultante
print(diccionario)
print("------------------")
time.sleep(0.5)

