#keys() devuelve las claves
# get() devuelve el valor de una clave
# clear() elimina todos los elementos
# pop () elimina un elemento
# items() para iterar el dicionario

diccionario = {
    "nombre": 'lucas',
    "apellido": 'dalto',
    "subs": 10000000
}

#nos devuelve un elemnto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_sfg = diccionario.get("sfg")
print("hola papa el programa continua")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#opteniendo un elemento dict_items iterable(recorer el elemento)
diccionario_iterable = diccionario.items()


print(diccionario_iterable)