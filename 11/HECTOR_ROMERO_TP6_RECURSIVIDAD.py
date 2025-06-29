#Ejercicio 1
#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
limite = int(input("Ingresa un número entero positivo: "))      # Solicitar un número al usuario
if limite < 1:                                                  # Verificar que sea un número válido
    print("Por favor ingresa un número mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {limite}:")
    for i in range(1, limite + 1):
        print(f"{i}! = {factorial(i)}")
    
print(" ") 
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")



#Ejercicio 2
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

print(" ") 
print(" ")
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  

#Programa principal
limite = int(input("Ingresa un número entero positivo para la serie de Fibonacci: "))  # Solicitar un número al usuario
if limite < 0:  # Verificar que sea un número válido
    print("Por favor ingresa un número mayor o igual a 0.")     
else:
    print(f"Serie de Fibonacci hasta la posición {limite}:")
    for i in range(limite + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")   
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#Ejercicio 3
#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
#utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Ingresa la base: "))  # Solicitar la base al usuario
exponente = int(input("Ingresa el exponente: "))  # Solicitar el exponente al usuario
if exponente < 0:
    print("Por favor ingresa un exponente mayor o igual a 0.")  
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")
print(" ")
print("  ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


#Ejercicio 4
#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
numero = int(input("Ingresa un número entero positivo: "))
if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
elif numero == 0:
    print("0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"{numero} en binario es: {binario}")
print(" ")
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


#Ejercicio 5
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:               #Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
        return True
    if palabra[0] != palabra[-1]:       #Comparar primera y última letra
        return False
    return es_palindromo(palabra[1:-1]) # Llamada recursiva sin la primera y última letra

#Programa principal
palabra = input("Ingresa una palabra sin espacios ni tildes: ").lower()

print(es_palindromo(palabra))  # Mostrar solo True o False
print(" ")
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#Ejercicio 6
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n == 0:            # Caso base: si n es 0, no queda nada por sumar
        return 0
    # Paso recursivo: último dígito + suma de los dígitos del resto del número
    return (n % 10) + suma_digitos(n // 10)

# Programa principal
numero = int(input("Ingresa un número entero positivo: "))
if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")    
print(" ")
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#Ejercicio 7
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca nbloques, 
#en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel 
#con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número 
# de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir
#toda la pirámide.
def contar_bloques(n):
    
    if n <= 0:                          #Caso base: si n es 0 o negativo, no hay bloques
        return 0
    return n + contar_bloques(n - 1)    #Paso recursivo: nivel actual + bloques de los niveles inferiores

#programa  principal
nivel_bloques = int(input("Ingresa el número de bloques en el nivel más bajo: "))
if nivel_bloques < 1:                  #Verificar que sea un número válido
    print("Por favor, ingresa un número entero positivo mayor o igual a 1.")
else:
    total_bloques = contar_bloques(nivel_bloques)
    print(f"Total de bloques necesarios para la pirámide: {total_bloques}")
print(" ")
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:                  #Caso base: si ya no quedan dígitos por analizar
        return 0
    ultimo = numero % 10            #Extraemos el último dígito usando módulo
    if ultimo == digito:            # Comprobamos si coincide con el dígito buscado
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

#Programa principal
n = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese el dígito a contar (0–9): "))
if n < 0 or d < 0 or d > 9:
    print("Ingresos no válidos. Asegúrese de que número sea positivo y dígito entre 0 y 9.")
else:
    veces = contar_digito(n, d)
    print(f"El dígito {d} aparece {veces} veces en {n}.")

print(" ")
print(" ")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

