#Creamos nuestra clase Carro y su principales ataributos (modelo, marca, año, color)) 
class Carro:
    def __init__(self, modelo, marca, año, color):
        self.modelo = modelo #atributo
        self.marca = marca #atributo
        self.año = año #atributo
        self.color = color #atributo
        
    def encender(self):
        print("Arrancando motor...")
        
    def acelerar(self):
        print("Incrementando velocidad...")
    
    def frenar(self):
        print("Disminuyendo velocidad...")
        
    def apagar(self):
        print("Apagando motor...")
        
carro1 = Carro("Camaro","Chevrolet","1999","Rojo")
carro1 = Carro("Challenger","Dodge","1999","Gris")

print("Carro 1:")
print("Modelo: ",carro1.modelo)
print("Marca: ",carro1.marca)
print("Año: ",carro1.año)
print("Color: ",carro1.color)

#print("carro 1: ", "\n" , "Modelo:", carro1.modelo, "\n","Marca:", carro1.marca,"\n","Año:", carro1.año,"\n","Modelo:", carro1.color)
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
    