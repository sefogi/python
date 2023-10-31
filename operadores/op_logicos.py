# los operadpres logicos son AND; OR ; NOT

# AND &
Resultado1 = True & True #Devolver True
Resultado2 = False & True #Devolver falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False # Devolver falso

#OR |
Resultado5 = True | True 	#Devolver true
Resultado6 = False | True    #Devolver True
Resultado7 = True | False   #Devolver TRUE
Resultado8 = False | False  #Devolver Falso

#NOT

Resultado9 = not True 		#Devuelve false, ya que el valor es negativo.
Resultado10 = not False     #Devuelve True, ya que el valor es positivo

#[::-1] #operador de rebanada este operador comienza en el ultimo caracter de cadena, y termina en el primer carácter de la cadena y avanza en pasos de -1. Esto significa que el operador devolverá una nueva cadena que es la cadena original invertida.
def backward_string(val: str) -> str:
    return val[::-1]
print(backward_string("carlos")) #devolvera "solrac"