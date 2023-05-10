#Se crea la funcion que suma y luego resta numeros
def suma_resta(numeros):
    total_sum = numeros[0] + numeros[1] + numeros[2]
    resta = numeros[0] - numeros[1] - numeros[2] 
    return (total_sum, resta)


params = [4, 2, 10] #Valores para la funcion
total_sum, resta = suma_resta(params) #se agrega los valores a la funcion
tupla = (total_sum, resta) #se agrega los resultados de la funcion a una tupla
print(tupla)