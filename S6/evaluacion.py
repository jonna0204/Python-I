"""
primero = int(input("Ingresa el primero número: "))
segundo = int(input("Ingresa el segundo número: "))
tercero = int(input("Ingresa el tercer número: "))

if primero > segundo and segundo > tercero: 
    print(primero,segundo,tercero)
elif primero > tercero and tercero > segundo: 
    print(primero,tercero,segundo)
if segundo > primero and primero > tercero: 
    print(segundo, primero, tercero)
elif segundo > tercero and tercero > primero: 
    print(segundo, tercero, primero)
if tercero > segundo and segundo > primero: 
    print(tercero,segundo,primero)
elif tercero > primero and primero > segundo: 
    print(tercero,primero,segundo)
    
"""

primero = int(input("Ingresa el primero número: "))
segundo = int(input("Ingresa el segundo número: "))
tercero = int(input("Ingresa el tercer número: "))

seteo = [primero,segundo,tercero]

seteo_1 = set(seteo)

ordenados = sorted(seteo_1,reverse=True)
print(ordenados)
    