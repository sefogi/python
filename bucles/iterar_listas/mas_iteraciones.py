
frutas = ["banana", "manzana", "ciruela","pera","naranja","granada","Durazno"]
cadena = "hola dalto"
numeros = [2,5,8,10]
#evitando que se coma una fruta con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f"me voy a comer una {fruta}")
    
# evitar que el bucle siga ejecutandose el else aqui no se ejecuta
for fruta in frutas:
   print(f"me voy a comer una {fruta}")
   if fruta == 'pera':
       break

print("bucle terminado")

# recorrer cadenas de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo(ejemplo duplicamos los numero)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
