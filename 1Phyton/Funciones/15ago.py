"""Hacer un programa que reciba el nombre, fecha de nacimiento, sexo, ciudad de recidencia de un estudiante
que se va a inscirbir en el curso de programacion y que genere un recidbo de la inscripcion detallado ejemplo:
_______________________________
Nombre alumno:
Fecha nacimiento:
Genero:
Ciudad de residencia:
_______________________________
Matricula:
    Programa:
    Duracion:
    Salon:
    Bloque:
_______________________________
Total pagado:

(5 puntos se reclama)
todo con metodos, bien estructurado, tipado
condicion: nada mas de los datos deben de estar quemados, todo debe ser input ingresado, en un solo programa """





#calcular una funcion en donde con el programa escogido, retorne los datos
print ("Ingrese el programa al que desea inscribirse (programacion, aviacion): ")
carrera: str = str (input())
 
def prog (programaProg, duracionProg, bloqueProg, matriculaProg, salonProg, totalAPagarProg, nombre, 
            fechaNacimiento, genero, cResidencia : str) -> str:
        print("________________________________________________")
        print("nombre completo:", nombre)
        print("Fecha de nacimiento: ", fechaNacimiento)
        print("Género: ", genero)
        print("Ciudad de residencia: ", cResidencia)
        print("________________________________________________")
        print("Matricula:", matriculaProg)
        print("Programa:", programaProg)
        print("________________________________________________")
        print("Duracion:", duracionProg)
        print("Bloque:", bloqueProg)
        print("Salon:", salonProg)
        print("________________________________________________")
        print("Total a pagar:", totalAPagarProg)
        print("________________________________________________")


def avia (programaAvia, duracionAvia, bloqueAvia, matriculaAvia, salonAvia, totalAPagarAvia, nombre, 
            fechaNacimiento, genero, cResidencia : str) -> str:
        print("________________________________________________")
        print("nombre completo:", nombre)
        print("Fecha de nacimiento: ", fechaNacimiento)
        print("Género: ", genero)
        print("Ciudad de residencia: ", cResidencia)
        print("________________________________________________")
        print("Matricula:", matriculaAvia)
        print("Programa:", programaAvia)
        print("________________________________________________")
        print("Duracion:", duracionAvia)
        print("Bloque:", bloqueAvia)
        print("Salon:", salonAvia)
        print("________________________________________________")
        print("Total a pagar:", totalAPagarAvia)
        print("________________________________________________")

#Datos de nombre usuario
nombre: str = input("Ingrese su nombre completo: ").upper()

fechaNacimiento: str = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ").split() 

genero: str = input("Ingrese su genero: masculino/femenino/otros: ").upper()

generos = ["masculino", "femenino", "otros"]
while genero in (generos):
    if len (generos) == 9:
        print (genero)
    elif len (generos) == 8:
        print (genero)
    else:
        print ("otros")

cResidencia: str = input("Ingrese su ciudad de residencia: ").upper()

#Datos de programacion

programaProg: str = str ("Programacion")
bloqueProg: str = str ("9")
duracionProg: str = str ("Tres semestres")
matriculaProg: str = str ("9019209300000404328423842938498234")
salonProg: str = str ("115")
totalAPagarProg: str = str ("2.200.000")

#Datos de aviacion

programaAvia: str = str ("Aviación")
bloqueAvia: str = str ("6")
duracionAvia: str = str ("9 semestres")
matriculaAvia: str = str ("0997737290390202909387763456798776")
salonAvia: str = str ("210")
totalAPagarAvia: str = str ("15.000.000")

#Condiciones

if carrera == "programacion":
    prog (programaProg, duracionProg, bloqueProg, matriculaProg, salonProg, totalAPagarProg, nombre, 
            fechaNacimiento, genero, cResidencia)       
elif carrera == "aviacion":
    avia (programaAvia, duracionAvia, bloqueAvia, matriculaAvia, salonAvia, totalAPagarAvia, nombre, 
            fechaNacimiento, genero, cResidencia)
elif carrera == "diseño grafico":
    diseñoGraf
else:
    print("Programa no reconocido. Por favor, ingrese 'programacion' o 'aviacion'.")
