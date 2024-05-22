con = 0
suma = 0
numero=int(input("ingresa un numero "))
suma += numero
while con == 0:
    numero=int(input("ingresa un numero para sumar "))
    suma += numero
    print (suma)
    while True:
        sentencia = input("Desea continuar? s=si n=no ")
        if sentencia == "n":
            con = 1
            break
        elif sentencia == "s":
            con = 0
            break
        else:
            print("Teclea una respuesta válida")



