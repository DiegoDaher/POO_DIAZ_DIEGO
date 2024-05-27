import math
exit = False;
while exit != True:
    print("*******************************************")
    print("Calculo de areas")
    print("Selecciona el area de la figura que deseas Area")
    print("1 - Rectangulo")
    print("2 - Triangulo")
    print("3 - Circulo")
    print("4 - Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print("Area de un rectangulo")
        lado_a = float(input("Lado A del Rectangulo: "))
        lado_b = float(input("Lado B del Rectangulo: "))

        rectangulo = lado_a * lado_b

        print("El area del rectangulo es: ",rectangulo,"cm2")
        print("*******************************************")

    elif opcion == "2":
        print("Area de un triángulo")
        base = float(input("Base del Triángulo: "))
        altura = float(input("Altura del Triángulo: "))
        triangulo = (base * altura)/2
        print("El area del Triángulo es: ",triangulo,"cm2")
        print("*******************************************")

    elif opcion == "3":
        print("Area de un circulo")
        diametro = float(input("Cuanto mide el diametro del circulo: "))
        radio = diametro / 2
        circulo = math.pi * (radio * radio)
        print("El area del circulo es: ",circulo,"cm2")
        print("*******************************************")

    elif opcion == "4":
        exit = True
        break

    else:
        print("Opción invalida. Por favor elije una opcion disponible.")
    