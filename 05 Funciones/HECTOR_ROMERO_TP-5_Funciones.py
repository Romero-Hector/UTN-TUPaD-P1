#Ejercicio 1
#Crear una funcion llamada imprimir_hola_mundo, qu eimprima el mensaje "Hola Mundo!!!" 
#Llamar la funcion desde el programa principal
def imprimir_hola_mundo():
    print("Hola Mundo!!!")

#Programa principal
imprimir_hola_mundo()
print("  ")
print("  ")
print("###############################################################################")
print("  ")


#Ejercicio 2
#Crear una funcion lamada saludar_usuario(nombre), que reciba un parametro de tipo cadena y
#imprima el mensaje "Hola <nombre>!!!". Llamar la funcion desde el programa principal
def saludar_usuario(nombre):
    print(f"Hola {nombre}!!!")     

#Programa principal
nombre_usuario = input("Introduce tu nombre: ")
saludar_usuario(nombre_usuario)
print("  ")
print("  ")
print("###############################################################################")
print("  ")

#Ejercicio 3
#Crear una funcion llamada  informacion_personal(nombre,apelliso,edad,residencia), que reciba
#4 paráetros e imprima: "Soy [nombre], tengo[edad] años, vivo en [residencia]"
def informacion_personal(nombre, apellidos, edad, residencia):
    print(f"Soy {nombre} {apellidos}, tengo {edad} años, vivo en {residencia}")

#Programa principal
nombre = input("Introduce tu nombre: ") 
apellidos = input("Introduce tus apellidos: ")
edad = input("Introduce tu edad: ")
residencia = input("Introduce tu residencia: ")
informacion_personal(nombre, apellidos, edad, residencia)
print("  ")
print("  ")
print("###############################################################################")
print("  ")

#Ejercicio 4
#Crear dos funciones, 1)calcular_area_circulo(radio) que reciba el radio como parámetro y
#y devuelva el área del círculo. 2) calcular _perimetro_circulo(radio) que reciba el radio como parámetro
#y devuelva el preímetro del círculo. Solcitar el radio al usuario y mostrar los resultados.
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)   

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio  

def mostrar_resultados(area, perimetro):
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")  

#Programa principal
radio = float(input("Introduce el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
mostrar_resultados(area, perimetro)
#print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
print("  ")
print("  ")
print("###############################################################################")
print("  ")


#Ejercicio 5
#Crear una fucnión llamada segundos_a_horas(segundos) que reciba una cantidad de segundos
# como parámetro y devuelva la cantidad de horas correspondiente. Solcitar al usuarios los 
#segundos y mostrar el resultado.
def ingresar_segundos():
    segundos = int(input("Ingrese la cantidad de segundos: "))
    return segundos

def segundos_a_horas(segundos):
    horas = segundos // 3600 
    return horas 
   
def mostrar_resultado(segundos, horas):
    print(f"{segundos} segundos son {horas} horas.")

segundos = ingresar_segundos()
horas = segundos_a_horas(segundos)
mostrar_resultado(segundos, horas)

#ejercicio 6
#Crear una funcion llamada tabla_multiplicar(numero) que reciba un número entero como
#parámetro y muestre la tabla de multiplicar del número del 1 al 10. Llamar a la función desde el programa principal.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")  
 
#Programa principal
print("  ") 
print("  ")
numero = int(input("Introduce un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)
print("  ")
print("  ")
print("###############################################################################")

#Ejercicio 7
#Crear una función llamada operaciones_basicas(a,b) que reciba dos numeros como parametros
#y devuelva una tupla con la suma, resta, multiplicación y división de los números.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Para evitar la división por cero, se verifica que b no sea cero
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    return (suma, resta, multiplicacion, division)# Devuelve una tupla con los resultados


#Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(a, b)
print(resultado)
print("  ")
print("  ")
print("###############################################################################")

#Ejercicio 8
#Crear una funcion llamada calcular_imc(peso, altura) que reciba el peso en kg y la altura en m
#y devuelva el índice de masa corporal (IMC) calculado con la fórmula IMC = peso / (altura ** 2).
def calcular_imc(peso, altura):
    if altura <= 0:
        return "Error: La altura debe ser mayor que cero."
    imc = peso / (altura ** 2)
    return imc

#Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
if isinstance(imc, str):
    print(imc)  # Imprime el mensaje de error si la altura es cero o negativa
else:
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
print("  ")
print("  ")
print("###############################################################################")

#Ejercicio 9
#Crear una funcion llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius
#y devuelva la temperatura equivalente en grados Fahrenheit. Solicitar al usuarios la temperatura en Celsius
##y mostrar el resultado.
#F = C * 9/5 + 32.
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

#Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F")
print("  ")
print("  ")
print("###############################################################################")


#Ejercicio 10
#Crear una función llamada calcular_promedio(a,b,c) que reciba tres números como parámetros
#y devuelva el promedio de esos números. Solicitar al usuario los números y mostrar el resultado
#usano esta función.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio 

def solicitar_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    return a, b, c
def mostrar_resultado(promedio):

    print(f"El promedio de los números es: {promedio:.2f}")

#Programa principal
numeros = solicitar_numeros()
promedio = calcular_promedio(*numeros)  # Desempaqueta la tupla de números
mostrar_resultado(promedio)
print("  ")
print("  ")
print("###############################################################################")


