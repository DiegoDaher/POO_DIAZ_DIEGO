print("Ingresa tu edad para saber si puedes ingresar al antro")
edad = int(input())
if edad >= 18 and edad < 100:
    print("Bienvenido, puedes entrar")
elif edad < 18 and edad >0:
    print("Lo siento, no puedes entrar")
else:
    print("Lo siento, ingresa una edad válida")