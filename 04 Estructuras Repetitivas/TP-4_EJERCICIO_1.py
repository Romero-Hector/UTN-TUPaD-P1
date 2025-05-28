#EJERCICIO 1
#IMPRIME NUMEROS DEL 0 AL 100 - UNO POR LINEA
for cont in range (0,101,1):
    print (cont)

#EJERCICIO 2
#PROGRAMA QUE SOLICITA AL USUARIO A UN NUMERO ENTERO Y DETERMINAR LA CANTIDAD DE DIGITOS
print (" ")
print ("######################################")
numero = int (input("Ingrese un numero entero: "))
cantidad_digitos = len(str(abs(numero))) #utilizo abs para no tener problema con numeros negativos- convierte a
print(cantidad_digitos)                  #cadena y cuenta caracteres con len

#EJERCICIO 3
#Programa que suma todos los numeros enteros entre dos dados por el usuario
print (" ")
print ("#######################################")
suma = 0
numero_inferior = int(input("Ingrese el numero inferior: "))
numero_superior = int(input("Ingrese el numero superior: "))
for i in range(numero_inferior,numero_superior+1,1):
    suma = i + suma
print(suma)

#EJERCICIO 4
#Programa que suma los numeros enteros ingresados por el usuarios hasta que ingrese 0
print (" ")
print ("#######################################")
print(" ")
print("Este programa todos los numeros que ingrese, con 0 finaliza.")
print(" ")
suma = 0
#numero = int(input("Ingrese nùmero: "))
while numero != 0:
        if numero !=0:
            numero = int(input("Ingrese nùmero: "))
            suma = numero + suma
print(suma)
print ("fin")

#EJERCICIO 5
#Programa en el que el usuario juege adivinando un numero(que se genera demanera aleatorio entre 0 y 9)
print(" ")
print("#########################################")
import random
numero_azar = random.randint(1, 10)
contador_intentos = 1
print("Adivine un número entre 0 y 9")
numero_usuario = int(input("Ingrese un numero entero: "))
while numero_azar != numero_usuario:
        numero_usuario = int(input("Ingrese un numero entero: "))
        contador_intentos += 1
print("Despues de ",contador_intentos," intentos adivino el número: ", numero_azar)

#Ejercicio 6
#Programa que imprime todos los numeros pares entre 0 y 100 en orden decresiente
print(" ")
print("#########################################")
print(" ")
print("Imprime los números pares en orden decresiente entre 100 y 0")
for i in range (98,0,-2):
    print(i)   

#Ejercicio 7
#Programa que calcule la suma de todos los numeros  comprendidos ente 0 y un numero 
# entero positivo indicado por el usuario
print(" ") 
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(" ")
total = 0
numero_maximo = int(input("Ingrese un numero Maximo Entero: "))
for i in range (0, numero_maximo+1,1):
     total = total + i
print (" ")
print ("La Suma de todos los numeros entre 0 yel numero ingresaso", numero_maximo, "es: ", total)


#Ejercicio 8
#Ingresar 100 numeros y dterminar cuantos numeros son pares, impares, cuantos positivos y/o positivos
print (" ")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print (" ")
par = 0
impar = 0
positivos = 0
negativos = 0
n = 10 #Modificr para llevar a 100 valores 
numero = 0
for i in range (1,n+1,1):
    numero = int(input("Ingresar Numero Entero: "))
    if numero < 0: 
         negativos = negativos +1
    if numero > 0:
         positivos = positivos +1
    if numero %2 == 0:
         par = par +1
    if numero%2 != 0:
        impar = impar + 1
print ("Cantidad de positivos: ", positivos)
print ("Cantidad de negativos", negativos)
print ("Cantidad de impares: ", impar)
print ("Cantidad de pares: ", par)

# Ejercicio 9
# Ingresar 100 valores y calcula la media
print (" ")
print ("############################################")
print (" ")
numero = 10
suma = 0
valor = 0
for i in range (1,numero+1,1)
    valor = int(input("Ingrese ", numero, "valores para calcular la media: "))
    suma = int (suma + valor)

media = suma/numero
print("La meda de ",numero,"valores es: ")

# Ejercicio 10
# Invierte los digitos de un numero ingresado por el usuario
numero = input("Ingrese un número: ")
if numero.startswith('-'):
    numero_invertio = '-' + numero[:0:-1]
else:
     numero_invertido = numero[::-1]
print("Número invertido: ", numero_invertido)



