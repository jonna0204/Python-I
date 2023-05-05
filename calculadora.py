"""
Se pide realizar una calculadora declarando funciones para cada tipo de calculo
que se realize.
Realizar un menu con opciones para seleccionar
Ingreso x consola
verificar errores de ingreso
verificar division x cero
"""
#funciones deben ser definidas antes de invocarlas
#def nombre_funcionn(parametro1,parametro2):

def suma(num1,num2):
    sumatoria = num1 + num2
    return sumatoria

def resta(num1: float,num2:float): #Solo datos tipos float
    return num1 - num2

def multiplicar(num1,num2)  -> float: #transforma el resultado en dato tipo float
    return num1 * num2

def dividir(num1,num2):
    if num2 == 0:
        return None
    else: 
        return num1 / num2


def opciones_a_mostrar():
        print("Bienvenido a la Calculadora.")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("5.- Salir")
        print("Ingrese una opcion: ")
    
#funcion calculadora llevara el menu y realizara calculos usando funciones
#y estructuras condicionales

def calculadora():
    while True:#mientras sea true o no exista un break o return se seguira ejecutando en ciclo
        try:
    #requerir y mostrar opciones al usuario
            opciones_a_mostrar() #invocamos a la funcion para mostrar opciones al usuario
    
        #ingresar valores de opcion y numeros que se realizara el calculo
            opcion = input("1/2/3/4/5:      ")
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
    
        #evaluar opcion y seleccionar una funcion a realizar si se cumple la funcion
            match opcion:
                case "1":
                    resultado = suma(num1,num2)#invocando funcion suma que necesita 2 valores
                case "2":
                    resultado = resta(num1,num2)
                case "3":
                    resultado = multiplicar(num1,num2)
                case "4":
                    resultado = dividir(num1,num2)
                case "5":
                    #return si es funcion
                    #funcion si es ciclo
                    print("Gracias por usar la calculadora.")
                case _:
                    #resultado = None
                    print("Opcion no valida, elija una valida.")
            if resultado is not None:
                print(f"El resultado del calculo entre {num1} y {num2}es : {resultado}")
            
        except Exception as e:
            print("Error: ",e)

calculadora()