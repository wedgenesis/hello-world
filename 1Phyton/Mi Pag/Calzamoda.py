'''Pagina de Bucaramanga, area de ventas'''
'''1. Productos en el mostrador (5 de ejemplo)
   2. Filtro de precios de mayor a menor 
   3. Tallas disponibles
   4. Descartar a base de las tallas
   5. Productos seleccionados por el cliente (carrito de compras)
   6. Pagar (Datos del cliente y metodo de pago)
   7. Factura generada
   8. Ingresar a bolsita los productos del cliente y despedir'''
   
#Dar Bienvenida

print: str = str ("Calzamoda Bucaramanga")

# Solicitar al usuario el tipo de producto que busca

print ("¿Que tipo de calzado busca? (Botas, Tacones, Sandalias): ")
estiloCalzado: str = str (input())

def botas (botasStyle, botaBrahmaColor, botasBramaTalla, botasBrahmaPrice, nombre, 
            fechaNacimiento, genero, cResidencia : str) -> str:
        print("___________________________________________________")
        print("nombre completo:", nombre)
        print("Fecha de nacimiento: ", fechaNacimiento)
        print("Género: ", genero)
        print("Ciudad de residencia: ", cResidencia)
        print("___________________________________________________")
        print("Opciones de botas:", botasStyle)
        print("Color de bota Brahma:", botaBrahmaColor)
        print("Talla de bota Brahma:", botasBramaTalla)
        print("Precio de bota Brahma:", botasBrahmaPrice)
        print("___________________________________________________")
        print("___________________________________________________")
        print("___________________________________________________")



#Datos de nombre usuario para su factura
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

#Datos de las botas disponibles
botasStyle: str = str ("Brahma Rx700, Vizzano P200, Cat rxt20")
#Datos de la brahma
botaBrahmaColor: str = str ("Pardo")
botasBramaTalla: str = str ("36, 37, 38")
botasBrahmaPrice: str = str ("488.000")

#Condiciones

if estiloCalzado == "Botas":
    botas (botasStyle, nombre, 
            fechaNacimiento, genero, cResidencia)       
else:
    print("Programa no reconocido. Por favor, ingrese 'programacion' o 'aviacion'.")