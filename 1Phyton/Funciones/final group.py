print ("Ingrese el programa al que desea inscribirse (programacion, aviacion, diseño grafico): ")
carrera: str = str (input())
 
def prog (programaProg, duracionProg, bloqueProg, matriculaProg, salonProg, totalAPagarProg, nombre, 
            fechaNacimiento, genero, cResidencia : str) -> str:
        print("___________________________________________________")
        print("nombre completo:", nombre)
        print("Fecha de nacimiento: ", fechaNacimiento)
        print("Género: ", genero)
        print("Ciudad de residencia: ", cResidencia)
        print("___________________________________________________")
        print("Matricula:", matriculaProg)
        print("Programa:", programaProg)
        print("___________________________________________________")
        print("Duracion:", duracionProg)
        print("Bloque:", bloqueProg)
        print("Salon:", salonProg)
        print("___________________________________________________")
        print("Total a pagar:", totalAPagarProg)
        print("___________________________________________________")


def avia (programaAvia, duracionAvia, bloqueAvia, matriculaAvia, salonAvia, totalAPagarAvia, nombre, 
            fechaNacimiento, genero, cResidencia : str) -> str:
        print("___________________________________________________")
        print("nombre completo:", nombre)
        print("Fecha de nacimiento: ", fechaNacimiento)
        print("Género: ", genero)
        print("Ciudad de residencia: ", cResidencia)
        print("___________________________________________________")
        print("Matricula:", matriculaAvia)
        print("Programa:", programaAvia)
        print("___________________________________________________")
        print("Duracion:", duracionAvia)
        print("Bloque:", bloqueAvia)
        print("Salon:", salonAvia)
        print("___________________________________________________")
        print("Total a pagar:", totalAPagarAvia)
        print("___________________________________________________")


def diseñograf (programaDiseñograf, duracionDiseñograf, bloqueDiseñograf, matriculaDiseñograf, salonDiseñograf, 
                totalAPagarDiseñograf, nombre, fechaNacimiento, genero, cResidencia : str) -> str:
        print("___________________________________________________")
        print("nombre completo:", nombre)
        print("Fecha de nacimiento: ", fechaNacimiento)
        print("Género: ", genero)
        print("Ciudad de residencia: ", cResidencia)
        print("___________________________________________________")
        print("Matricula:", matriculaDiseñograf)
        print("Programa:", programaDiseñograf)
        print("___________________________________________________")
        print("Duracion:", duracionDiseñograf)
        print("Bloque:", bloqueDiseñograf)
        print("Salon:", salonDiseñograf)
        print("___________________________________________________")
        print("Total a pagar:", totalAPagarDiseñograf)
        print("___________________________________________________")

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

#Datos de Diseño Grafico

programaDiseñograf: str = str ("Diseño Gráfico")
bloqueDiseñograf: str = str ("5")
duracionDiseñograf: str = str ("8 semestres")
matriculaDiseñograf: str = str ("0997737290390202909387763456798776")
salonDiseñograf: str = str ("136")
totalAPagarDiseñograf: str = str ("6.000.000")

#Condiciones

if carrera == "programacion":
    prog (programaProg, duracionProg, bloqueProg, matriculaProg, salonProg, totalAPagarProg, nombre, 
            fechaNacimiento, genero, cResidencia)       
elif carrera == "aviacion":
    avia (programaAvia, duracionAvia, bloqueAvia, matriculaAvia, salonAvia, totalAPagarAvia, nombre, 
            fechaNacimiento, genero, cResidencia)
elif carrera == "diseño grafico":
    diseñograf (programaDiseñograf, duracionDiseñograf, bloqueDiseñograf, matriculaDiseñograf, salonDiseñograf, totalAPagarDiseñograf, nombre, 
            fechaNacimiento, genero, cResidencia)
else:
    print("Programa no reconocido. Por favor, ingrese 'programacion' o 'aviacion'.")