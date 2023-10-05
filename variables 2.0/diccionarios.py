#creando diccionarios con dict()

diccionario = dict(nombre = "Lucas", apellido = "Dalto")
# crea como variables dento del diccionario

#las listas no pueden ser claves por que son mutables daria error pero las tuplas si en el caso de conjuntos se puede usando
#frozenset ej: diccionario_1 = {frozenset(["carlos","mario"]): "jajajja"}
diccionario_1 = {("carlos","mario"): "jajajja"}

# creando dicccionario con el metodo de diccionario dict.fromkeys() con dos valores,(siempre va a tomar el primero como iterable)
# valor por defecto "none"
diccionario_2 = dict.fromkeys(["nombre","apellidos"])

#creando diccionarios con dict.fromkey() cambiando el valor por defecto a "no se"
diccionario_3 = dict.fromkeys(["nombre","apellido"],"no se")

print(diccionario_3) 