#ordenados por clave y valor
#los diccionarios son una coleccion de elementos
#declaracion con llaves {} o con la funcion dict()

estudiantes = {
    #clave:valor
    "Fulanito":25,
    "Maria":22,
    "Jose":48,
    "Marta":34
}

print(estudiantes)#{'Fulanito': 25, 'Maria': 22, 'Jose': 48, 'Marta': 34}

#acceder al valor de una clave
#nombre_diccionario["clave"]
print(estudiantes["Maria"])#22

#remover clave de un diccionario
del estudiantes["Fulanito"]
print(estudiantes)#{'Maria': 22, 'Jose': 48, 'Marta': 34}

#imprimir solo las claves
claves = estudiantes.keys()
print(claves)

#borrar un diccionario
#estudiantes.clear()
#print(estudiantes)

#obtener solo los valores
valores = estudiantes.values()
print(valores)
