#se crean funciones de suma, resta, multiplicacion y division.

def sum(parametros):
    total_sum = parametros[0] + parametros[1]  
    return (total_sum)

def rest(parametros):
    total_rest = parametros[0] - parametros[1]  
    return (total_rest)

def mult(parametros):
    total_mult = parametros[0] * parametros[1]  
    return (total_mult)

def div(parametros):
    total_div = parametros[0] / parametros[1]  
    return (total_div)

parametros = (10,2) #Estos valores se le agregan a las funciones.
tupla = [] #Se crea una tupla vacia

result_suma = sum(parametros) #El resultado de la funcion se le asigna a una variable
result_rest = rest(parametros) #El resultado de la funcion se le asigna a una variable
result_mult = mult(parametros) #El resultado de la funcion se le asigna a una variable
result_div = div(parametros) #El resultado de la funcion se le asigna a una variable

#Los resultados de las funciones se agregan a la tupla vacia
tupla = [result_suma,result_rest,result_mult,result_div]

#print(tupla)

#Se crea una diccionario con los valores almacenados en la tupla
dicc = {
    "Suma": tupla[0],
    "Resta": tupla[1],
    "Multiplicacion": tupla[2],
    "Division": tupla[3],
}

print(dicc)

