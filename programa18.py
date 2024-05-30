inventario = {
    "Manzana" : 31.90,
    "Platano" : 23.70,
    "Naranja" : 21.43,
    "Melon" : 40.99,
    "Sandia" : 35.90,
    "Chile" : 20.70,
    "Tomate" : 19.60,
    "Cebolla" : 12.10
}

print("precios sin descuento")
for key in inventario:
    value = inventario[key]
    print(key,": $",value)

for key in inventario:
    value = inventario[key]
    descuento = 0.15
    preciodto = value - (value*descuento)
    preciofinal = round(preciodto,2)
    inventario[key] = preciofinal
    
print("********************")
print("Precios con descuento")
for key in inventario:
    value = inventario[key]
    print(key,": $",value)