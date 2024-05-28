listaEdadesRegistradas = [12,6,23,11,17,9,21,19,22,35,43,10,8]
listaInfancia = []
listaAdolescentes = []
listaJovenes = []
listaAdultos = []
for i in listaEdadesRegistradas: 
    if i >= 6 and i<=11:
        listaInfancia.append(i)
    elif i >= 12 and i<=17:
        listaAdolescentes.append(i)
    elif i >= 18 and i<=26:
        listaJovenes.append(i)
    elif i >= 27:
        listaAdultos.append(i)

print("Edades Registradas: ",listaEdadesRegistradas)
print("Grupo Infancia (6-11): ",listaInfancia)
print("Grupo Adolescentes: (12-17) ",listaAdolescentes)
print("Grupo Jovenes: (18-26) ",listaJovenes)
print("Grupo Adultos: (27-en adelante) ",listaAdultos)
