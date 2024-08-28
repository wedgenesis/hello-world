# Solicitar al usuario los datos necesarios
numero = int(input("Ingrese el número base para la tabla: "))
operador = input("Ingrese el operador ('+', '-', '*', '/'): ").strip()
hasta = int(input("Ingrese hasta qué número desea imprimir la tabla: "))

def imprimir_tabla(numero, operador, hasta):
    # verificar que el operador sea válido
    if operador not in ['+', '-', '*', '/']:
        print("Operador no válido. Por favor use '+', '-', '*', '/'.")
        return
    
    # Realizar las operaciones y mostrar los resultados
    for factor in range(1, hasta + 1):
        if operador == '+':
            resultado = numero + factor
        elif operador == '-':
            resultado = numero - factor
        elif operador == '*':
            resultado = numero * factor
        elif operador == '/':
            if factor != 0:
                resultado = numero / factor
            else:
                resultado = "Indefinido (división por cero)"
        print (f"{numero} {operador} {factor} = {resultado}")

        
# Llamar a la función
imprimir_tabla(numero, operador, hasta)