#Ejercicio !
#Dado el diccionario de precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#agregar: Naranja = 1200 - Manzana = 1500 - Pera = 2300
precios_frutas = {
                "banana": 1200,
                 "Ananá": 2500,
                 "melón": 3000,
                 "uva":   1450
                }

# Agregar nuevas frutas:
precios_frutas["Naranja"]   = 1200
precios_frutas["Manzana"]   = 1500
precios_frutas["Pera"]      = 2300

print(precios_frutas)
print(" ")
print(" ")
print("###########################################################")


#Ejercicio 2
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# en el punto anterior, actualizar los precios de las siguientes frutas:
#Banana = 1330 - Manzana = 1700 - Melón = 2800
precios_frutas = {
                "banana": 1200,
                "Ananá": 2500,
                "melón": 3000,
                "uva": 1450,
                "Naranja": 1200,
                "Manzana": 1500,
                "Pera": 2300
            }

# Actualización de precios
precios_frutas.update({
                    "banana": 1330,
                    "Manzana": 1700,
                    "melón": 2800
                    })
print(precios_frutas)
print(" ")
print(" ")
print("###########################################################")


#Ejercicio 3
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
#en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas = {
                "banana": 1330,
                "Ananá": 2500,
                "melón": 2800,
                "uva": 1450,
                "Naranja": 1200,
                "Manzana": 1700,
                "Pera": 2300
                }

# Crear la lista de frutas
frutas = list(precios_frutas.keys())
print(frutas)
print(" ")
print(" ")
print("###########################################################")

#Ejercicio 4
#Escribí un programa que permita almacenar y consultar números telefónicos. Permití al usuario cargar 
#5 contactos con su nombre como clave y número como valor. Luego, pedí un nombre y mostrale el número
#asociado, si existe.
def cargar_contactos(n):
    contactos = {}
    for i in range(n):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
        numero = input(f"Ingrese el número de {nombre}: ").strip()
        contactos[nombre] = numero
    return contactos

def consultar_contacto(contactos):
    nombre = input("¿Qué nombre deseas consultar? ").strip()
    numero = contactos.get(nombre)      # Usamos .get para evitar KeyError y manejar el caso inexistente
    if numero:
        print(f"El número de {nombre} es {numero}")
    else:
        print(f"El contacto '{nombre}' no existe.")
def principal(n):
    print("=== Agenda telefónica ===")
    contactos = cargar_contactos(n)
    print("\n--- Ahora veamos si encontramos un número ---")
    consultar_contacto(contactos)

#programa principal
n = int(input("¿Cuántos contactos deseas ingresar? (máximo 5): "))
principal(n)
print(" ")
print(" ")
print("###########################################################")    


#Ejercicio 5
#Solicita al usuario una frase e imprime: Las palabras únicas (usando un set). Un diccionario 
# con la cantidad de veces que aparece cada palabra.
def analizar_frase(frase):
    palabras = frase.split()        # Dividir en palabras
    palabras_unicas = set(palabras) # 1. Conjunto de palabras únicas
    frecuencias = {}                # 2. Diccionario con frecuencia de cada palabra
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return palabras_unicas, frecuencias

def principal():
    frase = input("Ingresa una frase: ")
    uniques, freqs = analizar_frase(frase)
    
    print("\nPalabras únicas:")
    print(uniques)
    
    print("\nFrecuencia de cada palabra:")
    for palabra, conteo in freqs.items():
        print(f"'{palabra}': {conteo}")

principal()
print
print(" ")
print("###########################################################")

#Ejercicio 6
#Permití ingresar los nombre de 3 alumnos, y para cada uno una TUPLA E 3 NOTAS.
#Luego mostrá el promedo de cada alumno.
def cargar_alumnos(n):
    alumnos = {}
    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)  # Guardar las notas como una tupla
    return alumnos
def calcular_promedios(alumnos):
    promedios = {}
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        promedios[nombre] = promedio
    return promedios
def principal(n):
    print("=== Ingreso de alumnos y sus notas ===")
    alumnos = cargar_alumnos(n)
    print("\n--- Promedios de los alumnos ---")
    promedios = calcular_promedios(alumnos)
    
    for nombre, promedio in promedios.items():
        print(f"{nombre}: {promedio:.2f}")

principal(3)
print(" ")
print(" ")
print("###########################################################")


#Ejercicio 7
#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#1-Mostrá los que aprobaron ambos parciales 2-Mostrá los que aprobaron solo uno de los dos 3-Mostrá la 
# lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
def analizar_estudiantes(parcial1, parcial2):
    ambos = parcial1.intersection(parcial2)             # Estudiantes que aprobaron ambos parciales
    solo_uno = parcial1.symmetric_difference(parcial2)  # Estudiantes que aprobaron solo uno
    total_aprobados = parcial1.union(parcial2)             # Todos los estudiantes que aprobaron al menos un parcial
    return ambos, solo_uno, total_aprobados

def principal():
    parcial1 = set(input("Ingrese los estudiantes que aprobaron Parcial 1 (separados por comas): ").split(","))
    parcial2 = set(input("Ingrese los estudiantes que aprobaron Parcial 2 (separados por comas): ").split(","))
    ambos, solo_uno, total_aprobados = analizar_estudiantes(parcial1, parcial2)
    print("\nEstudiantes que aprobaron ambos parciales:")
    print(ambos)
    print("\nEstudiantes que aprobaron solo uno de los dos parciales:")
    print(solo_uno)
    print("\nLista total de estudiantes que aprobaron al menos un parcial:")
    print(total_aprobados)
principal()
print(" ")
print(" ")
print("###########################################################")


#Ejercicio 8
#Armá un diccionario donde las claves sean nombre de productos y los valores su stock.
#Permitir al ususario: 1-Consultar el estock de un prodcuto ingresado. 2-Agregar unidades al stock si el 
#producto ya existe. 3-Agregar un nuevo producto si no existe.

def cargar_productos(): #CFunción para cargar productos y stock y armar el diccionario
    productos = {}
    while True:
        nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ").strip()#.strip evita errores de espacios al principio o al final
        if nombre.lower() == 'salir': #.lower convierte el texto a minúsculas para evitar errores de mayúsculas y minúsculas
            break
        stock = int(input(f"Ingrese el stock de {nombre}: "))
        productos[nombre] = stock   #Agrega el producto y su stock al diccionario
    return productos

def consultar_producto(productos):#Para consultar el stock de un producto      
    nombre = input("Ingrese el nombre del producto a consultar: ").strip()
    stock = productos.get(nombre)#busca una clave en el diccionario. Si la encuentra, devuelve su valor. Si no la encuentra, devuelve None (en lugar de lanzar un error).
    if stock is not None: #Si el producto fue encontrado en el diccionario, si tiene un stock asociado), entonces ejecutá este bloque de código
        print(f"El stock de {nombre} es {stock}")#Escribe el stock del producto consultado
    else:
        print(f"El producto '{nombre}' no existe.")#El producto no existe

def agregar_stock(productos):#Función para agregar stock a un producto existente
    nombre = input("Ingrese el nombre del producto para agregar stock: ").strip()
    if nombre in productos:  #Si el producto existe en el diccionario
        cantidad = int(input(f"Ingrese la cantidad a agregar al stock de {nombre}: "))
        productos[nombre] += cantidad # Suma la cantidad al stock existente
        print(f"Nuevo stock de {nombre}: {productos[nombre]}")
    else:
        print(f"El producto '{nombre}' no existe.")

def menu():  #Función para mostrar el menú y manejar las opciones
    productos = {}  # Diccionario de productos
    while True:
        print("\n📋 MENÚ DE OPCIONES")
        print("1. Cargar productos")
        print("2. Consultar stock de un producto")
        print("3. Agregar stock a un producto")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
            productos.update(cargar_productos())
        elif opcion == "2":
            consultar_producto(productos)
        elif opcion == "3":
            agregar_stock(productos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
#Programa principal --  Se podría agregar una opcion para eliminar productos o para modificar el stock de un producto existente
menu()  
print(" ")
print(" ")
print("###########################################################")


#Ejercicio 9
#Crea una agenda donde las claves sean tuplas de día y hora y los valores sean eventos. 
#Permitir consultar que actividad hay en cierto día y hora.
#Ej.: ("LUnes","10:00"):"Reunion",
#Ej.: ("Martes",15:00"):"Clase de Ingles"
def cargar_agenda(): #Función para cargar actividades en la agenda
    agenda = {}
    while True:
        dia = input("Ingrese el día de la actividad (o 'salir' para terminar): ").strip()
        if dia.lower() == 'salir':
            break
        hora = input("Ingrese la hora de la actividad (formato HH:MM): ").strip()
        evento = input("Ingrese el evento: ").strip()
        agenda[(dia, hora)] = evento  # Usamos una tupla como clave
    return agenda

def consultar_evento(agenda):
    dia = input("Ingrese el día de la actividad a consultar: ").strip()
    hora = input("Ingrese la hora de la actividad a consultar (formato HH:MM): ").strip()
    evento = agenda.get((dia, hora))  # Buscamos la tupla (día, hora) en el diccionario
    if evento: # Si el evento existe, lo mostramos
        print(f"Evento en {dia} a las {hora}: {evento}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")

def menu(): #Función para mostrar el menú y manejar las opciones
    agenda = {}  # Diccionario para almacenar la agenda
    while True:
        print("\n MENÚ DE AGENDA")
        print("1. Cargar actividades")
        print("2. Consultar actividad en un día y hora")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ").strip()
        if opcion == "1":
            agenda.update(cargar_agenda())
        elif opcion == "2":
            consultar_evento(agenda)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
#Programa principal
menu()
print(" ")
print(" ")
print("###########################################################")
  

#Ejercicio 10
#Dado un diccionario que mapea nombres de paises con sus capitales, construir un 
#nuevo diccionarios que: 1-Las CAPITALES sean las claves. 2-Los PAISES sean los valores.
#Ejm.: original: {'Argentina': 'Buenos Aires', 'Chile': 'Santiago'}
#Ejm.: nuevo: {'Buenos Aires': 'Argentina', 'Santiago': 'Chile'}

def invertir_diccionario(paises_capitales): #Función que invierte el diccionario
    capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}  # Invertir el diccionario
    return capitales_paises 

def menu():
    paises_capitales = {
                        'Argentina': 'Buenos Aires',
                        'Brasil': 'Brasilia',
                        'Chile': 'Santiago',
                        'Uruguay': 'Montevideo'
                        }
    print("Diccionario original:")
    print(paises_capitales)
    capitales_paises = invertir_diccionario(paises_capitales)
    print("\nDiccionario invertido:")
    print(capitales_paises)

#Programa principal
#Nota: Si en el diccionario original hay dos países con la misma capital, al invertir, 
#se pierde uno de ellos, porque un diccionario no puede tener claves duplicadas.
menu()
print(" ")
print(" ")
print("###########################################################")

