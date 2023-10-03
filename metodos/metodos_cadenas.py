# DIR= devuelve todos los atributos validos del objeto pasado
# Upper convierte todo en mayusc.
# Lower convierte a minusc.
# Capitalize primer letra en mayuscula
# Find : encuentra la primera aparicion del valor especificado, si no devuelve 1
# son asi : cadena1.uppper()

cadena1 = "hola, soy, Dalto"
cadena2 = "Bienvenido maquinola"

mayuscula = cadena1.upper()# metodo upper coloca todo en mayusc
minuscula = cadena1.lower()# metodo lower convierte todo en minusc
primera_letra_mayusc = cadena1.capitalize()#metodo capitalize primera letra en mayuscula
busqueda_find = cadena1.find("a")#buscamos una cadena en otra cadena en este caso se pide que busque hola y devuelve 0
#esto siginifica que hola esta de primero en la cadena "hola soy dalto" si no ahy concidencias devuelve -1
busqueda_index = cadena1.index("D")#buscamos una cadena en otra cadena,si no encuentra nada lanza una execpcion que seria un error ç
es_numerico = cadena1.isnumeric()#si es numerico, devolvemos true, sino false
es_alfanumerico = cadena1.isalpha()#si es alfanumerico true, si no false, tener en cuenta que no toma los espacios
contar_coincidencias = cadena1.count("h") #contamos las coincidencias de una cadena,dentro de otra cadena, devuelve la cantidad de coincidencias si no encuentra coloca =0
contar_caracteres = len(cadena1) #cunta cuantos caracteres hay en una cadena se usa de manera diferente ya que es una funcion ej: len(cadena1) ejmplo: 14 cuenta los espacios
empieza_con = cadena1.startswith("h")#verificamos que una cadena empieza con otra cadena dad, si es asi devuelve true
termina_con = cadena1.endswith("o")#verificamos que una cadena termina con otra cadena dada, si es asi devuelve true
cadena_nueva = cadena1.replace("hola","Holu")#si el valor 1 "hola" se encuentra en la cadena original,remmplaza el valor 1 de la misma, por el valor 2 "holu" siempre que tenga una coincidencia si no devuelve el mismo valor "hola", "holu" ok. "Hola", "holu" error
cadena_separada = cadena1.split(",")#separar cadenas con la cadena que le pasemos, en el ejemplo pedimos que las separe por , crera una lista

print(cadena_separada)


