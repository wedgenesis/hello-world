#escribir programa donde imprima un patron de estrellas defiido por el usuario
numero_de_filas = int(input("Introduce el número de filas para el patrón de estrellas: "))
for i in range(1, numero_de_filas + 1):
    print('*' * i)