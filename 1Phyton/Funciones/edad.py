#calcular una funcion en donde con la fecha de mi nacimiento, retorne cuantos años tengo
def yearNacimiento(year: int) -> int:
    yearActual: int = int (2024)
    resultadoEdad: int = (yearActual-year)
    return resultadoEdad
miEdad: int = yearNacimiento (2005)
print (miEdad)