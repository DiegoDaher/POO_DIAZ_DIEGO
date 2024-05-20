print("Ingresa el primer numero para la comparación")
n1 = int(input())
print("Ingresa el segundo numero para la comparación")
n2 = int(input())
if n1 > n2:
    print(n1 ," es mayor que ", n2,". Primer numero '",n1,"' es mayor")
elif n2 > n1:
    print(n1 ," es menor que ", n2,". Segundo numero '",n2,"' es mayor")
elif n1==n2:
    print("Los dos números son iguales")