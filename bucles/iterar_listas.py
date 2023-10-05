#recurda las listas son con []
animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,62,12,72]
numeros1 =[]

#recorriendo la lista animales
#dentro del ciclo for creamos una variable en este caso (animales)
#for animal in animales:
    #print(f'ahora la variable animal es igual a:{animal}')

#recorriendo la lista numeros y multiplicando cada valor por 10   
#aqui se creo despues del for una variable "resultado" donde pedimos que la vaiable "numero" se multiplique por 10    
#for numero in numeros:
    #resultado = numero * 10
    #print(resultado)
    
# iterar(recorrer) en dos listas usando zip al mismo tiempo
#for numero, animal in zip(animales,numeros):
    #print(f"recorriendo lista 1:{numero}")
    #print(f"recorriendo lista 2:{animal}")

# con range me permite crear un rango en este caso le pido a la variable num un rango de 1 al 21    
#for num in range(5):
    #print(num)
    
# forma no optima de recorrer una lista
#for num1 in range(len(numeros)):
    #print(numeros[num1])
    
#forma correcta de recorrer una lista con enumerate
#for num2 in enumerate(numeros):
    #indice = num2[0]
    #valor = num2[1]
    #print(f"el indice es, {indice} y el valor es: {valor}")
    
#recuerden que los indices comienzan desde cero hasta n-1 donde n es la longitud total de la lista

#usando else
for num3 in numeros1:
    print(f"ejecutando el ultimo bucle, valor actual: {num3}")
    
else:
    print("el bucle termino")
