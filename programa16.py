print("Ingresa Promedio 1")
p1 = float(input())
print("Ingresa Promedio 2")
p2 = float(input())
print("Ingresa Promedio 3")
p3 = float(input())

if p1 > p2 and p1 > p3:
    print("El promedio mayor es: ",p1)
elif p2 > p1 and p2 > p3:
    print("El promedio mayor es: ",p2)
else:
    print("El promedio mayor es: ",p3)