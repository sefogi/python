#una funcion es un fragmento de cogigo que podemos reutilizar
#funcion max y min aplica para listas y tuplas

numeros = [4,7,1,42,15,80]

# funcion max encontrando el numero mayor de una lista
numeros_mas_altos= max(numeros)


#funcion min encontrando el numero menor de una lista
numeros_mas_bajos= min(numeros)


#redondenado a 6 decimales con la funccion round se utiliza asi (n,# de decimales que queremos)
numero1 = round(12.345678, 2)

# funccion bool() retorna false -> si tiene un 0,vacio,ninguno,[lista vacia],(tupla vacia)/ true -> si le pasamos un numero
#distinto de 0, true, cadena o datos no vacios
resultado_bool = bool(0)

# funccion all() retorna True si todos los valores son verdaderos (si se tienen datos a excepcion que sea un 0)
resultado_all = all([7,"True",[344.23]])

# funcion sum() suma todos los valores de un iterable deben de ser numeros
suma_total = sum(numeros)
print(suma_total)