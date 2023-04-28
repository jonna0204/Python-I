import time
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
for i in lista:
    if i[0] == 0: #SI EL PRIMER NUMERO DE LA LISTA ES 0 SE CONTINUA A LA SIGUIENTE.
        continue
    print(i)
    time.sleep(0.5)

for index in lista: #se recorre nuevamente la lista
    for j in index: #se recorre el index
        if j == 0: #si dentro del index hay un numero 0
            index.remove(0) #se elimina el numero
    print(index)
    time.sleep(0.5)
