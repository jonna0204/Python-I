#variable global se puede acceder en todo el documento
variable_global = "se puede acceder desde todo el documento"

#variableLocal
#def nombre_metodo(parametros_entrada):
def suma(a,b):
    suma_valores = a+b #variable local porque existe dentro de la funcion
    return suma_valores


print(suma(2,1))
print(variable_global)