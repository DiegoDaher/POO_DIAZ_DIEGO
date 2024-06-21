#Creamos nuestra clase Carro y su principales ataributos (modelo, marca, año, color)) 
class Carro:
    def __init__(self, modelo, marca, año, color):
        self.modelo = modelo #atributo
        self.marca = marca #atributo
        self.año = año #atributo
        self.color = color #atributo
#metodos de la clase
    def encender(self):
        print("Arrancando motor de",self.modelo)
        
    def acelerar(self):
        print("Incrementando velocidad...")
    
    def frenar(self):
        print("Disminuyendo velocidad...")
        
    def apagar(self):
        print("Apagando motor...")

class Propietario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.carros = []

    def agregar_carro(self,carro):
        self.carros.append(carro)
        print(carro.modelo, " añadido a la lista de ",self.nombre)
    
    def ver_carros(self):
        for carro in self.carros:
            print(carro.modelo)
            
    def correr_carro(self):
        print("selecciona el carro a correr")
        for carro in self.carros:
            print("--",carro.modelo)
        selcarro=int(input())
        op=selcarro-1
        self.carros[op].encender()
        

#definir los objetos        
carro1 = Carro("Challenger","Dodge","1999","Gris")        
carro2 = Carro("Camaro","Chevrolet","1999","Rojo")

propietario=Propietario("Diego")

propietario.agregar_carro(carro1)
propietario.agregar_carro(carro2)
#propietario.ver_carros()
propietario.correr_carro()


"""
#imprimir los atributos de la clase
print("Carro 1:")
print("Modelo: ",carro1.modelo)
print("Marca: ",carro1.marca)
print("Año: ",carro1.año)
print("Color: ",carro1.color)

#print("carro 1: ", "\n" , "Modelo:", carro1.modelo, "\n","Marca:", carro1.marca,"\n","Año:", carro1.año,"\n","Modelo:", carro1.color)

#Probar los metodos de los objetos de la clase
while True:
    print("Acciones por el carro")
    print("1) encender")
    print("2) acelerar")
    print("3) frenar")
    print("4) apagar")
    print("5) Salir")
    accion=input()
    if accion=="1":
        carro1.encender()
    elif accion=="2":
        carro1.acelerar()
    elif accion=="4":
        carro1.acelerar()
    elif accion=="3":
        carro1.acelerar()
    elif accion=="5":
        break
   """ 