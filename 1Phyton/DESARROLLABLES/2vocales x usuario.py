#Escribe un programa que cuente cuántas vocales hay en una palabra ingresada por el usuario.
letra: str = str(input("Ingrese la frase: ").lower())

vocales: str = "aeiouAEIOU"
#se inicia en 0 el contador pues empieza desde 0, y declaramos el tipado como entero int()
contador: int = 0
#iteramos la palabra que se encuentre en la variable letras existe 
for letra in letra:
    if letra in vocales:
        #debo de amarrarlo con el operador de asignacion, donde debo igualar al operador y lo suma 
       contador += 1
       #la f le da funcion al string, ahorra codigo, expersion regular
print(f"la frase tiene {contador} vocales")