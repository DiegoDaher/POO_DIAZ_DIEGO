info_estudiantes = {}

def clear_screen():
    print("\033c", end="")
    
while True:
    print("\nMENÚ")
    print("1) Agregar estudiantes")
    print("2) Consulte las calificaciones de un estudiante")
    print("3) Ver todas las calificaciones")
    print("4) Salir")

    opcion = input("Seleccione una opción: ")
    print("")

    if opcion == "1":
        nombre = input("Agrege el nombre de un estudiante: ")
        calificacion = input("Agregue la calificacion del estudiante: ")
        info_estudiantes[nombre] = calificacion
        print(f"\nCALIFICACIONES: ")
        for key,value in info_estudiantes.items():
            print(f"{key} : {value}")
    elif opcion == "2": 
        nombrebuscar = input("Introduzca el nombre a buscar: ")
        while nombre != nombrebuscar:
            print("Nombre no encontrado. Introduzca uno correcto")  
            nombrebuscar = input("Introduzca el nombre a buscar: ")
        nombreguardado = info_estudiantes[nombrebuscar]
        print(f"calificacion de {nombrebuscar} : {nombreguardado}")
    elif opcion == "3":
        clear_screen()
        for key,value in info_estudiantes.items():
            print(f"{key} : {value}")
    elif opcion == "4":
        print("Saliendo.....")
        break
    else:
        print("Opción invalida. Por favor introduzca una correcta")
        opcion = input("Seleccione una opción: ")