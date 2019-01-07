import random
import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#conexion_diccionario = open('palabras.json', 'r')
#load_diccionario = json.load(conexion_diccionario)
diccionario = ["reloj", "chocolate", "viejo", "agua", "queso", "lata",
"calle", "arroz", "enchufe", "juguetes", "pollo", "palmera", "botella",
"tren", "conejo", "lupa", "papel", "alimentos", "lluvia", "taza", "tenedor",
"bostezar", "grande", "pies", "rodilla", "boca", "leer", "pescado", "primavera",
"maceta", "computadora", "globo", "bolso", "pantalones"]

select = random.choice(diccionario)

hidden = ""

turnos = len(select)

half = turnos // 2

select = list(select)

for character in select:
    hidden += "_"

hidden = list(hidden)

while turnos > 0:
    #turnos = 10
    print(str("".join(hidden)))
    ask = input("Ingresa letra: ").lower()
    check = False
    for posicion in range(0, len(select)):
        if select[posicion] == ask:
            hidden[posicion] = ask
            check = True
    if check:
        print("".join(hidden))
        print(bcolors.OKBLUE + "Te quedan " + str(turnos) + " turnos." + bcolors.ENDC)
    else:
        print(str("".join(hidden)))
        print (bcolors.FAIL + "Incorrecto, intenta nuevamente" + bcolors.ENDC)
        turnos -= 1
        print(bcolors.OKBLUE + "Te quedan " + str(turnos) + " turnos." + bcolors.ENDC)
    if str(hidden) == str(select):
        print("Ganaste!")
        exit(code=None)
    if half == turnos:
        print("""
        ---------
        | 0   0 |
        |   n   |
        |       |
        ---------
            |
        ----|----
            |
            |
           / \\
        """)
        print(bcolors.WARNING + "Te quedan la mitad de tus turnos!" + bcolors.ENDC)


if turnos == 0:
    print("Perdiste!")
    print("""
    ---------
    | x   x |
    |   n   |
    |       |
    ---------
        |
    ----|----
        |
        |
       / \\
    """)
    print(bcolors.OKGREEN + "La palabra era: " + str("".join(select)) + bcolors.ENDC)



    exit(code=None)
