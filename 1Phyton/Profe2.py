
print("Bienvenido, a continuación digite los siguientes datos para promediar su calificación final")

def calculadoraProfe(nota1, nota2):
    return (nota1 * 0.5) + (nota2 * 0.5)

def prog(programaProg, cicloProg, profesorProg, nombre, nota1, nota2, notaFinal):

    print("___________________________________________________")
    print("Nombre completo:", nombre)
    print("___________________________________________________")
    print("Programa:", programaProg)
    print("Ciclo:", cicloProg)
    print("Profesor:", profesorProg)
    print("___________________________________________________")
    print("Nota 1 del usuario:", nota1)
    print("Nota 2 del usuario:", nota2)
    print("___________________________________________________")
    print("Nota final del usuario:", notaFinal)
    print("___________________________________________________")

# Solicita datos del usuario 
nombre = input("Ingrese su nombre completo: ").upper()

# Solicitar las notas del usuario
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))

# Calcular la nota final
notaFinal = calculadoraProfe(nota1, nota2)
print("La nota final del estudiante es:", notaFinal)

if notaFinal < 50:
    print("El alumno reprobó.")
else:
    print("El alumno aprobó.")
        
# Datos del curso y semestre
programaProg = "Programación"
cicloProg = "Primer semestre"
profesorProg = "Juan Sebastian"

# Llamada a la función 
prog(programaProg, cicloProg, profesorProg, nombre, nota1, nota2, notaFinal)

