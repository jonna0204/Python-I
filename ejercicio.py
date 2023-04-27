"""Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.
Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:
"Puedes conducir"
"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
"No puedes conducir. Necesitas contar con una licencia"

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
        print("Puedes conducir")
elif edad < 16:
        print("Eres menor de edad, Debes cumplir 18 años y contar con una licencia de conducir")
else:
    print("No puedes conducir aun. Te queda poco para cumplir 18 años y sacar una licencia de conducir.")
"""

"""Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
"Cumples con los requisitos para postularte"
"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
"Para postularte, necesitas tener conocimientos de inglés"
"Para postularte, necesitas saber programar en Python"
Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.
"""

# Definir las variables booleanas para saber si el candidato cumple con los requisitos
sabe_python = bool(input("Sabes programar python? True or False: "))  # True si el candidato sabe programar en Python
sabe_ingles = bool(input("Sabes ingles? True or False: "))  # True si el candidato tiene conocimientos de inglés

# Evaluar las condiciones y mostrar el mensaje correspondiente en pantalla
if sabe_python and sabe_ingles:
    print("Cumples con los requisitos para postularte")
elif sabe_ingles:
    print("Para postularte, necesitas saber programar en Python")
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

    

