def mostrar_bienvenida():
    print("¡Bienvenido a Calzamoda Bucaramanga!")
    print("Por favor, indique qué tipo de calzado busca: Botas, Tacones, Sandalias")

def solicitar_datos_usuario():
    nombre = input("Ingrese su nombre completo: ").upper()
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
    genero = input("Ingrese su género (masculino/femenino/otros): ").lower()
    ciudad_residencia = input("Ingrese su ciudad de residencia: ").upper()
    return nombre, fecha_nacimiento, genero, ciudad_residencia

def mostrar_botas(nombre, fecha_nacimiento, genero, ciudad_residencia):
    botas_style = "Brahma Rx700, Vizzano P200, Cat rxt20"
    bota_brahma_color = "Pardo"
    botas_brahma_talla = "36, 37, 38"
    botas_brahma_price = "488.000"
    
    print("___________________________________________________")
    print("Nombre completo:", nombre)
    print("Fecha de nacimiento:", fecha_nacimiento)
    print("Género:", genero.capitalize())
    print("Ciudad de residencia:", ciudad_residencia)
    print("___________________________________________________")
    print("Opciones de botas:", botas_style)
    print("Color de bota Brahma:", bota_brahma_color)
    print("Talla de bota Brahma:", botas_brahma_talla)
    print("Precio de bota Brahma:", botas_brahma_price)
    print("___________________________________________________")

def main():
    mostrar_bienvenida()
    estilo_calzado = input().strip().capitalize()
    
    if estilo_calzado == "Botas":
        nombre, fecha_nacimiento, genero, ciudad_residencia = solicitar_datos_usuario()
        
        if genero not in ["masculino", "femenino", "otros"]:
            print("Género no válido. Por favor, ingrese 'masculino', 'femenino' o 'otros'.")
        else:
            mostrar_botas(nombre, fecha_nacimiento, genero, ciudad_residencia)
    else:
        print("Tipo de calzado no reconocido. Por favor, ingrese 'Botas', 'Tacones' o 'Sandalias'.")

if __name__ == "__main__":
    main()
