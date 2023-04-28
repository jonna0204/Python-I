import time

lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
for i in lista:
    if i[0] == 0: #SI EL PRIMER NUMERO DE LA LISTA ES 0 SE CONTINUA A LA SIGUIENTE.
        continue
    print(i)
    time.sleep(0.5)

for i in lista:      
    for j in i:
        if j == 0:#se quita el 0 de los valores
            continue
        print(j)#se imprimen los valores de la sublista
        time.sleep(0.5)