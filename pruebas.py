"""
x = (10,20,30,40,50)
for var in x:
    print("indice "+ str(x.index(var)) + ":",var)
"""
    
y = [(1,2), (3,4), (5,6)]
for a, b in y:
    print(a, "plus", b, "equals", a+b)
    
"""
print("Ciencia")
for caracter in "Ciencia ":
    print(caracter)
    
    
digitos = [0, 1, 5]
for i in digitos:
    print(i)
else:
    print("No quedan elementos en la lista.")


a = 5
b = 10
iteraciones = 5
cuenta = 0
while cuenta < a or cuenta < b and not cuenta >= iteraciones:
    print(f"Cuenta: { cuenta }, a: {a}, b: {b}")
    cuenta += 1
    
#La razón por la cual hemos creado un ciclo infinito es porque nunca cambiamos el valor de i, 
#siempre será cero y por tanto siempre será inferior a 10.
#i = 0
#while i <= 10: 
#    print("He creado un ciclo infinito")
    
#La programación correcta es: 
i = 0
while i <= 10:
    print("He creado un ciclo infinito")
    i += 1

for i in range(5):
    for j in range(i):
    print('*', end=””)
    print(“”)

i=1
while(i<=5):
    j=5
    while(j>=i):
    print(j, end=' ')
    j-=1
    i+=1
    print()
    
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
    print('fizzbuzz')
    elif i % 3 == 0:
    print('fizz')
    elif i % 5 == 0:
    print('buzz')
    else:
    print('-')


estudiantes = ["Paul", "Luis", "Carmen", "Alicia"]
for estudiante in range(0, len(estudiantes)):
    if estudiante == 2:
    continue
    else:
    print(estudiantes [estudiante])
    print("Contador es " + str(estudiante))
"""