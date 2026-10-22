import numpy as np
# Emily Barraza NC 0025
# Ejemplos de numpy  Numerical Python 
print("-- Espaciado Linealmente en array -- 0025")
arre=np.linspace(start=0, stop=1, num=5)
print(arre)
print("-- Matriz indentidad en 2D array -- 0025")
matrix=np.eye(3)
print(matrix)
print("-- Genera numeros al azar(aleatorios) en 2D array -- 0025")
numale=np.random.random((3,4)) # Genera 12 numeros aleatorios
print(numale)
print("Genera 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3)) 
print(numale)
# como genera 9 números aleatorios aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3 por 3
print("Genera 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3,3)
print(arre)
print("Emily Barraza NC 0025")