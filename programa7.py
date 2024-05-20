print("Ingresa el peso en kilos (kg) del paquete ingresado")
kg = float(input())
if kg < 1:
    tarifa = float(50.0)
elif kg < 5 and kg > 1:
    tarifa = float(100.0)
elif kg < 10 and kg > 5:
    tarifa = float(200.0)
else:
    tarifa = float(500.0)

print("El peso de tu producto es: ",kg," kilos")
print("Tu tarifa a pagar es: $",tarifa)