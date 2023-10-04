#es una forma de asignar valores a variables de manera diferente y particular
#// en el caso de conjutos no permite desempaquetar datos //
# creamos una tupla
datos = ("Lucas", "Dalto", 100000)

#creamos una lista
datos_lista = ["Lucas", "Dalto", 100000]

# aqui cremos dos variables que desencapsulan la tupla ej: nombre = Lucas/ apellidos = Dalto
nombre, apellidos, suscriptores = datos_lista

print(suscriptores)
