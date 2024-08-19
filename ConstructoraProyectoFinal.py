#Conexion
import mysql.connector

class Database:
    def __init__(self, host, user, database):
        self.host = host
        self.user = user
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            database=self.database
        )
        print("Conexión establecida")

    def is_connected(self):
        return self.connection.is_connected() if self.connection else False
        
    def execute_query(self, query, params=None):
        if not self.is_connected():
            raise Exception("No hay conexión a la base de datos.")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()

    def fetchall(self, query, params=None):
        if not self.is_connected():
            raise Exception("No hay conexión a la base de datos.")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetchone(self, query, params=None):
        if not self.is_connected():
            raise Exception("No hay conexión a la base de datos.")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def close(self):
        if self.is_connected():
            self.connection.close()
            print("Conexión cerrada.")
        else:
            print("La conexión ya está cerrada o nunca se estableció.")

class Proyecto:

    def __init__(self, db, id_proyecto=None, nombre_proyecto=None, cliente=None, ubicacion=None, fecha_inicio=None, fecha_fin=None, estado=None):
        self.db = db
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.cliente = cliente
        self.ubicacion = ubicacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def crear_proyecto(self):
        query = "INSERT INTO proyectos (nombre_proyecto, cliente, ubicacion, fecha_inicio, fecha_fin, estado) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (self.nombre_proyecto, self.cliente, self.ubicacion, self.fecha_inicio, self.fecha_fin, self.estado)
        self.db.execute_query(query, params)

    def modificar_proyecto(self):
        query = "UPDATE Proyectos SET nombre_proyecto=%s, cliente=%s, ubicacion=%s, fecha_inicio=%s, fecha_fin=%s, estado=%s WHERE id_proyecto=%s"
        params = (self.nombre_proyecto, self.cliente, self.ubicacion, self.fecha_inicio, self.fecha_fin, self.estado, self.id_proyecto)
        self.db.execute_query(query, params)

    def eliminar_proyecto(self):
        id_proyecto = input("Ingrese el ID del proyecto a eliminar: ")
    
        query_delete_asignaciones = "DELETE FROM asignaciones WHERE id_proyecto = %s"
        self.db.execute_query(query_delete_asignaciones, (id_proyecto,))
    
        query_delete_proyecto = "DELETE FROM proyectos WHERE id_proyecto = %s"
        self.db.execute_query(query_delete_proyecto, (id_proyecto,))

    def consultar_proyecto(self):
        query = "SELECT * FROM Proyectos WHERE id_proyecto=%s"
        params = (self.id_proyecto,)
        return self.db.fetchone(query, params)

class Empleado:
    def __init__(self, db, id_empleado=None, nombre_empleado=None, especialidad=None, telefono=None, correo=None):
        self.db = db
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo

    def crear_empleado(self):
        query = "INSERT INTO empleados (nombre_empleado, especialidad, telefono, correo) VALUES (%s, %s, %s, %s)"
        params = (self.nombre_empleado, self.especialidad, self.telefono, self.correo)
        self.db.execute_query(query, params)
        print("Empleado creado exitosamente.")

    def modificar_empleado(self):
        query = "UPDATE empleados SET nombre_empleado=%s, especialidad=%s, telefono=%s, correo=%s WHERE id_empleado=%s"
        params = (self.nombre_empleado, self.especialidad, self.telefono, self.correo, self.id_empleado)
        self.db.execute_query(query, params)
        print("Empleado modificado exitosamente.")

    def eliminar_empleado(self, id_empleado):
        delete_asignaciones_query = "DELETE FROM asignaciones WHERE id_empleado = %s"
        self.db.execute_query(delete_asignaciones_query, (id_empleado,))

        delete_empleado_query = "DELETE FROM empleados WHERE id_empleado = %s"
        self.db.execute_query(delete_empleado_query, (id_empleado,))

    def consultar_empleado(self):
        query = "SELECT * FROM empleados WHERE id_empleado=%s"
        params = (self.id_empleado,)
        return self.db.fetchone(query, params)


class Asignacion:
    def __init__(self, db, id_asignacion=None, id_empleado=None, proyecto_id=None, fecha_asignacion=None):
        self.db = db
        self.id_asignacion = id_asignacion
        self.id_empleado = id_empleado
        self.proyecto_id = proyecto_id
        self.fecha_asignacion = fecha_asignacion

    def crear_asignacion(self):
        query = "INSERT INTO asignaciones (id_empleado, id_proyecto, fecha_asignacion) VALUES (%s, %s, %s)"

        params = (self.id_empleado, self.proyecto_id, self.fecha_asignacion)
        self.db.execute_query(query, params)
        print("Asignación creada exitosamente.")

    def actualizar_asignacion(self):
        query = """
        UPDATE asignaciones
        SET id_empleado = %s, proyecto_id = %s, fecha_asignacion = %s
        WHERE id_asignacion = %s
        """
        params = (self.id_empleado, self.proyecto_id, self.fecha_asignacion, self.id_asignacion)
        self.db.execute_query(query, params)
        print("Asignación actualizada exitosamente.")

    def eliminar_asignacion(self):
        query = "DELETE FROM asignaciones WHERE id_asignacion = %s"
        params = (self.id_asignacion,)
        self.db.execute_query(query, params)
        print("Asignación eliminada exitosamente.")

    def obtener_asignacion_por_id(self):
        query = "SELECT * FROM asignaciones WHERE id_asignacion = %s"
        params = (self.id_asignacion,)
        result = self.db.fetchone(query, params)
        if result:
            self.id_empleado, self.proyecto_id, self.fecha_asignacion = result[1], result[2], result[3]
            print(f"Asignación obtenida: Empleado ID: {self.id_empleado}, Proyecto ID: {self.proyecto_id}, Fecha Asignación: {self.fecha_asignacion}")
        else:
            print("No se encontró ninguna asignación con ese ID.")

    def obtener_todas_asignaciones(self):
        query = "SELECT * FROM asignaciones"
        results = self.db.fetchall(query)
        for row in results:
            print(f"ID: {row[0]}, Empleado ID: {row[1]}, Proyecto ID: {row[2]}, Fecha Asignación: {row[3]}")


def menu_principal(db):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Proyectos")
        print("2. Gestión de Empleados")
        print("3. Gestión de Asignaciones")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_proyectos(db)
        elif opcion == "2":
            menu_empleados(db)
        elif opcion == "3":
            menu_asignaciones(db)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_proyectos(db):
    while True:
        print("\n--- Gestión de Proyectos ---")
        print("1. Crear Proyecto")
        print("2. Modificar Proyecto")
        print("3. Eliminar Proyecto")
        print("4. Consultar Proyecto por ID")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_proyecto = input("Nombre del proyecto: ")
            cliente = input("Cliente: ")
            ubicacion = input("Ubicación: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
            estado = input("Estado: ")

            proyecto = Proyecto(db, nombre_proyecto=nombre_proyecto, cliente=cliente, ubicacion=ubicacion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, estado=estado)
            proyecto.crear_proyecto()
            print("Proyecto creado exitosamente.")
        
        elif opcion == "2":
            id_proyecto = input("ID del proyecto a modificar: ")
            nombre_proyecto = input("Nuevo nombre del proyecto: ")
            cliente = input("Nuevo cliente: ")
            ubicacion = input("Nueva ubicación: ")
            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
            estado = input("Nuevo estado: ")

            proyecto = Proyecto(db, id_proyecto=id_proyecto, nombre_proyecto=nombre_proyecto, cliente=cliente, ubicacion=ubicacion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, estado=estado)
            proyecto.modificar_proyecto()
            print("Proyecto modificado exitosamente.")

        elif opcion == "3":
            id_proyecto = input("ID del proyecto a eliminar: ")

            proyecto = Proyecto(db, id_proyecto=id_proyecto)
            proyecto.eliminar_proyecto()
            print("Proyecto eliminado exitosamente.")
        
        elif opcion == "4":
            id_proyecto = input("ID del proyecto a consultar: ")

            proyecto = Proyecto(db, id_proyecto=id_proyecto)
            resultado = proyecto.consultar_proyecto()
            if resultado:
                print(f"ID: {resultado[0]}, Nombre: {resultado[1]}, Cliente: {resultado[2]}, Ubicación: {resultado[3]}, Fecha de Inicio: {resultado[4]}, Fecha de Fin: {resultado[5]}, Estado: {resultado[6]}")
            else:
                print("No se encontró ningún proyecto con ese ID.")

        elif opcion == "5":
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_empleados(db):
    empleado = Empleado(db)
    while True:
        print("\n--- Gestión de Empleados ---")
        print("1. Crear Empleado")
        print("2. Modificar Empleado")
        print("3. Eliminar Empleado")
        print("4. Consultar Empleado por ID")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_empleado = input("Nombre del empleado: ")
            especialidad = input("Especialidad: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")

            empleado = Empleado(db, nombre_empleado=nombre_empleado, especialidad=especialidad, telefono=telefono, correo=correo)
            empleado.crear_empleado()
            print("Empleado creado exitosamente.")
        
        elif opcion == "2":
            id_empleado = input("ID del empleado a modificar: ")
            nombre_empleado = input("Nuevo nombre del empleado: ")
            especialidad = input("Nueva especialidad: ")
            telefono = input("Nuevo teléfono: ")
            correo = input("Nuevo correo: ")

            empleado = Empleado(db, id_empleado=id_empleado, nombre_empleado=nombre_empleado, especialidad=especialidad, telefono=telefono, correo=correo)
            empleado.modificar_empleado()
            print("Empleado modificado exitosamente.")

        elif opcion == "3":
            id_empleado = input("Ingresa el ID del empleado que deseas eliminar: ")
            empleado.eliminar_empleado(id_empleado)
            print("Empleado eliminado exitosamente.")
        
        elif opcion == "4":
            id_empleado = input("ID del empleado a consultar: ")

            empleado = Empleado(db, id_empleado=id_empleado)
            resultado = empleado.consultar_empleado()
            if resultado:
                print(f"ID: {resultado[0]}, Nombre: {resultado[1]}, Especialidad: {resultado[2]}, Teléfono: {resultado[3]}, Correo: {resultado[4]}")
            else:
                print("No se encontró ningún empleado con ese ID.")

        elif opcion == "5":
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_asignaciones(db):
    while True:
        print("\n--- Gestión de Asignaciones ---")
        print("1. Crear Asignación")
        print("2. Modificar Asignación")
        print("3. Eliminar Asignación")
        print("4. Consultar Asignación por ID")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_empleado = input("ID del empleado: ")
            proyecto_id = input("ID del proyecto: ")
            fecha_asignacion = input("Fecha de asignación (YYYY-MM-DD): ")

            asignacion = Asignacion(db, id_empleado=id_empleado, proyecto_id=proyecto_id, fecha_asignacion=fecha_asignacion)
            asignacion.crear_asignacion()
        
        elif opcion == "2":
            id_asignacion = input("ID de la asignación a modificar: ")
            empleado_id = input("Nuevo ID del empleado: ")
            proyecto_id = input("Nuevo ID del proyecto: ")
            fecha_asignacion = input("Nueva fecha de asignación (YYYY-MM-DD): ")

            asignacion = Asignacion(db, id_asignacion=id_asignacion, empleado_id=empleado_id, proyecto_id=proyecto_id, fecha_asignacion=fecha_asignacion)
            asignacion.actualizar_asignacion()

        elif opcion == "3":
            id_asignacion = input("ID de la asignación a eliminar: ")

            asignacion = Asignacion(db, id_asignacion=id_asignacion)
            asignacion.eliminar_asignacion()
        
        elif opcion == "4":
            id_asignacion = input("ID de la asignación a consultar: ")

            asignacion = Asignacion(db, id_asignacion=id_asignacion)
            asignacion.obtener_asignacion_por_id()

        elif opcion == "5":
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Conexión a la base de datos
db = Database(host='localhost', user='root', database='constructora')
db.connect()

# Ejecutar el menú principal
menu_principal(db)

# Cerrar la conexión al final
db.close()
