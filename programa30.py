import os
os.system('cls')

import mysql.connector
def conexion():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='dbescolares'
    )
    return connection

    
def mostrar_alumnos():
    connection = conexion()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alumnos")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cursor.close()
    connection.close()
    
def mostrar_aula():
    connection = conexion()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM aula")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cursor.close()
    connection.close()
    
def mostrar_maestros():
    connection = conexion()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM maestros")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cursor.close()
    connection.close()
    
def registrar_alumno():
    connection = conexion()
    cursor = connection.cursor()
    nombre = input("Ingrese su Nombre: ")
    edad = int(input("Ingrese su Edad: "))
    direccion = input("Ingrese su Dirección: ")
    id_maestro = int(input("Ingrese el ID del Maestro: "))
    id_aula = int(input("Ingrese el ID del Aula: "))
    cursor.execute(
        "INSERT INTO alumnos (nombre, edad, direccion, id_maestro) VALUES (%s, %s, %s, %s)",
        (nombre, edad, direccion, id_maestro,id_aula)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("Alumno registrado exitosamente.")
    
    
def eliminar_alumno():
    connection = conexion()
    cursor = connection.cursor()
    borrar = input("Ingrese el ID del usuario que quiere borrar: ")
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (borrar,))
    if cursor.rowcount > 0:
        print(f"Usuario con ID {borrar} borrado exitosamente.")
    else:
        print(f"No se encontró ningún usuario con ID {borrar}.")
    connection.commit()
    cursor.close()
    connection.close()

def menu():
    while True:
        print("Menu Principal:")
        print("1. Mostrar Alumnos")
        print("2. Mostrar Aulas")
        print("3. Mostrar Maestros")
        print("4. Registrar Alumno")
        print("5. Eliminar Alumno")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_alumnos()
        elif opcion == "2":
            mostrar_aula()
        elif opcion == "3":
            mostrar_maestros()
        elif opcion == "4":
            registrar_alumno()
        elif opcion == "5":
            eliminar_alumno()
        elif opcion == "6":
            print("Saliendo del programa")
            break;
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
menu()