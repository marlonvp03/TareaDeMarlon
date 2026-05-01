def mostrar_menu():

    print("\nMENÚ DE LA CESTA")
    print("\n1. AGREGAR un nuevo articulo.")
    print("2. MOSTRAR la cesta.")
    print("3. ELIMINAR un producto.")
    print("4. CALCULAR el total.")
    print("5. SALIR.")

def agregar_producto(cesta):

    print("\n--- Agregar Nuevo Articulo ---")
    nombre = input("Introduce el Nombre del Articulo: ").strip()

    while True:
        precio_str = input(f"Introduce el precio de '{nombre}': ").strip()
        if precio_str.replace('.', '', 1).isdigit():
            precio = float(precio_str)
            if precio >= 0:
                break
            else:
                print("ERROR. Intentalo de Nuevo.")
        else:
            print("ERROR. Introduce un Numero valido para el precio.")
    
    producto = {"nombre": nombre, "precio": precio}
    cesta.append(producto)
    print(f"¡'{nombre}' se ha añadido a la cesta!")

def mostrar_cesta(cesta):

    print("\n--- Contenido de tu Cesta---")
    if not cesta:
        print("Tu Cesta esta Vacia.")
    else:
        for i, producto in enumerate(cesta, 1):
            print(f"{i}. {producto['nombre']}: ${producto['precio']:.2f}")
    print("--------------------")

def eliminar_producto(cesta):

    print("\n--- Eliminar Producto ---")
    if not cesta:
        print("No tienes nada para eliminar.")
        return
    
    mostrar_cesta(cesta)

    while True:
        num_producto_str = input("Introduce el numero de productos que quieres eliminar: ").strip()
        if num_producto_str.isdigit():
            num_producto = int(num_producto_str)
            if 1 <= num_producto <= len(cesta):
                producto_eliminado = cesta.pop(num_producto - 1)
                print(f"¡'{producto_eliminado['nombre']}' ha sido eliminado.")
                break
            else:
                print(f"ERROR. El numero debe de estar entre 1 y {len(cesta)}.")
        else:
            print("ERROR> Por Favor, introduce un numero valido.")

def calcular_total(cesta):

    print("\n--- Total de la Compra ---")
    if not cesta:
        print("La cesta esta Vacia. El total es $0.00")
    else:
        total = sum(producto['precio'] for producto in cesta)
        print(f"El total a pagar es: ${total:.2f}")
    print("--------------------")

def main():

    cesta_de_compra = []

    print("¡Bienvenido a mi Tienda Virtual.!")

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-5): ")

        if opcion == '1':
            agregar_producto(cesta_de_compra)
        elif opcion == '2':
            mostrar_cesta(cesta_de_compra)
        elif opcion == '3':
            eliminar_producto(cesta_de_compra)
        elif opcion == '4':
            calcular_total(cesta_de_compra)
        elif opcion == '5':
            print("\n¡Gracias por usar mi Tienda Virtual! ¡Hasta Pronto!")
            break
        else:
            print("\nOpcion no Valida. por favor, elige un numero del 1 al 5.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()