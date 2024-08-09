class Carro:
    def __init__(self, modelo, marca, año, color):
        self.modelo = modelo #atributo
        self.marca = marca #atributo
        self.año = año #atributo
        self.color = color #atributo
        
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self,modelo):
        self.modelo = modelo
        
    def encender(self):
        print("Arrancando motor de",self.modelo)
        
    def acelerar(self):
        print("Incrementando velocidad...")
        
    def describir(self):
        print("El vehiculo es un ", self.modelo,", de la automotriz ", self.marca, ", del año ",self.año," y de color",self.color)
    

class Camioneta(Carro):
    def __init__(self,modelo,marca,año,color,cabina):
        super().__init__(modelo,marca,año,color)
        self.cabina = cabina
        
    def describir(self):
        super().describir()
        print("tiene una cabina",self.cabina)
        
class Motocicleta(Carro):
    def __init__(self, modelo, marca, año, color,tipo):
        super().__init__(modelo, marca, año, color)
        self.tipo = tipo            
    
    def describir(self):
        super().describir()
        print("esta motocicleta es para",self.tipo) 
        
class Camion(Carro):
    def __init__(self,modelo,marca,año,color,remolque):
        super().__init__(modelo,marca,año,color)
        self.remolque = remolque
        
    def describir(self):
        super().describir()
        print("tiene un remolque",self.remolque)
        
carro1 = Carro("Jetta","Volkswagen","2005","negro")
moto1 = Motocicleta("Hyper","vento",2016,"rojo","carreras")
camion1 = Camion("Actros L","Mercedes Benz",2006,"rojo","Doble")
camioneta1 = Camioneta("R4va","Toyota",2019,"blanca","doble")


#abstraccion
print("*********abstraccion:")
carro1.encender()

#Encapsulacion
print("*********Encapsulacion:")
print("modelo anterior: ",carro1.get_modelo())
carro1.set_modelo("sedan")
print("modelo nuevo: ",carro1.get_modelo())

#Herencia 
print("*********herencia:")
camioneta1 = Camioneta("SUV","Volkswagen","2018","Blanco","cerrada")
camioneta1.describir()
camioneta1.encender()

#polimorfismo
print("*********polimorfismo:")
carro1.describir()
camion1.describir()
camioneta1.describir()
moto1.describir()