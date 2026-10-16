# José Miguel Martínez Blanco.
# Matricula: 2630043
# Grupo: Ingenieria mecatronica 3, primer cuatrimestre.




# Resumen ejecutivo.

""" Los tipos `int` y `float` en Python representan a los números enteros y números de
punto flotante.La principal diferencia que hay entre estos dos es que los `float`
manejan decimales. 

Un valor booleano representa `True` (verdadero) o `False`
(falso), que se obtienen mediante comparaciones.

La validacion de rangos y evitar la división
por cero es fundamental, ya que asi prevenimos los fallos en la ejecución del codigo. 

Este archivo abordara seis problemas de practicaa que implementan entradas de datos,
validaciones, conversiones y toma de decisiones condicionales.
"""

# Problema 1: Conversor de temperatura e indicador de rango

# Descripción: Convierte una temperatura de Celsius a Fahrenheit y Kelvin.
# Determina si se trata de una temperatura alta (>= 30.0) mediante un indicador booleano.
# Entradas: temp_c (float)
# Salidas: Fahrenheit, Kelvin, indicador de temperatura alta
# Validaciones: Verificar la conversión y asegurar que el valor en Kelvin no sea físicamente imposible (< 0.0)
# Casos de prueba:
#   1) Normal: 25.5
#   2) Límite: 30.0
#   3) Error: -300.0 (Kelvin inferior a 0)

print("Temperature Converter")
raw_temp_c = input("Enter temperature in Celsius: ")
is_valid_temp = True
try:
    temp_c = float(raw_temp_c)
except ValueError:
    is_valid_temp = False

if not is_valid_temp:
    print("Error: invalid input")
else:
    
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    
    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = (temp_c >= 30.0)
        
        high_temp_str = "true" if is_high_temperature else "false"
        
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", high_temp_str)
print("")

# Validación: Comprobamos si la entrada se puede convertir a float
# Cálculos para convertir a kelvin y farenheit
# Validamos la imposibilidad física en Kelvin
# Formateamos la salida booleana en minúsculas



# Problema 2: Horas de trabajo y pago de horas extra
# Descripción: Calcula la remuneración semanal. Hasta 40 horas a la tarifa normal.
# las horas adicionales (> 40) se pagan al 150 % de la tarifa. Genera un valor booleano `has_overtime`.
# Entradas: `hours_worked` (número de punto flotante), `hourly_rate` (número de punto flotante)
# Salidas: Pago regular, pago por horas extra, pago total, indicador de horas extra (`has_overtime`)
# Validaciones: `hours_worked` >= 0, `hourly_rate` > 0
# Casos de prueba:
#   1) Normal: `hours_worked` = 45.0, `hourly_rate` = 100.0
#   2) Límite: `hours_worked` = 40.0, `hourly_rate` = 150.0
#   3) Error: `hours_worked` = -5.0, `hourly_rate` = 200.0

print("Problem 2: Work Hours and Overtime")

raw_hours = input("Enter hours worked: ")
raw_rate = input("Enter hourly rate: ")

is_valid_p2 = True
try:
    hours_worked = float(raw_hours)
    hourly_rate = float(raw_rate)
except ValueError:
    is_valid_p2 = False
if not is_valid_p2:
    print("Error: invalid input")
else:
    if hours_worked < 0.0 or hourly_rate <= 0.0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(0.0, hours_worked - 40.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40.0)
        overtime_flag_str = "true" if has_overtime else "false"
        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", overtime_flag_str)

print("")

# Validamos los rangos.




# Problema 3: 
"Elegibilidad para descuentos mediante valores booleanos"

# Descripción: Determina si corresponde aplicar un descuento a una compra basándose en si el comprador es estudiante, 
# es una persona mayor, o si el total de la compra es >= 1000.0. Se aplica un descuento del 10 % si se cumplen las condiciones.
# Entradas: purchase_total (float), is_student_text (str), is_senior_text (str)
# Salidas: Indicador de elegibilidad para el descuento, total final
# Validaciones: purchase_total >= 0.0; los valores de texto deben ser "YES" o "NO"
# Casos de prueba:
#   1) Normal: purchase = 500.0, student = "YES", senior = "NO"
#   2) Límite: purchase = 1000.0, student = "NO", senior = "NO"
#   3) Error: purchase = 200.0, student = "MAYBE", senior = "NO"

print("Problem 3: Discount Eligibility")

raw_purchase = input("Enter purchase total: ")
is_student_text = input("Is student? (YES/NO): ")
is_senior_text = input("Is senior? (YES/NO): ")

is_valid_p3 = True
try:
    purchase_total = float(raw_purchase)
except ValueError:
    is_valid_p3 = False

if not is_valid_p3:
    print("Error: invalid input")
else:
    if purchase_total < 0.0:
        print("Error: invalid input")
    else:

        clean_student = is_student_text.strip().upper()
        clean_senior = is_senior_text.strip().upper()
        
        if (clean_student != "YES" and clean_student != "NO") or (clean_senior != "YES" and clean_senior != "NO"):
            print("Error: invalid input")
        else:
            is_student = (clean_student == "YES")
            is_senior = (clean_senior == "YES")
            
            discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
            
            if discount_eligible:
                final_total = purchase_total * 0.9
            else:
                final_total = purchase_total
                
            eligible_str = "true" if discount_eligible else "false"
            
            print("Discount eligible:", eligible_str)
            print("Final total:", final_total)

print("")

# Normalizamoslaentrada de texto


"Problema 4: Estadísticas básicas de tres números enteros"
# Descripción: Lee tres números enteros y calcula la suma, el promedio, el máximo, el mínimo
# y un indicador booleano que señala si todos los números son pares.
# Entradas: n1 (int), n2 (int), n3 (int)
# Salidas: Suma, promedio, máximo, mínimo, indicador de si todos son pares
# Validaciones: Los valores deben poder convertirse correctamente a números enteros (int)
# Casos de prueba:
#   1) Normal: 4, 8, 12
#   2) Límite: 0, 0, 0
#   3) Error: 5, "abc", 10

print("=== Problem 4: Basic Statistics ===")
raw_n1 = input("Enter first integer: ")
raw_n2 = input("Enter second integer: ")
raw_n3 = input("Enter third integer: ")

is_valid_p4 = True
try:
    n1 = int(raw_n1)
    n2 = int(raw_n2)
    n3 = int(raw_n3)
except ValueError:
    is_valid_p4 = False

if not is_valid_p4:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    all_even_str = "true" if all_even else "false"
    
    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even_str)

print("\n.")

"Problema 5: Elegibilidad para un préstamo (ingresos y ratio de endeudamiento)"

# Descripción: Evalúa la elegibilidad para un préstamo basándose en los ingresos mensuales,
# la deuda mensual y la puntuación crediticia, utilizando un umbral de ratio de endeudamiento
# y requisitos de puntuación.
# Entradas: monthly_income (float), monthly_debt (float), credit_score (int)
# Salidas: Ratio de endeudamiento, indicador de elegibilidad
# Validaciones: monthly_income > 0.0 (evita la división por cero), debt >= 0, score >= 0
# Casos de prueba:
#   1) Normal: income = 10000.0, debt = 2000.0, score = 700
#   2) Límite: income = 8000.0, debt = 3200.0, score = 650
#   3) Error: income = 0.0, debt = 500.0, score = 700

print("Problem 5: Loan Eligibility")
raw_income = input("Enter monthly income: ")
raw_debt = input("Enter monthly debt: ")
raw_score = input("Enter credit score: ")

is_valid_p5 = True
try:
    monthly_income = float(raw_income)
    monthly_debt = float(raw_debt)
    credit_score = int(raw_score)
except ValueError:
    is_valid_p5 = False

if not is_valid_p5:
    print("Error: invalid input")
else:

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
        
        eligible_str = "true" if eligible else "false"
        
        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible_str)

print("\n.")

# Validamos si income > 0.0 evita la división por cero


# Problema 6: Índice de Masa Corporal (IMC) e indicadores de categoría
# Descripción: Calcula el IMC y evalúa indicadores booleanos de categoría (bajo peso,
# peso normal, sobrepeso).
# Entradas: weight_kg (float), height_m (float)
# Salidas: IMC redondeado, indicador de bajo peso, indicador de peso normal, indicador de sobrepeso
# Validaciones: weight_kg > 0.0, height_m > 0.0
# Casos de prueba:
#   1) Normal: weight = 70.0, height = 1.75
#   2) Límite: weight = 56.875, height = 1.75 (límite exacto para peso normal en 18.5)
#   3) Error: weight = -70.0, height = 1.75


print("Problem 6: Body Mass Index (BMI)")
raw_weight = input("Enter weight in kg: ")
raw_height = input("Enter height in meters: ")

is_valid_p6 = True
try:
    weight_kg = float(raw_weight)
    height_m = float(raw_height)
except ValueError:
    is_valid_p6 = False

if not is_valid_p6:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        rounded_bmi = round(bmi, 2)
        
        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)
        
        underweight_str = "true" if is_underweight else "false"
        normal_str = "true" if is_normal else "false"
        overweight_str = "true" if is_overweight else "false"
        
        print("BMI:", rounded_bmi)
        print("Underweight:", underweight_str)
        print("Normal:", normal_str)
        print("Overweight:", overweight_str)



# Conclusion

"""Los números enteros y los flotantes funcionan en perfecta armonía o vaya complemntandose entre si
para realizar cálculos mas precisos acoplandos a los del mundo real.
Las comparaciones que nosotros hacemos, generan valores booleanos que permiten tomar decisiones dinámicas mediante condicionales.
Validar rangos numéricos y divisores evita que cometamos errores de ejecución y lógica incorrecta.
Combinar condiciones con operadores como 'and', 'or' y 'not' permite gestionar reglas de negocio complejas,
estos patrones de programación constituyen la base de los sistemas de nóminas, descuentos y préstamos."""




# References

" try | expect" #  https://www.w3schools.com/PYTHON/python_try_except.asp
"and |  or | not" # https://ellibrodepython.com/operadores-logicos
"numero flotantes" # https://ellibrodepython.com/float-python
"numeros enteros" # https://ellibrodepython.com/entero-en-python
" operadores matematicos" # https://ellibrodepython.com/operadores-python

# Repositorio de GitHub