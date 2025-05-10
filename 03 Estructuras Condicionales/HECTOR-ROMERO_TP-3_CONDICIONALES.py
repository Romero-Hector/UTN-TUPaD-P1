# EJERCICIO 1
# Indica si es mayor o menor de edad
edad = int(input("¿Que edad tienes? "))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# EJERCICIO 2
# Se solicita nota al usario y se indica si aprobo o no
print (" ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
print (" ")
nota=float(input("¿Ingresa tu NOTA: "))
if nota >= 6:
    print("APROBO")
else:
    print("DESAPROBO")


# EJERCICIO 3   
# Escribir un programa que permita ingresar solo numeros pares. 
print (" ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
num = int(input("Ingrese un número par:  "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("Por favor, ingrese un número par")


# EJERCICIO 4
# Escribir un programa que solicite al usuario su edad. Determinar a que categoría pertenece
# según su edad: niño hasta 12 años --  adolescente entre 12 y 18 años -- adulto/joven entre 
# 18 y 30 años y adulto mayor o igual a 30 años
print (" ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
edad = int(input("Por favor, ingresa tu edad: "))
if edad < 12:
    print("Eres un niño")
elif edad >= 30:
    print("Eres un adulto mayor")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/joven")


# EJERCICIO 5
# Escribir un programa que permita introducir contraseñas entre 8 y 14 caracteres
# si se ingresa la cantidad correcta "Ha ingresado la contraseña correcta"
# si no "Por favor, ingrese una contraeña entre 8 y 14 caracteres"
print (" ")
print (" ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
contraseña = input("Por favor, ingrese su contraseña(entre 8 y 14 caracteres): ")
if len(contraseña) >= 8 and len(contraseña) <= 14: #len: obtiene la cantidad de elemenos en una cadena
    print("Ha ingresado la contraseña correcta") 
else:
    print("Por favor, ingrese una contraeña entre 8 y 14 caracteres")



# EJERCICIO 6
# Escribir un programa que permita utilizar el paquete statistics para calcular 
# la media, mediana y moda de una lista de números enteros aleatorios
# Para esto ultimo utilizamos random
print("  ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
print("  ")
import random
numeros_aleatorios=[random.randint(1,100)for i in range (50)]
print(numeros_aleatorios)
import statistics
moda = statistics.mode(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
print (f"Lamedia es: {media}")
print (f"La mediana es: {mediana}")
print (f"La moda es: {moda}")
print ("  ")
if media == mediana == moda:
        print("No tenemos sesgo")
elif media > mediana and mediana > moda:
        print("Tenemos sesgo positivo")
elif media < mediana and mediana < moda:
        print("Tenemos sesgo negativo")
elif media == mediana and media > moda:
        print("Tenemos sesgo positivo")
elif media == mediana and media < moda:
        print("Tenemos sesgo negativo")
elif media > mediana and media == moda:
        print("Tenemos sesgo positivo")
elif media < mediana and media == moda:
        print("Tenemos sesgo negativo")

#Ejercicio 7
# Escribir un programa que solicite alusuario una frase o palabra.
#Si ermina en vocal, añadir un signo de ! e imprimir.
#Si termnina en consonante, imprimir como ingreso
print("  ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
print("  ")
frase = input("Ingrese una frase o palabra: ")
if frase[-1] in "aeiouAEIOU":
    print(frase + "!")  
else:
    print(frase)


#Ejercicio 8
# Escribir un programa que para que e usuario ingrese una opcion elgiendo de 3 numeros
print("  ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
print("  ")
print("Elija una opcion: ")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Siquiere su nombre con la primere letra en mayúscula")
print("  ")
opcion = int(input("Seleccione opcion: "))
nombre = input("Ingrese su nombre: ")
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.capitalize())
else:
    print("Opcion no valida")
 
#Ejercicio 9
#Escribir un progrmaa que categorice la mangnitud de un terremoto según la escala de Richter

print("  ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
magnitud = int(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy Leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perseptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas pero sin daños)") 
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar dañosa esructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos")
elif magnitud >= 7 and magnitud < 8:
    print("Extremo (puede causar graves daños a gran escala)")
    
#Ejercicio 10
#Escribir un programa que informe estacion del año segun hemisferio y fecha
print("  ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))
hemisferio = input("Ingrese el hemisferio (N/S): ")
if hemisferio == "N" or hemisferio == "n":
    if (mes == 3 and dia >= 21) or (mes == 6 and dia < 21):
        print("Es primavera")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("Es verano")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia < 21):
        print("Es otoño")
    else:
        print("Es invierno")
elif hemisferio == "S" or hemisferio == "s":
    if (mes == 3 and dia >= 21) or (mes == 6 and dia < 21):
        print("Es otoño")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("Es invierno")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia < 21):
        print("Es primavera")
    else:
        print("Es verano")


