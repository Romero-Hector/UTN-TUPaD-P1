#Ejercicio 1
#Creas una lista con los numeros del 1 al 100 que sean múltiplose de 4, 
#Utilizar la función range
print("Ejercicio 1")
lista = list(range(4,101,4))
print(lista)
print(" ")
print(" ")
print("=================================================================")

#Ejercicio 2
#Crear una lista con 5 elementos(colocar nunúmeros cualesquiera) y mostrar
#el penúltimo. Investigar como funciona el indexing con numeros negativos
print("Ejercicio 2")
lista2 = [10, 20, 30, 40, 50]
print(lista2)
print("El penúltimo elemento de la lista es:", lista2[-2])#-1 es e ultimo elemento;
#-2 es el penúltimo; -3 es el antepenúltimo, etc.
print(" ")
print(" ")
print("=================================================================")

#Ejercicio 3
#crear una lista vacía, agregar tres palabras con append e imprimir la lista
#resultante por pantalla. Pista lista_vacia = []
print("Ejercicio 3")
lista_vacia = []
lista_vacia.append("do")
lista_vacia.append("re")
lista_vacia.append("mi")
print("Lista resultante:", lista_vacia)
print(" ")
print(" ")
print("=================================================================")

#Ejercicio 4
#Reemplazar e segundo y último valor de la lista "animales" con las palabras 
#"loro" y "oso" respectivamente. Imprimir las lista resultante por pantalla.
#Investigar a función indexing con números negativos
print("Ejercicio 4")
animales = ["gato", "perro", "conejo", "pez", "tortuga"]
print("Lista Inicial:    ",animales)
animales[1] = "loro"  # Reemplaza el segundo elemento (índice 1)
animales[-1] = "oso"  # Reemplaza el último elemento (índice -1)   
print("Lista resultante: ", animales)
print(" ")
print("=================================================================")

#Ejercicio 5
#Analizar el siguiente programa y explicar que realiza
print("Ejercicio 5")
numeros = [8,15,3,22,7] 
print("Lista dada:   ", numeros)                      #Lista dada
print("Valor máximo: ", max(numeros))     
numeros.remove(max(numeros))                        # Elimina el valor máximo de la lista
print("Lista c/valor máximo eliminado: ",numeros)    #Lista sin el valor máximo
print("Lista resultante: ", animales)
print(" ")
print("=================================================================")

#Ejercicio 6
#Crear una lista con numeros del 10 al 30 (inlcuido), haciendo saltos de 5 en 5 y mostrando
#y mostrar por pantalla los dos primeros
print("Ejercicio 6")
lista_numeros = list(range(10,31,5))                                        # hasta el 31 para incluir el 30
print("Lista de números del 10 al 30 con saltos de 5:", lista_numeros)      # escribo la lista
print("Los dos primeros números de la lista son:     ", lista_numeros[:2])  # muestra los dos primeros elementos
print(" ")
print("=================================================================")

#Ejercicio 7
#Reemplazar los dos valores centrales(indices 1 y 2) de la lista "autos" por dos nuevos valores cualesquiera
print("Ejercicio 7")
autos = ["Golf", "Polo", "Suran", "Gol"]  #lista dada "autos"
print("Lista inicial: ", autos)                   
autos[1:3] = ["Fiesta", "Focus"]          # Reemplaza los valores 1 el índice 1(incluido) hasta el índice 3(excluido)
print("Lista resultante: ", autos)        # Lista con los valores reemplazados
print(" ")  
print("=================================================================")

#Ejercicio 8
#Crear una lista vacia llamada "dobles" y agregar agregar el doble de 5,10,15 
#usando append directamente. Imprimir las lista resultante por pantalla
print("Ejercicio 8")
dobles = []                        # lista vacía
for i in range(5, 16, 5):          # iterar desde 5 hasta 15 con saltos de 5
    dobles.append(i * 2)           # agregar el doble de cada número a la lista
print("Lista de dobles:", dobles)  # imprimir la lista final
print(" ")
print("=================================================================")


#Ejercicio 9
#Dada la lsita "compras" cuyos elementos repreentan productos comprados por
#diferentes cliente.
print("Ejercicio 9")
compras = [["pan", "leche"],["arroz", "fideos", "salsa"],["agua"]]
print("Lista de compras:", compras)  # Imprimir la lista de compras
#print("Cantidad de clientes:", len(compras))  # Imprimir la cantidad de clientes
#print("Cantidad de productos del primer cliente:", len(compras[0]))  # Imprimir la cantidad de productos del primer cliente
#print("Cantidad de productos del segundo cliente:", len(compras[1]))  # Imprimir la cantidad de productos del segundo cliente
#print("Cantidad de productos del tercer cliente:", len(compras[2]))  # Imprimir la cantidad de productos del tercer cliente
compras[2].append("jugo")
print("Se agrego jugo a la lista del cliente 3: ", compras)  # se agrego jugo al cliente 3
compras[1][1]=["tallarines"]
print("Se reemplazo fideos por tallarines en la lista del cliente 2: ", compras)  # se reemplazo "fideos" por "tallarines" al cliente 2
if "pan" in compras[0]:
    compras[0].remove("pan")   # se elimino "pan" del cliente 1 
print("Se eliminó pan de la lista del cliente 1:", compras)
print("Lista resultante de compras:",compras)  # Imprimir la lista de compras final
print(" ")
print("=================================================================")

#Ejercicio 10
#Elaborar una lista anidada "lista_anidada" 
print("Ejercicio 10")
lista_anidada = [
    15,
    True,
    [25.5,57.9,30.6],
    False
    ]
print("Lista anidada:", lista_anidada)  # Imprimir la lista anidada


