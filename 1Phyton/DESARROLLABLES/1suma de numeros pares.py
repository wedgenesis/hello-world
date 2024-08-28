#escribe un programa que sume todos los numeros pares desde 1 hasta un numero n dado por el usuario.
n:int = int(input("Ingrese el número: "))

#inicializar la suma en 0
suma = 0

#iterar desde 1 hasta n
for x in range(0, n + 1):
    #verificar si el numero es par
    if x % 2 == 0:
        #sumar el numero par a la suma
        suma += x

#imprimir el resultado
print("la suma de todos los numero pares desde 1 hasta", n, "es:", suma)