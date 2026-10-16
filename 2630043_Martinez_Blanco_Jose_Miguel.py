# Jose Miguel Martinez Blanco, 2630043, Ingenieria Mecatrinica 3 I--3

"""Un string en python es un dato tipo texto, que vienen siendo una secuencia de datos 
que son inmutables, o sea, no pueden modificarse en si. Si se quieren modificar se necesitaria
metodos.
Se pueden operar y manipular los strings: Concatenacion '+' permiete unir cadenas de texto y con len() 
podemos saber la cantidad de caracters que tiene un string, el slizing permite cortar listas y aislar strings.
La importancia de verificar recae en que es necesario estandarizar en ciertas ocaciones para poder
evitar que tengamos errores inesperados, mejorar la estetcica del codigo, etc"""

# Problem number.- 1: Full name formartter (name + initials)
""" Dado el nombre completo de una persona en una sola cadena (por ejemplo: jose mmiguel martinez blanco)
el programa debe:
1) Normalizar el texto (strip , espacios extra, mayusculas/minusculas)
2) Mostrar el nombre formateado en title Case y las iniciales 
""" 
# Entradas:
""" - full_name (string; nombre completo, pede venir en mayusculas, minusculas o mezclado, con 
espacios extra).
"""

# Salidas:
"""
Formatted name: (Name In Tile Case)
Initials: (X.X.X)
"""

#Validaciones:
"""
- full_name no debe de estar vacio despues de strip()
- Debe contener almenos dos palabaras (nombre y apellido)
- Noo aceptar cadenas que sean solo espacios
"""

# Ejercicio 1: Formato de nombre completo e iniciales
full_name = " jose miguel martinez blanco   "

full_name = full_name.strip()

if full_name == "":
    print("Error: El nombre no puede estar vacío.")

else:
    words = full_name.split()
    
    if len(words) < 2:
        print("Error: Debe contener al menos un nombre y un apellido.")
    
    else:
        formatted_name = full_name.title()
        
        initial_list = []
        for initial in words:
            initial_list.append(initial[0].upper())
        
        initials = ".".join(initial_list) + "."
        
        print("Formatted name:", formatted_name)
        print("Initials:", initials)

# 1. Normalizo el texto quitando espacios extra con el metodo .strip()
# 2. Valido verificando que no esté vacío el string
# 3. Separo las palabras para contar cuántas son .split()
# 4. Validamos ya que debe contener al menos dos palabras
# 5. Muestro el nombre formateado en Title Case .title()
# 6. Saco las iniciales con un ciclo sencillito

# Problem number.- 2: Simple email validator
""" Valida si una direccion de correo tienen un formato basico correcto:
- Contienen exactamente un @
- Despues de @ debe de haber almenos un .
- No contiene espacios en blanco.
si el correo es valido , tambien muestrab el dominio 

"""

# Entradas:
""" - email_text (string)
"""

# Salidas:
"""
valid email: true o valid email: flase
si es valido: dominian: dominian_part 
"""

#Validaciones:
"""
- email_text no vacio tras strip()
- contar cuantas veces aparece @
- Verificar que no haya espacios 
"""

# Ejercicio 2: Validador simple de correo electrónico
email_text = "  correo.ejemplo@gmail.com  "

email_text = email_text.strip()

if email_text == "":
    print("validcion de email: no validado")
    print("Error: El correo está vacío.")
else:
    
    have_spaces = False
    for caracter in email_text:
        if caracter == " ":
            have_spaces = True

    if tiene_espacios:
        print("valid email: false")
    else:
        
        contador_arroba = email_text.count("@")
        
        if contador_arroba != 1:
            print("valid email: false")
        else:
            
            pos_arroba = email_text.find("@")
            dominian_part = email_text[pos_arroba + 1:]
            
            if "." in dominian_part and len(dominian_part) > 0:
                print("valid email: true")
                print("dominian:", dominian_part)
            else:
                print("valid email: false")

# 1. Quito los espacios de los extremos
# 2. Validación de no vacío
# 3. Verificamos que no contenga espacios en blanco adentro
# 4. Contamos cuántas veces aparece el '@'
# 5. Encontramos la posición del '@' para revisar el dominio
# 6. Verificamos que después del '@' haya al menos un punto

# Problem number.- 3: Palindrome checker (ignoring spaces and case) 
""" Determina si una frase es un palindromo, es decir, se lee igual de izquierda a derecha y de 
derecha a izquierda, ignorando espacios y mayusculas/minusculas.
""" 
# Entradas:
""" phrase (string)
"""

# Salidas:
"""
Is a palindrome: true o is palindrome: false
"""

#Validaciones:
"""
- phrase no vaci tras strip()
- Longitud minima razonable despues de limpiar espacios
"""
# Ejercicio 3: Verificador de palíndromos
phrase = "Anita lava la tina  "

phrase = phrase.strip()

if len(phrase) < 3:
    print("Is a palindrome: false")
else:

    phrase_clean = ""
    for leter in phrase:
        if leter != " ":
            phrase_clean = phrase_clean + leter.lower()
            
    phrase_invertida = phrase_clean[::-1]
    
    if phrase_clean == phrase_invertida:
        print("Is a palindrome: true")
    else:
        print("Is a palindrome: false")

# 1. Limpiamos los espacios de losextremos
# 2. Validaamos la longitud mínima razonable
# 3. Quitamos los espacios internos y pasamos todo a minúsculas
# 4. Invertimos la cadena limpia para comparar
# 5. Condiciónamos para saber si es un palíndromo


# Problem number.- 4: Sentence word stats (lengths and first/las word)

""" dada una oracion, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final)
2) Separar las palabras por esapcios.
3) Mostrar:
- Numero total de palabras 
- Primera palabra
- Ultima palabra
- Palabra mas corta y mas larga (por longitud) 
""" 
# Entradas:
""" sentences (string)
"""

# Salidas:
"""
- Word count: n
- First word: 
- Last word
- shortest word:
- Longest word:
"""

#Validaciones:
"""
- Oracion no vacia tras strip()
- Debe contener al menos una palabrav valida despues del split()
"""
# Ejercicio 4: Estadísticas de palabras en una oración
sentences = "  el perro corre por el campo verde  "

sentences = sentences.strip()

if sentences == " ":
    print("Error: La oración está vacía.")
else:
    
    words = sentences.split()
    
    if len(words) == 0:
        print("Error: No hay palabras válidas.")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        
        shortest = words[0]
        longest = words[0]
        
        for word in words:
            if len(word) < len(shortest):
                shortest = word
            if len(word) > len(longest):
                longest = word
                
        print("- Word count:", word_count)
        print("- First word:", first_word)
        print("- Last word:", last_word)
        print("- shortest word:", shortest)
        print("- Longest word:", longest)

# 1. Normalizamos espacios al principio y final
# 3. Validamos que no este vacío
# 4. Separamos las palabras por espacios
# 5. Encontramos la palabra más corta y más larga usando condicionales
# 6. Mostramos resultados




# Problem number.- 5: Pasword strength classifier
"""
Clasifica una contraseña como (weak), (medium) o (strong) segun reglas minimas
weak: longitud menor que 8, todo en minuscula o muy simple
medium: longitud mayor o igual a 8 yy mezcla de mayusculas con minusculas o diditos
strong: longitud mayor a 8 y contienen al menos:
-una mayuscula
- una letra minuscula
- un digito
- un simbolo mo malfanumerico

""" 
# Entradas:
""" password_input (string)
"""

# Salidas:
"""
password strength: weak
password strength: medium
password strength: strong
"""

#Validaciones:
"""
- no aceptar contraseña vacia
- verificar longitud con len()
"""
# Ejercicio 5: Clasificador de seguridad de contraseñas
password_input = "Abc123!_#"

password_input = password_input.strip()

if password_input == "":
    print("Error: La contraseña no puede estar vacía.")
else:
    longitud = len(password_input)
    
    tiene_mayus = False
    tiene_minus = False
    tiene_digito = False
    tiene_simbolo = False
    
    for x in password_input:
        if x.isupper():
            tiene_mayus = True
        elif x.islower():
            tiene_minus = True
        elif x.isdigit():
            tiene_digito = True
        else:
            tiene_simbolo = True
            
    if longitud > 8 and tiene_mayus and tiene_minus and tiene_digito and tiene_simbolo:
        print("password strength: strong")
    elif longitud >= 8 and ((tiene_mayus and tiene_minus) or tiene_digito):
        print("password strength: medium")
    else:
        print("password strength: weak")

# eliminamos los espacios de los extremos con .strip() 
# Validación: no aceptar contraseña vacía
# Evaluamos las reglas con condicionales anidados / combinados

# Problem number.- 6: Product label formatter
""" 
Dado el nombre de un producto y su precio, genera una etiquera en una sola lina con el siguiente
formato:
Product: Name Price: $Price

La cadena completa debe de tener exactamente 30 caracteres:
- Si es mas larga, recorta hasta 30 caracterees.
- Si es mas cortas , rellena con espacios al final
""" 
# Entradas:
""" 
- product_na,e (string)
- price_value (como string o numero, preferilemente en string para mostrarlo)
"""

# Salidas:
"""
- Label: exactly 30 caracters
"""

#Validaciones:
"""
- product_name no vacio tras strip(.
-price_value debe poder convertirse a un numero positivo
"""
# Ejercicio 6: Formateador de etiqueta de producto
product_name = "Camisa de algodon"
price_value = "299.99"

product_name = product_name.strip()

if product_name == "":
    print("Error: El nombre del producto no puede estar vacío.")
else:

    es_valido_precio = True
    try:
        numero_precio = float(price_value)
        if numero_precio < 0:
            es_valido_precio = False
    except:
        es_valido_precio = False
        
    if not es_valido_precio:
        print("Error: El precio debe ser un número positivo.")
    else:
        
        etiqueta = "Product: " + product_name + " Price: $" + str(price_value)
        
        if len(etiqueta) > 30:
            etiqueta = etiqueta[:30]
        elif len(etiqueta) < 30:
            faltantes = 30 - len(etiqueta)
            etiqueta = etiqueta + (" " * faltantes)
            
        print("Label:", etiqueta)
        print("(Longitud exacta:", len(etiqueta), "caracteres)")

# eliminamos espacios con .strip()
# Validamos que el nombre no este vacío
# Validamos que el precio debe poder convertirse a un número positivo
# Armams la etiqueta base
# Ajustams exactamente a 30 caracteres




# Conclusion

"""Estandarizamos los strings para trabajar de una manera mas facil, ya que asi podemos aplicarle variosmetodos 
a estos mismos sin tener que aplicarle otros de por medio. Asi nos aseguramos de tener un codigo as limpio
y facil de escribir y entender"""

# Referencias 
[1] https://ellibrodepython.com/operadores-logicos
[2] https://ellibrodepython.com/excepciones-try-except-finally
[3] https://www.w3schools.com/PYTHON/python_try_except.asp

# Repositorio en GitHub