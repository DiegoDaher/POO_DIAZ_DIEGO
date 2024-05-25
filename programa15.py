listaEdadesRegistradas = [12,34,23,11,17,37,21,19]
listaMayorEdad = []
listaMenorEdad = []
for i in listaEdadesRegistradas: 
    if i >= 18:
        listaMayorEdad.append(i)
    else:
        listaMenorEdad.append(i)

print("Mayor de edad")
for i in listaMayorEdad: 
    print(i)

print("Menor de edad")
for i in listaMenorEdad: 
    print(i)
