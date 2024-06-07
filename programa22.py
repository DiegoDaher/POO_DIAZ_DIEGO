def sumar(a,b):
    suma = a + b
    return suma

def restar(a,b):
    resta = a - b
    return resta

def multiplicar(a,b):
    multiplicacion = a * b
    return multiplicacion

def dividir(a,b):
    division = a + b
    return division


while True:
    print("MENÚ")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        operacion = "sumar"
        operador = "+"
        a = float(input(f"ingrese el número a {operacion}: "))
        b = float(input(f"ingrese el otro número a {operacion}: "))
        resultado = sumar(a,b)
        print(f"Resultado es : {a} {operador} {b} = {resultado}\n")

    elif opcion == "2":
        operacion = "restar"
        operador = "-"
        a = float(input(f"ingrese el número a {operacion}: "))
        b = float(input(f"ingrese el otro número a {operacion}: "))
        resultado = restar(a,b)
        print(f"Resultado es : {a} {operador} {b} = {resultado}\n")

    elif opcion == "3":
        operacion = "multiplicar"
        operador = "x"
        a = float(input(f"ingrese el número a {operacion}: "))
        b = float(input(f"ingrese el otro número a {operacion}: "))
        resultado = multiplicar(a,b)
        print(f"Resultado es : {a} {operador} {b} = {resultado}\n")
    
    elif opcion == "4":
        operacion = "dividir"
        operador = "/"
        a = float(input(f"ingrese el número a {operacion}: "))
        b = float(input(f"ingrese el otro número a {operacion}: "))
        resultado = dividir(a,b)
        print(f"Resultado es : {a} {operador} {b} = {resultado}\n")

    elif opcion == "5":
        print("***************Proceso Terminado************")
        break

    else:
        print("Selecciona una opcion valida")