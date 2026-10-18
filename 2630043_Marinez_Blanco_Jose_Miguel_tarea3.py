# 2630043 Martínez Blanco Jose Miguel- Ingenieria Mecatronica grupo 3


"""
Una lista, se podria decir que es una coleccion ordenada y mutable de elementos 
que pueden añadirse, eliminarse o modificarse después de que se halla creado, 
y se conservan tanto el orden como los elementos duplicados.
Por ejemplo, una lista de la compra. 

Una tupla también es ordenada, pero a diferencia de la lista, la tupla es inmutable, 
osea, que una vez creada, sus elementos no se pueden modificar, lo que la hace
adecuada para datos que sean fijos, como coordenadas o fechas. 

Un diccionario (*dict*) almacena elementos pares (clave-valor) y permite una 
búsqueda rápida de un valor a partir de su clave única. 
Por ejemplo, asociar el nombre de un producto con su precio).

El hecho de ser 'mutable' significa que una lista puede modificarse directamente 
(añadiendo o eliminando elementos, ordenarlos, etc.), sin necesidad de crear un 
objeto nuevo. 

Por el contrario, al ser 'inmutable', cualquier 'modificación' en 
una tupla requiere realmente la creación de una tupla completamente nueva. 

Los diccionarios lo que hacen es asociar cada clave con un valor, lo que permite 
recuperar los datos directamente mediante su nombre o identificador, en lugar de 
tener que realizar una búsqueda a lo largo de una secuencia.

Een este documento se abordarán seis problemas sencillos, cada uno incluye una 
descripción, sus entradas y salidas, las validaciones aplicadas a los datos de 
entrada, y ejemplos de cómo utilizar listas, tuplas y diccionarios en contextos 
prácticos, tales como catálogos, registros o estadísticas básicas.
"""

# Exercises

# Problem 1: Shopping list basics (list operations)

#Description: 
"""
Works with a list of product names (strings). Builds an
initial list from a comma-separated string, appends a new product,
reports the total number of items, and checks whether a given product
is present in the list.
"""

# Inputs:
# - initial_items_text (string; e.g. "apple,banana,orange")
# - new_item (string; product to add)
# - search_item (string; product to search for)

# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false

# Validations:
# - initial_items_text must not be empty after strip().
# - The string is split on commas and each element is stripped of extra
#   spaces.
# - new_item and search_item must not be empty.

# Test cases:
# 1) Normal: initial_items_text="apple,banana,orange", new_item="grape",
#    search_item="banana" -> Found item: true
# 2) Border: initial_items_text="apple", new_item="banana",
#    search_item="banana" -> Found item: true (search_item == new_item,
#    only present after being added)
# 3) Error: initial_items_text="" -> Error: invalid input


print("Problem 1: Shopping list basics \n")

initial_items_text = "apple,banana,orange"
new_item = "grape"
search_item = "banana"

if initial_items_text.strip() == "" or new_item.strip() == "" or search_item.strip() == "":
    print("Error: invalid input")
else:
    
    raw_items = initial_items_text.split(",")

    items_list = []
    for raw_item in raw_items:
        clean_item = raw_item.strip()
        if clean_item != "":
            items_list.append(clean_item)


    items_list.append(new_item.strip())

    total_items = len(items_list)


    is_in_list = False
    if search_item.strip() in items_list:
        is_in_list = True

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", is_in_list)

# split the text by commas to start building the list
# add the new product at the end of the list
# check if the search_item is inside the list


# Problem 2: Points and distances with tuples
# Description: 
"""
Uses tuples to represent two points in a 2D plane,
(x1, y1) and (x2, y2). 
Computes the Euclidean distance between the two
points and builds a new tuple with their midpoint.
"""

# Inputs:
# - x1, y1, x2, y2 (float; point coordinates)


# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)

# Validations:
# - All four inputs must be convertible to float.
# - No additional range restrictions are required.

# Test cases:
# 1: Normal: x1=0, y1=0, x2=3, y2=4 -> Distance: 5.0, Midpoint: (1.5, 2.0)
# 2: Border: x1=2, y1=2, x2=2, y2=2 -> Distance: 0.0 (same point)
# 3: Error: x1="abc" -> Error: invalid input


print("\n Problem 2: Points and distances with tuples")

x1_text = "0"
y1_text = "0"
x2_text = "3"
y2_text = "4"

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)

    
    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
except ValueError:
    print("Error: invalid input")


# tuples because a point should not change after it is created


# Problem 3: Product catalog with dictionary
# Description: Manages a small product catalog as a dict where the key is
#   the product name (string) and the value is the unit price (float).
#   Reads a product name and a quantity, and computes the total price to
#   pay if the product exists.

# Inputs:
# - product_name (string)
# - quantity (int; amount to buy)

# Outputs:
# - If the product exists:
#   - "Unit price:" <unit_price>
#   - "Quantity:" <quantity>
#   - "Total:" <total_price>
# - If the product does not exist:
#   - "Error: product not found"

# Validations:
# - quantity must be > 0.
# - product_name must not be empty after strip().
# - Check whether product_name exists as a key in the dictionary.

# Test cases:
# 1) Normal: product_name="apple", quantity=3 -> Total: 30.0 (apple=10.0)
# 2) Border: product_name="banana", quantity=1 -> Total: equal to unit price
# 3) Error: product_name="mango", quantity=2 -> Error: product not found

print("\n Problem 3: Product catalog with dictionary")

product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0,
}

product_name = "apple"
quantity_text = "3"

if product_name.strip() == "":
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_text)

        if quantity <= 0:
            print("Error: invalid input")
        else:
            product_name = product_name.strip()

            if product_name in product_prices:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity

                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
            else:
                print("Error: product not found")
    except ValueError:
        print("Error: invalid input")


# Problem 4: Student grades with dict and list
# Description: Manages a group's grades as a dict where the key is the
# student name (string) and the value is a list of grades (list of
# float). Computes the average grade for a given student and whether
# they passed (average >= 70.0).

# Inputs:
# - student_name (string)

# Outputs:
# - If the student exists:
#   - "Grades:" <grades_list>
#   - "Average:" <average>
#   - "Passed:" true|false
# - If the student does not exist:
#   - "Error: student not found"

# Validations:
# - student_name must not be empty after strip().
# - Check whether student_name is a key in the dictionary.
# - Check that the grades list is not empty before computing the average.

# Test cases:
# 1) Normal: student_name="Alice" (grades=[90, 85]) -> Average: 87.5,
#    Passed: true
# 2) Border: student_name="Carol" (grades=[70.0]) -> Average: 70.0,
#    Passed: true (average exactly at the passing threshold)
# 3) Error: student_name="Dave" -> Error: student not found


print("\n Problem 4: Student grades with dict and list")

grades = {
    "Alice": [90.0, 85.0],
    "Bob": [60.0, 65.0, 70.0],
    "Carol": [70.0],
}

student_name = "Alice"

if student_name.strip() == "":
    print("Error: invalid input")
else:
    student_name = student_name.strip()

    if student_name in grades:
        grades_list = grades[student_name]

        if len(grades_list) == 0:
            print("Error: invalid input")
        else:
            
            grades_sum = 0
            for grade in grades_list:
                grades_sum = grades_sum + grade

            average = grades_sum / len(grades_list)

            is_passed = False
            if average >= 70.0:
                is_passed = True

            print("Grades:", grades_list)
            print("Average:", round(average, 2))
            print("Passed:", is_passed)
    else:
        print("Error: student not found")

# add up all the grades manually with a loop

# Problem 5: Word frequency counter (list + dict)
# Description: Counts the frequency of each word in a sentence. Converts
# the sentence to lowercase, splits it into a list of words, builds a
# frequency dictionary, and reports the full dictionary plus the most
# common word.

# Inputs:
# - sentence (string)

# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>

# Validations:
# - sentence must not be empty after strip().
# - Simple punctuation is removed before splitting (documented decision:
#   periods, commas, exclamation and question marks are stripped using
#   replace()).
# - Check that the resulting words list is not empty.

# Test cases:
# 1) Normal: sentence="the cat sat on the mat" -> Most common word: "the"
# 2) Border: sentence="hello" -> Frequencies: {"hello": 1}
# 3) Error: sentence="   " -> Error: invalid input


print("\n Problem 5: Word frequency counter")

sentence = "the cat sat on the mat"

if sentence.strip() == "":
    print("Error: invalid input")
else:
    cleaned_sentence = sentence.lower()
    cleaned_sentence = cleaned_sentence.replace(".", "")
    cleaned_sentence = cleaned_sentence.replace(",", "")
    cleaned_sentence = cleaned_sentence.replace("!", "")
    cleaned_sentence = cleaned_sentence.replace("?", "")

    raw_words = cleaned_sentence.split()

    words_list = []
    for raw_word in raw_words:
        if raw_word != "":
            words_list.append(raw_word)

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1


        most_common_word = words_list[0]
        highest_count = freq_dict[most_common_word]
        for word in freq_dict:
            if freq_dict[word] > highest_count:
                most_common_word = word
                highest_count = freq_dict[word]

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)

# walk through the dictionary to find the most common word


# Problem 6: Simple contact book (dictionary CRUD)
# Description: Implements a mini contact book as a dict where the key is
#   the contact name (string) and the value is the phone number (string).
#   Supports three actions: ADD (add or update a contact), SEARCH (look up
#   a phone number) and DELETE (remove a contact).

# Inputs:
# - action_text (string; "ADD", "SEARCH" or "DELETE")
# - name (string; required for all actions)
# - phone (string; required only for "ADD")

# Outputs:
# - For "ADD": "Contact saved:" name, phone
# - For "SEARCH":
#   - If found: "Phone:" <phone>
#   - If not found: "Error: contact not found"
# - For "DELETE":
#   - If found: "Contact deleted:" name
#   - If not found: "Error: contact not found"

# Validations:
# - action_text is normalized to uppercase.
# - action_text must be one of "ADD", "SEARCH", "DELETE".
# - name must not be empty after strip().
# - For "ADD", phone must not be empty after strip().

# Test cases:
# 1) Normal: action_text="ADD", name="Dave", phone="5551234" -> Contact
#    saved: Dave 5551234
# 2) Border: action_text="search", name="Alice" (already in contacts) ->
#    Phone: 1234567890 (lower-case action is normalized to "SEARCH")
# 3) Error: action_text="SEARCH", name="Zoe" (not in contacts) -> Error:
#    contact not found


print("\n Problem 6: Simple contact book")

contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210",
}

action_text = "ADD"
name = "Dave"
phone = "5551234"

action_text = action_text.strip().upper()

if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid input")
elif name.strip() == "":
    print("Error: invalid input")
else:
    name = name.strip()

    if action_text == "ADD":
        if phone.strip() == "":
            print("Error: invalid input")
        else:
            phone = phone.strip()
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")

action_text = "search"
name = "Alice"

action_text = action_text.strip().upper()

if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid input")
elif name.strip() == "":
    print("Error: invalid input")
else:
    name = name.strip()

    if action_text == "ADD":
        if phone.strip() == "":
            print("Error: invalid input")
        else:
            phone = phone.strip()
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")

action_text = "SEARCH"
name = "Zoe"

action_text = action_text.strip().upper()

if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid input")
elif name.strip() == "":
    print("Error: invalid input")
else:
    name = name.strip()

    if action_text == "ADD":
        if phone.strip() == "":
            print("Error: invalid input")
        else:
            phone = phone.strip()
            contacts[name] = phone
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")

# we run the three actions one after another to show all three cases,
# just like the test cases above


# CONCLUSIONS

"""
Las listas son la opción adecuada cuando el número de elementos o su orden 
puedencambiar con el tiempo; por ejemplo, una lista de la compra que crece 
a medida que se añaden artículos.
Sus métodos (append, remove, pop, sort) facilitan mantener estos datos
flexibles y actualizados. 

Las tuplas, por el contrario, resultan útiles precisamente porque son inmutables:
las coordenadas o los registros fijos son más seguros cuando nada puede modificarlos 
accidentalmente tras su creación. 

Los diccionarios destacan cuando es necesario recuperar datos mediante una clave 
significativa en lugar de un índice numérico;
por ejemplo, al buscar un precio a partir del nombre de un producto o un número de teléfono
a partir del nombre de un contacto, lo que evita tener que recorrer toda una lista. 

Un patrón recurrente y muy útil para abordar este tipo de situaciones consiste en combinar 
estructuras —como un diccionario cuyos valores son listas (nombre del estudiante -> lista de calificaciones),
lo que permite que cada clave contenga varios datos relacionados, manteniendo al mismo tiempo
la capacidad de realizar búsquedas rápidas mediante dicha clave.
"""

# References:
"""
[1] Listas: https://ellibrodepython.com/listas-en-python
[2] Tuplas: https://ellibrodepython.com/tuplas-python
[3] Diccionarios: https://ellibrodepython.com/diccionarios-en-python
[4] Diccionarios:https://www.datacamp.com/es/tutorial/python-dictionary-methods
[5]diccionarios: https://docs.python.org/es/3.6/tutorial/datastructures.html#dictionaries
"""

#Repository for GitHub