opcion = input("Ingresa si desea realizar una operacion o una tabla : ")
if opcion == "tabla":

 def imprimir_tabla(numero, operador, hasta):
    for factor in range(1, hasta, 8 + 1):
        
        if operador == '*':
            resultado = numero * factor
            print(f'{numero} * {factor} = {resultado}')
        else:
            print("Operador no válido")


elif opcion == "operacion":
    print ("Ingrese la operación que desea hacer: (suma, resta, multiplicacion, division): ")
    def calcular(opcion, num1, num2):
    
     num1 = int(num1)
     num2 = int(num2)
    
     if opcion == "suma":
        resultado = num1 + num2
        print(f'El resultado de la suma de {num1} y {num2} es: {resultado}')
     elif opcion == "resta":
        resultado = num1 - num2
        print(f'El resultado de la resta de {num1} y {num2} es: {resultado}')
     elif opcion == "multiplicacion":
        resultado = num1 * num2
        print(f'El resultado de la multiplicación de {num1} y {num2} es: {resultado}')
     elif opcion == "division":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f'El resultado de la división de {num1} y {num2} es: {resultado}')
     