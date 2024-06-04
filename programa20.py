conjunto1={3,5,1,2,4,5}
conjunto2={9,1,7,11,6,8}
conjunto3={12,14,15,13,16,18}
conjuntoNuevo={}
conjuntob = conjunto1.union(conjunto2)
conjunto123 = conjuntob.union(conjunto3)
conjuntoNuevo = {num for num in conjunto123 if num % 2 == 0}

print(conjuntoNuevo)

