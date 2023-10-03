#Crando una lista con list es una funcion debe llevar ([])
lista = list([False,28,23,34,True])

#devuelve la cantidad de elementos de la lista
cantidad_de_la_lista = len(lista)

# agregar elementos a la lista con append
lista.append(48)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,29)

#agregando varios elementos a la lista OJO se debe agregar como si fuera otra lista asi ([])
lista.extend([False,2030,41])

#eliminando un elemento de la lista(por su indice) recuerda cuenta de 0 a 9 )para eliminar el ultimo elemento usar -1 -2 para eliminar el penultimo y asi sucesivamente
lista.pop()

#removiendo un elemento de la  lista por su valor
lista.remove(29)

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la list de forma asendente(si usamos el parametro reerse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()
print(lista)