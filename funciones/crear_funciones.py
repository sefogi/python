# creando una funcion  simple
#def saludar():
    #print("hola sebas. eres el mejor")
#ejecutando la funcion simple   
#saludar()

#crear una funcion que tenga parametros(parametro: variables que se crean para ser usados dentro de una funcion)
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo ="titan"
    else:
        adjetivo ='no lo sabemos'
    
    print(f"Hola {nombre}, mi {adjetivo} como estas")
    
saludar("seba", "hombre")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars ="abcdefghij" #creamos caracteres aleatorios
    num_entero = str(num) #aqui convertimos a string la variable num
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return(contraseña) # el return se usa para que sea un valor que solo vea el desarrollador a diferencia de print
    
password = crear_contraseña_random(10)
frase = f"tu contraseña nueva es: {password}"
print(frase)

# crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars ="abcdefghij" #creamos caracteres aleatorios
    num_entero = str(num) #aqui convertimos a string la variable num
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num #puedo usar una tupla
#desempaquetando la funcion
password, primer_numero = crear_contraseña_random(398)

#mostrando los resultados obtenidos y los datos utilizaos para optenerlo
print(f"Tu contraseña nueva es:{password}")
print(f"El numero utilizado para crearla fue:{primer_numero}")
