#son datos que tienen adentro otros datos usan []
lista=["lucas dalto", "soy Dalto", True,1.85]
#se toman los datos desde 0 a 9 ejemplo lucas dalto seria = 0
print(lista[3])

#esto es valido
lista[3]= "maquinola" #me imprime maquinola

#TUPLAS son parecidas a las listas pero no se pueden modificar Y usan ()
tupla=("lucas dalto", "soy dalto", True, 1.85)
print(tupla[3])#siempre que se quiera buscar en una lista o tupla se una print([])

#lista[3]= "maquinola" me muestra error ya que no se puede modificar

#creando un conjunto (set) estos no tienen un orden fijo, 
# son elementos desordenados y pueden cambiar y usan {} en los conjuntos
#no podemos acceder al indice ej: print(conjunto[1]) me sale error
#tampoco pueden haber datos duplicados, y si los hay los elimina
conjunto={"lucas dalto", "soy dalto", True, 1.85}

#creando un diccionario usa {} lo que en javascript seria un json la estructura es clave:valor y se separa con comas cuando hay mas de 1 elemento
diccionario={
    'nombre': "Lucas dalto",
    'canal': "soy dalto",
    'altura': 1.84,
    'dato_duplicado':"soy dalto"
    
    
}

print(diccionario['nombre'])


