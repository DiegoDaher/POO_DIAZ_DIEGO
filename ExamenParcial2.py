#Creamos nuestra clase Carro y su principales ataributos (modelo, marca, año, color)) 
class Carro:
    def __init__(self, modelo, marca, año, color):
        self.modelo = modelo #atributo
        self.marca = marca #atributo
        self.año = año #atributo
        self.color = color #atributo
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
   
    #metodo con el uso de la clase compocision (aleron)    
    def describir(self):
        print("El vehiculo es un ", self.modelo,", de la automotriz ", self.marca, ",del año ",self.año," y de color",self.color)
        if self.aleron:
            print("tiene un alerón de color",self.aleron.color,",forma",self.aleron.forma,"y material",self.aleron.material)
        else:
            print("sin alerón")
            
    #metodo con el uso de la clase dependencia (gasolina)        
    def llenar_tanque(self,gasolina):
        print(self.modelo,"esta llenando el tanque con",gasolina.tipo)


#agregacion
class Propietario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.carros = []

    def agregar_carro(self,carro):
        self.carros.append(carro)
        #comprobar que el carro se ha añadido
        #print(carro.modelo, " añadido a la lista de ",self.nombre)
    
    def ver_carros(self):
        for carro in self.carros:
            print(carro.modelo)
            
    #uso de estructura de datos  
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
  
#compocision      
class Aleron:
    def __init__(self,color,forma,material):
        self.color = color
        self.forma = forma
        self.material = material
        
    def describir(self):
        print("Este es un alerón de color",self.color,",forma",self.forma,"y material",self.material)
  
#herencia      
class Motocicleta(Carro):
    def __init__(self, modelo, marca, año, color,tipo):
        super().__init__(modelo, marca, año, color)
        self.tipo = tipo            
    
    def describir(self):
        super().describir()
        print("esta motocicleta es para",self.tipo) 

class Camioneta(Carro):
    def __init__(self,modelo,marca,año,color,cabina):
        super().__init__(modelo,marca,año,color)
        self.cabina = cabina
        
    def describir(self):
        super().describir()
        print("tiene una cabina",self.cabina)
        
class Camion(Carro):
    def __init__(self,modelo,marca,año,color,remolque):
        super().__init__(modelo,marca,año,color)
        self.remolque = remolque
        
    def describir(self):
        super().describir()
        print("tiene un remolque",self.remolque)
        
#dependencia
class Gasolina:
    def __init__(self,tipo,octanaje):
        self.tipo = tipo
        self.octanaje = octanaje
        
    def describir(self):
        print("Es gasolina",self.tipo,"de octanaje de",self.octanaje)
        


#********definir los objetos**********
#carro
carro1 = Carro("Challenger","Dodge","1999","Gris")        
carro2 = Carro("Camaro","Chevrolet","1999","Rojo")

#motocicleta
moto1 = Motocicleta("Hyper","vento",2016,"rojo","carreras")
moto2 = Motocicleta("Burgman","suzuki",2018,"negro","carreras")

#camioneta
camioneta1 = Camioneta("R4va","Toyota",2019,"blanca","doble")
camioneta2 = Camioneta("Traverse","Chevrolet",2020,"gris","sencilla")

#camion
camion1 = Camion("Actros L","Mercedes Benz",2006,"rojo","Doble")
camion2 = Camion("D-600","Dodge",2002,"blanco","caja")

#propietario
propietarios_list=[]
propietario1=Propietario("Diego")
propietario2=Propietario("Ana")
propietarios_list.append(propietario1)
propietarios_list.append(propietario2)

#mecanico
mecanicos_list=[]
mec1=Mecanico("Juan Alonso")
mec2=Mecanico("Jose Alberto")
mecanicos_list.append(mec1)
mecanicos_list.append(mec2)

#aleron
aleron_list=[]
aleron1 = Aleron("Rojo","nylon","metalico")
aleron2 = Aleron("Plateado","Acero","plastico")
aleron_list.append(aleron1)
aleron_list.append(aleron2)

#gasolina
gasolina_list=[]
gasreg = Gasolina("Regular", "88")
gaspre = Gasolina("Premium", "92")
gasolina_list.append(gasreg)
gasolina_list.append(gaspre)

vehiculos_list=[]
vehiculos_list.append(carro1)
vehiculos_list.append(moto1)
vehiculos_list.append(camion1)
vehiculos_list.append(camioneta1)
vehiculos_list.append(carro2)
vehiculos_list.append(moto2)
vehiculos_list.append(camion2)
vehiculos_list.append(camioneta2)

propietario1.agregar_carro(carro1)
propietario1.agregar_carro(moto1)
propietario1.agregar_carro(camion1)
propietario1.agregar_carro(camioneta1)

propietario2.agregar_carro(carro2)
propietario2.agregar_carro(moto2)
propietario2.agregar_carro(camion2)
propietario2.agregar_carro(camioneta2)
   
def propietarios_menu():
    print("selecciona un propietario a modificar:")
    for propietario in propietarios_list:
        print(propietario.nombre)
    propietariosel=int(input())
    op=propietariosel-1
    print("**************************")
    print("lista de carros de",propietarios_list[op].nombre)
    propietarios_list[op].ver_carros()
    print("selecciona un carro")
    carrosel=int(input())
    opcs=carrosel-1
    exit=False
    while exit != True:
        print("selecciona la actividad")
        print("1 - Encender carro")
        print("2 - acelerar carro")
        print("3 - frenar carro")
        print("4 - apagar carro")
        print("5 - colocar aleron")
        print("6 - mostrar caracteristicas")
        print("7 - llenar tanque")
        opcion = input("Opción: ")
        if opcion == "1":
            propietario.carros[opcs].encender()
            print("*****************************")
        if opcion == "2":
            propietario.carros[opcs].acelerar()
            print("*****************************")
        if opcion == "3":
            propietario.carros[opcs].frenar()
            print("*****************************")
        if opcion == "4":
            propietario.carros[opcs].apagar()
            print("*****************************")
            exit=True
            break
        if opcion == "5":
            for aleron in aleron_list:
                print("--",aleron.forma)
            aleronsel=int(input())
            op=aleronsel-1
            propietario.carros[op].colocar_aleron(aleron_list[op])
            print("*****************************")
        if opcion == "6":
            propietario.carros[op].describir()
            print("*****************************")
        if opcion == "7":
            print("selecciona la gasolina")
            for gasolina in gasolina_list:
                print("--",gasolina.tipo)
            gassel=int(input())
            op=gassel-1
            propietario.carros[op].llenar_tanque(gasolina_list[op])
            print("*****************************")
        else:
            print("Seleccione una opcion valida")
            print("*****************************")
            
def mecanico_menu():
    print("selecciona un mecanico a modificar:")
    for mecanico in mecanicos_list:
        print(mecanico.nombre)
    mecsel=int(input())
    op=mecsel-1
    print("selecciona la actividad")
    print("1 - reparar carro")
    print("2 - mostrar carros")
    opcion = input()
    if opcion == "1":
        print("seleccione un carro a reparar")
        for carro in vehiculos_list:
            print(carro.modelo)
        veh_sel=int(input())
        op1=veh_sel-1
        mecanicos_list[op].reparar_carro(vehiculos_list[op1])
    elif opcion=="2":
        mecanicos_list[op].mostrar_carros_mantenimiento()
    else:
        print("Seleccione una opcion valida")
        print("*****************************")
exit=False
while exit != True:
    print("Taller mastercar")
    print("Selecciona el usuario")
    print("1 - dueños")
    print("2 - mecanicos")
    print("3 - Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        propietarios_menu()
    elif opcion == "2":
        mecanico_menu()
    elif opcion == "3":
        exit = True
        break
    else:
        print("Opción invalida. Por favor elije una opcion disponible.")