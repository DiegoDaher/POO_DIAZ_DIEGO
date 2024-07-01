#Creamos nuestra clase Carro y su principales ataributos (modelo, marca, año, color)) 
class Carro:
    def __init__(self, modelo, marca, año, color):
        self.modelo = modelo #atributo
        self.marca = marca #atributo
        self.año = año #atributo
        self.color = color #atributo+
        self.aleron = None
#metodos de la clase
    def encender(self):
        print("Arrancando motor de",self.modelo)
        
    def acelerar(self):
        print("Incrementando velocidad...")
    
    def frenar(self):
        print("Disminuyendo velocidad...")
        
    def apagar(self):
        print("Apagando motor de",self.modelo)
        
    def colocar_aleron(self,aleron):
        self.aleron = aleron
        
    def describir(self):
        print("El carro es un ", self.modelo,", de la automotriz ", self.marca, ",del año ",self.año," y de color",self.color)
        if self.aleron:
            print("tiene un alerón de color",self.aleron.color,",forma",self.aleron.forma,"y material",self.aleron.material)
        else:
            print("sin alerón")

#Agregar otra clase de tipo agregacion
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
        
#asociacion  
class Mecanico:
    def __init__(self,nombre):
        self.nombre = nombre
        self.carros_en_mantenimiento=[]
        
    def reparar_carro(self,carro):
        self.carros_en_mantenimiento.append(carro)
        print(self.nombre, "esta reparando a ", carro.modelo)
        
    def mostrar_carros_mantenimiento(self):
        print(self.nombre,"ha tratado los siguientes carros:")
        for carro in self.carros_en_mantenimiento:
            print(carro.modelo)
       
class Aleron:
    def __init__(self,color,forma,material):
        self.color = color
        self.forma = forma
        self.material = material
        
    def describir(self):
        print("Este es un alerón de color",self.color,",forma",self.forma,"y material",self.material)
        
#compocisicon 

#definir los objetos        
carro1 = Carro("Challenger","Dodge","1999","Gris")        
carro2 = Carro("Camaro","Chevrolet","1999","Rojo")
aleron1 = Aleron("Rojo","nylon","metalico")
aleron2 = Aleron("Plateado","Acero","plastico")

carro1.colocar_aleron(aleron1)
carro1.describir()
carro2.colocar_aleron(aleron2)
carro2.describir()


"""
#nuevo veterinario
mec1=Mecanico("Juan Alonso")
#metodos con veterinario
mec1.reparar_carro(carro1)
mec1.reparar_carro(carro2)
mec1.mostrar_carros_mantenimiento()

"""
"""
propietario=Propietario("Diego")

propietario.agregar_carro(carro1)
propietario.agregar_carro(carro2)
#propietario.ver_carros()
propietario.correr_carro()

"""


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
