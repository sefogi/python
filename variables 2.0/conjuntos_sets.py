# creando un conjunto con set()

conjunto = set(["dato1",])

#metiendo un conjunto dentro de otro conjunto usando la funcion frozenset ([])
conjunto1 = frozenset (["dato1","dato2"])
conjunto2 = {conjunto1, "dato 3"}
#print(conjunto2)

#teoria de conjuntos
conjunto_1 = {1,3,5,7}
conjunto_2 ={1,3,7}
#verificando si es un subconjunto se usa .issubset o tambien <= 
#resultado = conjunto_2.issubset(conjunto_1)
resultado = conjunto_2 <= conjunto_1

#verificano si es un superconjunto
resultado_1 = conjunto_1.issuperset(conjunto_2)
resultado_2 = conjunto_1 > conjunto_2

#verificar si hay un resultado en comun
resultado_3 = conjunto_2.isdisjoint(conjunto_1)

print(resultado_3)