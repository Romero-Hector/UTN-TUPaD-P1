import matplotlib.pyplot as plt #visualización de datos
import random                   #crear listas aleatorias para ordenar
import time                     #medir el tiempo de ejecución

# ------------------- Quick Sort ( -------------------
def quick_sort(arr, low=0, high=None):          # Ordena el arreglo usando el algoritmo Quick Sort
    if high is None:                            # Si high no se ha definido, lo establece al último índice del arreglo  
        high = len(arr) - 1                        
    if low < high:
        pi = partition(arr, low, high)          # Llama a la función de partición y obtiene el índice del pivote
        visualize(arr, low, high, pi)           # Visualiza el proceso de ordenamiento
        quick_sort(arr, low, pi - 1)            # Llama recursivamente a quick_sort para las dos mitades del arreglo
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):                  # Divide el arreglo en dos partes y devuelve el índice del pivote
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        visualize(arr, low, high, high)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def visualize(arr, low, high, pivot_index):     # Visualiza el proceso de ordenamiento
    plt.clf()
    color_array = []
    for idx in range(len(arr)):
        if idx == pivot_index:
            color_array.append('green')   # pivote
        elif low <= idx <= high:
            color_array.append('red')     # segmento actual
        else:
            color_array.append('blue')    # resto
    plt.bar(range(len(arr)), arr, color=color_array)
    plt.pause(0.3)

# ------------------- Búsqueda Binaria -------------------
def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"Buscando... izquierda: {izquierda}, derecha: {derecha}, medio: {medio}")
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# ------------------- Principal -------------------
if __name__ == "__main__":
    # Crear lista aleatoria
    data = random.sample(range(1, 50), 20)  #Lista de 20 números aleatorios entre 1 y 50
    print("Lista original:", data)          #Imprime la lista generada

    # Visualización inicial 
    plt.ion()                               #Activa el “modo interactivo” de matplotlib.
    plt.figure(figsize=(10, 6))             #Define el tamaño de la figura

    # Ordenamiento con Quick Sort
    start = time.time()                     # Medir el tiempo de inicio
    quick_sort(data)
    end = time.time()                       # Medir el tiempo de finalización   

    plt.ioff()                              # Desactiva el modo interactivo 
    plt.show()                              # Muestra la visualización final

    print("Lista ordenada:", data)
    print(f"Tiempo de ordenamiento: {end - start:.4f} segundos")

    # Búsqueda binaria
    try:
        valor = int(input("Ingrese un número para buscar en la lista ordenada: "))
        resultado = busqueda_binaria(data, valor)
        if resultado != -1:
            print(f"Número {valor} encontrado en la posición {resultado}")
        else:
            print(f"Número {valor} no encontrado en la lista")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")
