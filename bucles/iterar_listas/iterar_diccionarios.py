diccionario = {
    "nombre": "Lucas",
    "apellidos": "Dalto",
    "subs": 10000000
}

# value es valor key es llave con value veo los primeros datos con key los segundos 
#recorriendo diccionario para obtener las claves
for key in diccionario:
    print(key)
    
#con .items podemos iterar el elemento 
#recorriendo el diccionario con.items() para obtener las claves y valores   
for datos in diccionario.items():
    key = datos[0]
    value = datos [1]
    print(f"la clave es: {key} y el valor es : {value}")