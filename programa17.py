exit = False;
while exit != True:
    print("Selecciona la opcion que deseas convertir:")
    print("1) Celsius a Fahrenheit")
    print("2) Fahrenheit a Celsius")
    print("3) Salir")
    op = input()
    if op=="1":
        print("Teclee los grados celsius")
        cel = float(input())
        far = (cel*(9/5)) + 32
        print(far,"° celsius es igual a ",cel," ° farenheit")
        print("********************************************")
    elif op=="2":
        print("Teclee los grados farenheit")
        far = float(input())
        cel = (far-32) * 5/9
        print(far,"° farenheit es igual a ",cel," °celsius")
        print("********************************************")
    elif op=="3":
        exit=True
        break
    else:
        print("*******************************************")
        print("*********Teclea una opción válida*********")
        print("*******************************************")




    