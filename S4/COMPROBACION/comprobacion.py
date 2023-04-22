a = 8 #variable con numero 8
b = 10.5 # variable con numero 10.5
c = "ejercicio" #variable con palabra "ejercicio"

new_set = set({a,b,c}) #se crea un set con las variables, y este se asigna a una variable 
print(new_set)


lista = [new_set] #se crea una lista con el set creado anteriormente
falso = False #variable con valor logico false
lista.append(falso) #se agrega variable con valor False
print(lista)

lista_asignada = lista #se agrega la lista a una nueva variable

print(lista_asignada) #se imprime en pantalla la variable creada