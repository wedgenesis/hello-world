# crear algoritmo que defina si un numero es par o no
#1. analizar mi algoritmo (Determinar)
#2. recibir un numero por parte del usuario
#3. retornar una respuesta (par o impar)
#4. validar que tipo de operacion debo realizar para evaluar el resultado (o)
#5. analizarla operacion para evaluar la condicion (si un numero es par o no)
n:int = int(input("Ingrese el número: "))

resultado_operacion: int = (n % 2)

if (n % 2) == 0:
    print (n, "es par.")
else:
    print (n, "no es par.")