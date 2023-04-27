""" La resistencia dentro de un circuito paralelo se calcula como: 
RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))
Donde: 
● RT es la resistencia total. 
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.

Realizar el código en Python para calcular la resistencia total del circuito.
#leer valores ingresados x consola
r1 = float(input("Ingresa el valor de la resistencia 1: "))
r2 = float(input("Ingresa el valor de la resistencia 2: "))
r3 = float(input("Ingresa el valor de la resistencia 3: "))

#calcular resistencia total
rt = 1/((1 /r1)+(1/r2)+(1/r3))

#imprimir la resistencia total
print("La resistancia total es: ",rt)

"""
#validar ingreso de la resistencia, que sea mayor que 0, controlar error
#y utilizar funciones

#funcion para validar ingreso de la resistencia
def validate_input_float(texto):
    while True: #ingreso de valores
        try:  #VALIDA ERRORES
            r = float(input(texto))
            if r > 0:
                return r
            else: print("Ingresa un valor mayor a 0.")
        except Exception as e: #EL ERROR EXCEPTION SE TRANFORMA A e:
            print("Ha ocurrido un error en el ingreso de la resistencia: ",e)
            print("Ingrese un valor valido.")



#invocando funcion
r_1 = validate_input_float("Ingresa la resistencia 1: ")
r_2 = validate_input_float("Ingresa la resistencia 2: ")
r_3 = validate_input_float("Ingresa la resistencia 3: ")

#calcular resistencia total
r_t = 1/((1 /r_1)+(1/r_2)+(1/r_3))

#imprimir la resistencia total
print("La resistancia total es: ",r_t)


#pedir cuantas resistencias se desean ingresar para calcular resistentia total
#llamar al metodo validate input float las veces que sea necesario con un ciclo
#acumular valores de resistencia e imprimir la resistencia total